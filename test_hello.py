from hello import greet


def test_greet():
    assert greet("World") == "Hello, World!"


def test_greet_with_different_name():
    assert greet("Claude") == "Hello, Claude!"
