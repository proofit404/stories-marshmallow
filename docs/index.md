# Stories marshmallow

[![azure-devops-builds](https://img.shields.io/azure-devops/build/proofit404/stories-marshmallow/19?style=flat-square)](https://dev.azure.com/proofit404/stories-marshmallow/_build/latest?definitionId=19&branchName=master)
[![azure-devops-coverage](https://img.shields.io/azure-devops/coverage/proofit404/stories-marshmallow/19?style=flat-square)](https://dev.azure.com/proofit404/stories-marshmallow/_build/latest?definitionId=19&branchName=master)
[![pypi](https://img.shields.io/pypi/v/stories-marshmallow?style=flat-square)](https://pypi.org/project/stories-marshmallow)
[![python](https://img.shields.io/pypi/pyversions/stories-marshmallow?style=flat-square)](https://pypi.org/project/stories-marshmallow)

Use marshmallow schemas as stories context contract.

**[Documentation](https://proofit404.github.io/stories-marshmallow) |
[Source Code](https://github.com/proofit404/stories-marshmallow) |
[Task Tracker](https://github.com/proofit404/stories-marshmallow/issues)**

A paragraph of text explaining the goal of the library…

## Pros

- A feature
- B feature
- etc

## Example

A line of text explaining snippet below…

```pycon

>>> from marshmallow import Schema
>>> from marshmallow.fields import String
>>> from stories import story, Success
>>> from stories_marshmallow import contract

>>> class Purchase:
...
...     @story
...     def make(I):
...         I.find_user
...
...     def find_user(self, state):
...         return Success()

>>> @contract(Purchase.make)
... class State(Schema):
...
...     user = String()

```

## Questions

If you have any questions, feel free to create an issue in our
[Task Tracker](https://github.com/proofit404/stories-marshmallow/issues). We
have the
[question label](https://github.com/proofit404/stories-marshmallow/issues?q=is%3Aopen+is%3Aissue+label%3Aquestion)
exactly for this purpose.

## Enterprise support

If you have an issue with any version of the library, you can apply for a paid
enterprise support contract. This will guarantee you that no breaking changes
will happen to you. No matter how old version you're using at the moment. All
necessary features and bug fixes will be backported in a way that serves your
needs.

Please contact [proofit404@gmail.com](mailto:proofit404@gmail.com) if you're
interested in it.

## License

`stories-marshmallow` library is offered under the two clause BSD license.

<p align="center">&mdash; ⭐️ &mdash;</p>
<p align="center"><i>The `stories-marshmallow` library is part of the SOLID python family.</i></p>
