from abc import ABC


class JsonSerializable(ABC):
    def serialize(self):
        pass


class Dicteadble(ABC):
    def get_as_dict(self):
        pass
