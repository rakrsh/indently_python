from __future__ import annotations

from ast import List
from random import shuffle

people: list[str] = ['Bob', 'Tom', 'James', 'Sandra']
shuffle(people)
print(people)
