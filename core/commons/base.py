import functools
from abc import ABC


class Base(ABC):
    @classmethod
    def default_kwargs(cls, **default_kwargs):
        """
        default_kwargs

        Args:
            **default_kwargs (): -

        Returns:
            Callable
        """

        def decorator(fn):
            @functools.wraps(fn)
            def g(*args, **kwargs):
                default_kwargs.update(kwargs)
                return fn(*args, **default_kwargs)

            return g

        return decorator
