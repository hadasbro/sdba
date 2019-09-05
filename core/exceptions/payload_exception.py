from typing import Any


class PayloadException(Exception):
    def __init__(self, msg: str = "", payload: Any = None):
        super().__init__(msg)
        self.payload = payload
