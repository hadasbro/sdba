from functools import partial
from typing import Callable, Dict, Any

from core.commons import log_objects


class Memoize():

    def __init__(self, func: Callable[..., Any]) -> None:
        """
        __init__
        Args:
            func (Callable[..., Any]): -
        """
        self.__func: Callable[..., Any] = func
        self.__cache: Dict[str, Any] = {}
        '''
        TODO
        [__predicate should be optional lambda expression - which tells us
        what conditions should we meet to take data from cache or to reload data]
        '''
        self.__predicate: Callable[..., bool] = lambda: True

    def __get__(self, obj, objtype=None) -> Any:
        """
        __get__

        Args:
            obj (): -
            objtype (): -

        Returns:
            Any
        """
        if obj is None:
            return self.__func
        return partial(self, obj)

    def __call__(self, posarg, *args, **kwargs) -> Any:
        """
        __call__

        Args:
            posarg (): -
            *args (): -
            **kwargs (): -

        Returns:
            Any
        """
        key: str = (self.__func, posarg, args[1:], frozenset(kwargs.items())).__str__()
        try:
            if self.__predicate() == False:
                raise KeyError()
            res = self.__cache[key]
        except KeyError:
            res = self.__cache[key] = self.__func(posarg, *args, **kwargs)
        except Exception as e:
            log_objects(e)
        return res
