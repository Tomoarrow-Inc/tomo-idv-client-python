import base64
import json
from urllib.parse import parse_qs

from cryptography.hazmat.primitives.asymmetric import ec, utils
from cryptography.hazmat.primitives.hashes import SHA256

from tomo_idv_client import (
    CLIENT_ASSERTION_TYPE,
    BodyOptions,
    ClientAssertionOptions,
    build_token_request,
    create_client_assertion,
)


def test_create_client_assertion_signs_es256_jwt():
    # This test proves that the SDK helper creates the OAuth2 client assertion
    # expected by idv-server: correct JWT claims and a verifiable ES256 signature.
    private_key = ec.generate_private_key(ec.SECP256R1())
    secret_key = _private_key_to_encoded_jwk(private_key)

    jwt = create_client_assertion(
        ClientAssertionOptions(
            client_id="client-123",
            secret_key=secret_key,
            base_url="https://api.example.test",
        )
    )

    header, payload, signature = jwt.split(".")
    decoded_header = json.loads(_base64url_decode(header))
    decoded_payload = json.loads(_base64url_decode(payload))

    assert decoded_header == {"alg": "ES256", "typ": "JWT"}
    assert decoded_payload["iss"] == "client-123"
    assert decoded_payload["sub"] == "client-123"
    assert decoded_payload["aud"] == "https://api.example.test/v1/oauth2/token"
    assert decoded_payload["exp"] - decoded_payload["iat"] == 300
    assert decoded_payload["jti"]

    raw_signature = _base64url_decode(signature)
    der_signature = utils.encode_dss_signature(
        int.from_bytes(raw_signature[:32], "big"),
        int.from_bytes(raw_signature[32:], "big"),
    )
    private_key.public_key().verify(
        der_signature,
        f"{header}.{payload}".encode("utf-8"),
        ec.ECDSA(SHA256()),
    )


def test_build_token_request_uses_default_oauth_fields():
    # This test locks the public form body contract shared with the Node and
    # Kotlin SDKs, including the default scope/resource/assertion type values.
    request = build_token_request("assertion-value")
    parsed = parse_qs(request.body)

    assert request.headers == {"Content-Type": "application/x-www-form-urlencoded"}
    assert parsed["grant_type"] == ["client_credentials"]
    assert parsed["scope"] == ["idv.read"]
    assert parsed["resource"] == ["https://api.tomopayment.com/v1/idv"]
    assert parsed["client_assertion_type"] == [CLIENT_ASSERTION_TYPE]
    assert parsed["client_assertion"] == ["assertion-value"]


def test_build_token_request_accepts_overrides():
    # This test keeps custom token request options usable for customer-specific
    # OAuth2 deployments without changing the default request behavior.
    request = build_token_request(
        "assertion-value",
        BodyOptions(scope="idv.write", resource="https://resource.example.test"),
    )
    parsed = parse_qs(request.body)

    assert parsed["scope"] == ["idv.write"]
    assert parsed["resource"] == ["https://resource.example.test"]


def _private_key_to_encoded_jwk(private_key):
    numbers = private_key.private_numbers()
    public_numbers = numbers.public_numbers
    jwk = {
        "kty": "EC",
        "crv": "P-256",
        "d": _base64url_encode(numbers.private_value.to_bytes(32, "big")),
        "x": _base64url_encode(public_numbers.x.to_bytes(32, "big")),
        "y": _base64url_encode(public_numbers.y.to_bytes(32, "big")),
    }
    return _base64url_encode(json.dumps(jwk, separators=(",", ":")).encode("utf-8"))


def _base64url_encode(data):
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def _base64url_decode(data):
    padded = data + "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(padded.encode("ascii"))
