# Example of tuple and string
from __future__ import annotations

from typing import Tuple as tuple

coordinates: tuple[float, float] = (1, 2)
print('Before: ', id(coordinates))
coordinates += 3,  # type: ignore
print('After: ', id(coordinates))
