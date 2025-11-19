"""Tests for core module."""

import pytest

from {{ cookiecutter.package_name }}.core import hello


def test_hello_default():
    """Test hello function with default argument."""
    assert hello() == "Hello, World!"


def test_hello_custom_name():
    """Test hello function with custom name."""
    assert hello("Alice") == "Hello, Alice!"


@pytest.mark.parametrize(
    "name,expected",
    [
        ("Bob", "Hello, Bob!"),
        ("Charlie", "Hello, Charlie!"),
        ("", "Hello, !"),
    ],
)
def test_hello_parametrized(name, expected):
    """Test hello function with multiple inputs."""
    assert hello(name) == expected