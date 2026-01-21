# PyWrappers

`PyWrappers` is a library containing wrappers and decorators for python development.
All these wrappers are intended to be used with debugging purposes.

To install the package, use the GitHub link:
```
pip install git+https://github.com/Jtachan/PyWrappers
```

`PyWrappers` does not need of any other third-party Python package for its installation. 

!!! note
    The package right now is an alpha version of some algorithms that I usually need.

## Basic usage

Use the name `py_wraps` to import the functionality of the package:

```python
from py_wraps.decorators import *


# Usage of `PyWrappers` decorators
@count_words
def get_user_bio(name: str, age: int) -> str:
    return f"Hello! My name is {name}, I am {age} years old 🚀."

@time_execution
def heavy_computation(n: int) -> list[int]:
    return [i**2 for i in range(n)]


print(get_user_bio("Alice", 30))
# Total word count: 10
# Hello! My name is Alice, I am 30 years old 🚀.
heavy_computation(50_000)
# Function 'heavy_computation' executed in 0.002569 seconds
```

!!! hint
    Consider using a logger for a more custom printing.
