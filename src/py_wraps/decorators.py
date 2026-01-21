"""General decorators (alphabetically organized) to be used within python callables."""

import functools
import re
import typing as tp

P = tp.ParamSpec("P")
T = tp.TypeVar("T")


def count_words(func: tp.Callable[P, str]) -> tp.Callable[P, str]:
    """Decorator to count the words of any string, ignoring any non-word character.
    It expects that the decorated function returns a simple string.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> str:
        text = func(*args, **kwargs)
        words = re.findall(r"\w+", text)
        print(
            "---- Word Count Audit ----"
            f"Total Count: {len(words)}"
            "--------------------------",
            flush=True,
        )
        # Return the original text so the program continues normally
        return text

    return wrapper
