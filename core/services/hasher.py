import re
from typing import Any
from core import Program
from core.interfaces.singleton import Singleton
from cryptography.fernet import Fernet


class Hasher(metaclass=Singleton):
    __metaclass__ = Singleton

    WRAP_REGEX: str = '<HASHED_DATA_SDBA>{(.+?)}</HASHED_DATA_SDBA>'

    def __init__(self) -> None:
        self.__crypto_key = Program.get_crypto_key()

    def _unhash(self, estr: str) -> str:
        """
        _unhash

        Args:
            estr (str):

        Returns:
            _unhash
        """
        f = Fernet(self.__crypto_key)
        decrypted = f.decrypt(estr.encode(Program.ENCODING))
        return decrypted

    def _hash(self, estr: str) -> str:
        """
        _hash

        Args:
            estr (str):

        Returns:
            str
        """
        message = str(estr).encode()
        f = Fernet(self.__crypto_key)
        encrypted_str: str = f.encrypt(message).decode(Program.ENCODING)
        return self.WRAP_REGEX.replace("{(.+?)}", "{}").format(encrypted_str)

    def decode_data(self, strdata: Any) -> Any:
        """
        decode_data

        Args:
            strdata (Any):

        Returns:
            Any
        """
        hasher_tag: str = self.WRAP_REGEX.split('{')[0]

        def decode(estr: str) -> str:
            if hasher_tag not in str(estr):
                return estr
            else:
                patters: str = self.WRAP_REGEX.replace("{", "").replace("}", "")
                m = re.search(patters, estr)
                if m:
                    found = m.group(1)
                    return self._unhash(found)
                elif estr == self.WRAP_REGEX.replace("{(.+?)}", ""):
                    return ""
                else:
                    return estr

                return estr

        if isinstance(strdata, dict):
            ndct = {}
            for k, v in strdata.items():
                if isinstance(v, dict):
                    ndct[k] = v
                else:
                    ndct[k] = decode(v)
            return ndct
        else:
            return decode(strdata)

    def encode_data(self, strdata: Any) -> str:
        """
        encode_data

        Args:
            strdata (Any):

        Returns:
            str
        """
        hasher_tag: str = self.WRAP_REGEX.split('{')[0]

        def encode(estr: str) -> str:

            if hasher_tag in str(estr):
                return estr
            else:
                return self._hash(estr)

        if isinstance(strdata, dict):
            ndct = {}
            for k, v in strdata.items():
                if isinstance(v, dict):
                    ndct[k] = v
                else:
                    ndct[k] = encode(v)
            return ndct
        else:
            return encode(strdata)
