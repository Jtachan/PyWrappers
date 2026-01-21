"""General decorators (alphabetically organized) to be used within python callables."""

import functools
import re
import time
import typing as tp

# Type hinting setup
P = tp.ParamSpec("P")
T = tp.TypeVar("T")


def count_words(func: tp.Callable[P, str]) -> tp.Callable[P, str]:
    """Decorator to count the words of any string.

    The decorator expects that the decorated function returns a simple string.
    The logic of the decorator ignores any non-word character (such as emojis) but
    considers numbers (for exaple, the year '2026') also as words.

    Examples
    --------
    ```pycon
    >>> from py_wraps.decorators import count_words
    >>> @count_words
    ... def get_user_bio(name: str, age: int) -> str:
    ...     return f"Hello! My name is {name}, I am {age} years old 🚀."
    >>> print(get_user_bio("Alice", 30))
    Total word count: 10
    Hello! My name is Alice, I am 30 years old 🚀.
    ```
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> str:
        text = func(*args, **kwargs)
        words = re.findall(r"\w+", text)
        print(f"Total word count: {len(words)}")
        # Return the original text so the program continues normally
        return text

    return wrapper


def time_execution(func: tp.Callable[P, T]) -> tp.Callable[P, T]:
    """A decorator that measures and prints the execution time of a function.

    The decorator differs from the [`timeit`](https://docs.python.org/3/library/timeit.html)
    module as the module is defined to measure small bits of Python code (allowing
    multiple repetitions) while the decorator displays the runtime of the single
    decorated function.

    Examples
    --------
    ```pycon
    >>> from py_wraps.decorators import time_execution
    >>> @time_execution
    ... def heavy_computation(n: int) -> list[int]:
    ...     return [i**2 for i in range(n)]
    >>> heavy_computation(50_000)
    Function 'heavy_computation' executed in 0.002569 seconds
    ```
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> T:
        start_time = time.perf_counter()
        # Execute the original function
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(
            f"Function '{func.__name__}' executed in "
            f"{end_time - start_time:.6f} seconds"
        )
        return result

    return wrapper
