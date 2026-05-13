from tomo_idv_client import Configuration, DefaultApi, StartIdvReq


def test_generated_client_exports_importable_api_and_model():
    # This test verifies that OpenAPI code generation was copied into the public
    # package and that top-level SDK exports expose representative generated API
    # and model classes.
    configuration = Configuration(host="https://api.example.test")
    api = DefaultApi()
    model = StartIdvReq(
        callback_url="https://example.com/callback",
        user_id="user-123",
    )

    assert configuration.host == "https://api.example.test"
    assert api is not None
    assert model.user_id == "user-123"
