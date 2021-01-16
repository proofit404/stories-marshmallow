"""Tests related to stories_marshmallow module."""
from stories_marshmallow import contract
from stories_marshmallow.exceptions import StoryMarshmallowError


def test_exception():
    """`StoryMarshmallowError` should be Exception subclass."""
    assert issubclass(StoryMarshmallowError, Exception)
    assert contract(1) == 1
