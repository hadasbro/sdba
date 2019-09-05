import re
from typing import Any


class Hasher():

    WRAP_REGEX: str = '<HASHED_DATA_SDBA>{(.+?)}</HASHED_DATA_SDBA>'

    @staticmethod
    def _unhash(estr: str) -> str:
        """
        _unhash

        Args:
            estr (str):

        Returns:
            str
        """
        estr = str(estr)
        return estr

    @staticmethod
    def _hash(estr: str) -> str:
        """
        _hash

        Args:
            estr ():

        Returns:
            str
        """
        estr = str(estr)
        return Hasher.WRAP_REGEX.replace("{(.+?)}", "{}").format(str(estr))

    @staticmethod
    def decode_data(strdata: Any) -> Any:
        """
        decode_data

        Args:
            strdata (Any):

        Returns:
            Any
        """
        hasher_tag: str = Hasher.WRAP_REGEX.split('{')[0]

        def decode(estr: str) -> str:
            if hasher_tag not in str(estr):
                return estr
            else:
                patters: str = Hasher.WRAP_REGEX.replace("{", "").replace("}", "")
                m = re.search(patters, estr)
                if m:
                    found = m.group(1)
                    return Hasher._unhash(found)
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


    @staticmethod
    def encode_data(strdata: Any):
        """
        encode_data

        Args:
            strdata (Any):

        Returns:
            Any
        """
        hasher_tag: str = Hasher.WRAP_REGEX.split('{')[0]

        def encode(estr: str) -> str:

            if hasher_tag in str(estr):
                return estr
            else:
                return Hasher._hash(estr)

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
