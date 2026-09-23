from photo_audit.main import hello_world


def test_hello_world() -> None:
    """Test hello world."""
    assert hello_world() == "Hello, World!"
