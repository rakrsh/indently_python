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


def main() -> None:
    state: State = State.ON

    if state == State.ON:
        print('Turned ON!')
    elif state == State.OFF:
        print('Turned OFF!')
    else:
        assert_never(state)


if __name__ == '__main__':
    main()
