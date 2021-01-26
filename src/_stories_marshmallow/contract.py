from functools import singledispatch
from inspect import isclass

from _stories.mounted import ClassMountedStory
from marshmallow import Schema
from marshmallow import ValidationError

from _stories_marshmallow.exceptions import StoryMarshmallowError


def contract(story):
    """Convert marshmallow schema to stories context contract."""
    if not isinstance(story, ClassMountedStory):
        raise StoryMarshmallowError("Contract should be called on story")

    def wrapper(cls):
        if not (isclass(cls) and issubclass(cls, Schema)):
            raise StoryMarshmallowError("Story contract should be a marshmallow schema")
        story.contract({name: _Validator(cls, name) for name in cls._declared_fields})
        return cls

    return wrapper


class _Validator:
    def __init__(self, spec, field):
        self.spec = spec
        self.field = field

    def __call__(self, value):
        try:
            return self.spec().load({self.field: value}).get(self.field), None
        except ValidationError as error:
            return None, _format_errors(error.messages[self.field])

    def __repr__(self):
        return self.spec._declared_fields[self.field].__class__.__name__

    @property
    def __name__(self):
        # Workaround.
        return repr(self)


@singledispatch
def _format_errors():
    ...  # pragma: no cover


@_format_errors.register(dict)
def _(errors):
    return _format_errors(
        [
            [_format_errors(key) + ":", _format_errors(values, indent="    ")]
            for key, values in errors.items()
        ]
    )


@_format_errors.register(list)
def _(errors, *, indent=""):
    return indent + f"{indent}\n".join(_format_errors(error) for error in errors)


@_format_errors.register(int)
def _(error):
    return str(error)


@_format_errors.register(str)
def _(error):
    return error
