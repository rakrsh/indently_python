from __future__ import annotations
numbers: list[int] = list(range(1, 11))
text: str = 'Hello World!'

rev: slice = slice(None, None, -1)
print(numbers[rev])
print(text[rev])
