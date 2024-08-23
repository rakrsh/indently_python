from __future__ import annotations


numbers: list[int] = list(range(1, 11))
text: str = 'Hello World!'

rev: slice = slice(None, None, -1)
print(numbers[rev])
print(text[rev])


# Set operations
set_a: set[int] = {1, 2, 3, 4, 5}
set_b: set[int] = {4, 5, 6, 7, 8}

print(f"{set_a | set_b}")
print(f"{set_a - set_b}")
print(f"{set_b - set_a}")
print(f"{set_b & set_a}")
print(f"{set_b ^ set_a}")
