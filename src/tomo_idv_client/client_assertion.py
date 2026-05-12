from __future__ import annotations

import base64
import json
import time
import uuid
from dataclasses import dataclass
from typing import Dict, Optional
from urllib.parse import urlencode

from cryptography.hazmat.primitives.asymmetric import ec, utils
from cryptography.hazmat.primitives.hashes import SHA256


CLIENT_ASSERTION_TYPE = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
DEFAULT_RESOURCE = "https://api.tomopayment.com/v1/idv"


@dataclass(frozen=True)
class ClientAssertionOptions:
    client_id: str
    secret_key: str
    base_url: str


@dataclass(frozen=True)
class BodyOptions:
    grant_type: str = "client_credentials"
    scope: str = "idv.read"
    resource: str = DEFAULT_RESOURCE
    client_assertion_type: str = CLIENT_ASSERTION_TYPE


@dataclass(frozen=True)
class TokenRequestData:
    headers: Dict[str, str]
    body: str


def create_client_assertion(options: ClientAssertionOptions) -> str:
    private_jwk = _decode_base64url_jwk(options.secret_key)
    private_key = _jwk_to_private_key(private_jwk)

    now = int(time.time())
    payload = {
        "iss": options.client_id,
        "sub": options.client_id,
        "aud": f"{options.base_url}/v1/oauth2/token",
        "iat": now,
        "exp": now + 300,
        "jti": str(uuid.uuid4()),
    }
    return _sign_jwt(private_key, payload)


def build_token_request(
    client_assertion: str,
    options: Optional[BodyOptions] = None,
) -> TokenRequestData:
    body_options = options or BodyOptions()
    body = urlencode(
        {
            "grant_type": body_options.grant_type,
            "scope": body_options.scope,
            "resource": body_options.resource,
            "client_assertion_type": body_options.client_assertion_type,
            "client_assertion": client_assertion,
        }
    )
    return TokenRequestData(
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        body=body,
    )


def _sign_jwt(private_key: ec.EllipticCurvePrivateKey, payload: Dict[str, object]) -> str:
    header = {"alg": "ES256", "typ": "JWT"}
    signing_input = ".".join(
        [
            _base64url_encode(json.dumps(header, separators=(",", ":")).encode("utf-8")),
            _base64url_encode(json.dumps(payload, separators=(",", ":")).encode("utf-8")),
        ]
    )
    der_signature = private_key.sign(signing_input.encode("utf-8"), ec.ECDSA(SHA256()))
    r, s = utils.decode_dss_signature(der_signature)
    raw_signature = r.to_bytes(32, "big") + s.to_bytes(32, "big")
    return f"{signing_input}.{_base64url_encode(raw_signature)}"


def _decode_base64url_jwk(encoded_jwk: str) -> Dict[str, str]:
    try:
        decoded = _base64url_decode(encoded_jwk).decode("utf-8")
        jwk = json.loads(decoded)
    except Exception as error:
        raise ValueError(f"Failed to decode base64url JWK: {error}") from error

    if jwk.get("kty") != "EC" or jwk.get("crv") != "P-256" or "d" not in jwk:
        raise ValueError("secret_key must encode an EC P-256 private JWK")
    return jwk


def _jwk_to_private_key(jwk: Dict[str, str]) -> ec.EllipticCurvePrivateKey:
    private_value = int.from_bytes(_base64url_decode(jwk["d"]), "big")
    return ec.derive_private_key(private_value, ec.SECP256R1())


def _base64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def _base64url_decode(data: str) -> bytes:
    padded = data + "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(padded.encode("ascii"))
