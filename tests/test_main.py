import pytest
from app.main import hello_world

def test_hello_world():
    assert hello_world() == "Hello, Code Camp!"
