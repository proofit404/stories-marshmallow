# Contract

`marshmallow` schema could be used to define state contract on the story.
Validators would be applied at the moment of variable assignment or passed to
arguments. Validators are defined according to fields of the schema.

```pycon

>>> from marshmallow import Schema
>>> from marshmallow.fields import Integer, List, String
>>> from stories import story, Success
>>> from stories_marshmallow import contract

>>> class Action:
...
...     @story
...     def do(I):
...         I.one
...         I.two
...         I.three
...
...     def one(self, state):
...         state.foo = self.get_foo()
...         return Success()
...
...     def two(self, state):
...         state.bar = self.get_bar()
...         return Success()
...
...     def three(self, state):
...         state.baz= self.get_baz()
...         return Success()

>>> @contract(Action.do)
... class State(Schema):
...     foo = String()
...     bar = Integer()
...     baz = List(Integer())

```

In the code below we could see what would happen if all state variables were
correct.

```pycon

>>> class Correct(Action):
...
...     def get_foo(self):
...         return 'a'
...
...     def get_bar(self):
...         return 1
...
...     def get_baz(self):
...         return [1]

>>> Correct().do()

```

And we would see clear error, if some variable didn't pass validation.

```pycon

>>> class Incorrect(Action):
...
...     def get_foo(self):
...         return 'a'
...
...     def get_bar(self):
...         return 'a'
...
...     def get_baz(self):
...         return [1]

>>> Incorrect().do()
Traceback (most recent call last):
  ...
_stories.exceptions.ContextContractError: This variable violates context contract: 'bar'
<BLANKLINE>
Function returned value: Incorrect.two
<BLANKLINE>
Violations:
<BLANKLINE>
bar:
  'a'
  Not a valid integer.
<BLANKLINE>
Contract:
  bar: Integer  # Variable in Incorrect.do

```
