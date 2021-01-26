"""Tests related to context contract definition as marshmallow schema."""
import pytest
from marshmallow import Schema
from marshmallow.fields import Integer
from marshmallow.fields import List
from marshmallow.fields import String
from stories import arguments
from stories import Result
from stories import story
from stories import Success
from stories.exceptions import ContextContractError

from stories_marshmallow import contract
from stories_marshmallow.exceptions import StoryMarshmallowError


def test_contract_unsupported_argument():
    """Context contract should be applied to the story."""
    with pytest.raises(StoryMarshmallowError) as exc_info:
        contract(1)

    assert str(exc_info.value) == "Contract should be called on story"


@pytest.mark.parametrize("v", [1, int])
def test_contract_unsupported_type(v):
    """Context contract should require marshmallow schema as an argument."""

    class Action:
        @story
        def do(I):
            I.one

    with pytest.raises(StoryMarshmallowError) as exc_info:
        contract(Action.do)(v)

    assert str(exc_info.value) == "Story contract should be a marshmallow schema"


def test_keep_contract_class():
    """Context contract decorator should keep marshmallow schema as is."""
    assert issubclass(State, Schema)


def test_contract_converter():
    """Context contract should convert marshmallow schema to regular contract."""
    action = Action(lambda: [2])
    assert action.do(foo=1, bar="a") == [2]


@pytest.mark.parametrize(
    ("value", "message"),
    [("a", "Not a valid list."), (["a"], "0:\n    Not a valid integer.")],
)
def test_contract_assignment_error(value, message):
    """Context contract should handle state attribute assignment validation."""
    expected = f"""
This variable violates context contract: 'baz'

Function returned value: Action.one

Violations:

baz:
  {value!r}
  {message}

Contract:
  baz: List  # Variable in Action.do
    """.strip()

    action = Action(lambda: value)
    with pytest.raises(ContextContractError) as exc_info:
        action.do(foo=1, bar="a")

    assert str(exc_info.value) == expected


class Action:
    """A service."""

    @story
    @arguments("foo", "bar")
    def do(I):
        """Do something."""
        I.one
        I.two

    def one(self, state):
        """Do step."""
        state.baz = self.f()
        return Success()

    def two(self, state):
        """Do step."""
        return Result(state.baz)

    def __init__(self, f):
        self.f = f


@contract(Action.do)
class State(Schema):
    """A contract for the state of the service."""

    foo = Integer()
    bar = String()
    baz = List(Integer())
