from __future__ import annotations

from typing import Any


class Book:
    def __init__(self, title: str, pages: int) -> None:
        self.title = title
        self.pages = pages

    def __format__(self, format_spec: Any) -> str:
        match format_spec:
            case 'time':
                return f'{self.pages / 60:.2f}h'
            case 'caps':
                return self.title.upper()
            case _:
                raise ValueError('Unknown specifier for Book()')


def main() -> None:
    hairy_potter: Book = Book('Very Hairy potter', 300)
    python_daily: Book = Book('Python Daily', 30)

    print(f'{python_daily:caps}')
    print(f'Read time: {python_daily:time}')

    print(f'{hairy_potter:caps}')
    print(f'Read time: {hairy_potter:time}')


if __name__ == '__main__':
    main()
