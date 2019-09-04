from abc import abstractmethod, ABC


class Loggable(ABC):

    @abstractmethod
    def get_as_string(self) -> str:
        pass
