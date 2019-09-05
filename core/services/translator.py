from typing import Dict

from core.interfaces.singleton import Singleton


class Translator(metaclass=Singleton):

    __metaclass__ = Singleton

    key_en_value: Dict[str, str] = {
        "db_choose": "Please choose database"
    }

    def __init__(self, default_lang = "en") -> None:
        self.lang = default_lang
        pass

    def translate(self, key: str, lang = "en") -> str:
        if key in self.key_en_value:
            return self.__translate(self.key_en_value[key], lang)
        return key

    def __translate(self, mstring: str, lang = "en") -> str:
        # TODO
        return mstring
