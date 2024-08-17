# Example of tuple and string
from typing import Tuple as tuple

coordinates: tuple[float, float] = (1, 2)
print("Before: ", id(coordinates))
coordinates += 3,
print("After: ", id(coordinates))

