import logging
from functools import singledispatch
from typing import List, Callable, TypeVar, Type, Tuple, Union

T = TypeVar('T')


class StaticLogger:
    _logger = None

    @staticmethod
    def log(obj: Union[List[T], Tuple[T, ...]],
            log_producer: Callable[[Type[T]], Union[str, None]] = lambda el: str(el)) -> None:
        """
        log

        Args:
            obj (Union[List[T], Tuple[T, ...]]): -
            log_producer (Callable[[Type[T]], Union[str, None]]): -

        Returns:
            None
        """
        if StaticLogger._logger is None:
            logging.basicConfig(level=logging.INFO)
            StaticLogger._logger = logging.getLogger("static_logger")
            pass

        """
        call custom handler
        """
        for i in obj:
            log_producer(i)


@singledispatch
def log_objects(obj) -> None:
    """
    log_objects
    Args:
        obj (): -

    Returns:
        None
    """
    raise NotImplementedError("Cannot log state for this object")
