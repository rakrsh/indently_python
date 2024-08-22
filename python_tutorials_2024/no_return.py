from __future__ import annotations

from enum import Enum
from typing import Never
from typing import NoReturn


def func(msg: str) -> NoReturn:
    raise Exception(msg)


def assert_never(arg: Never) -> NoReturn:
    raise AssertionError('Expected code is unreachable')


class State(Enum):
    OFF: int = 0
    ON: int = 1
