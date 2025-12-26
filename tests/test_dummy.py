from module.settings import settings


def test_dummy() -> None:
    """A dummy test that always passes."""
    print(settings.model_dump())
    print("Dummy test executed")
    assert True
