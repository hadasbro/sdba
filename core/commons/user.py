from core.interfaces.singleton import Singleton


class User(metaclass=Singleton):
    __metaclass__ = Singleton

    def __init__(self, start_point: int = 0) -> None:
        """
        __init__

        Args:
            start_point (int):
        """
        self.start_point = start_point;

# a = User(1)
# b = User(2)
