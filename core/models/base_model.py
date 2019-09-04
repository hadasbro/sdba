from abc import ABC
from core.commons import log_objects


class BaseModel(ABC):
    def __init__(self) -> None:
        log_objects(self)
