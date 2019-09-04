import time
from collections import Callable
from typing import Dict, Any

RT = Callable[..., Dict[str, Any]]
BT = Callable[..., int]


def decorator_check_duration(precision: int = 5) -> Callable[[BT], RT]:
    """
    decorator_check_duration

    Args:
        precision (int): -

    Returns:
        Callable
    """

    def wrap(f: BT) -> RT:
        def wrapped_f(**range: int) -> Dict[str, Any]:
            start: float = time.time()
            res = f(**range)
            end: float = time.time()
            return {"result": res, "time": round(end - start, precision)}

        return wrapped_f

    return wrap
