import pytest

def test_app_is_importable():
    from app import app as application
    assert application

def test_foo():
    assert 1 is True
