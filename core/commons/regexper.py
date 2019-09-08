import re

from core.commons import log_objects


class Regexper:

    @staticmethod
    def clean_str(rgx_iterable, mstring: str) -> str:
        """
        clean_str

        Args:
            rgx_iterable (): -
            mstring (str): -

        Returns:
            str
        """
        new_str = mstring
        for rgx_match in rgx_iterable:
            new_str = re.sub(rgx_match, '', new_str)
        return new_str

    @staticmethod
    def clean_white_chars(mstring: str) -> str:
        """
        clean_white_chars

        Args:
            mstring (str):

        Returns:
            str
        """
        return re.sub('\s+', ' ', str)

    @staticmethod
    def find_between(s, first, last) -> str:
        """
        find_between

        Args:
            s ():
            first ():
            last ():

        Returns:
            str
        """
        try:
            start = s.index(first) + len(first)
            end = s.index(last, start)
            return s[start:end]
        except ValueError as e:
            log_objects(e)
            return ""
        except Exception as e:
            log_objects(e)

    @staticmethod
    def find_between_rindex(s, first, last) -> str:
        """
        find_between_rindex

        Args:
            s ():
            first ():
            last ():

        Returns:
            str
        """
        try:
            start = s.rindex(first) + len(first)
            end = s.rindex(last, start)
            return s[start:end]
        except ValueError:
            return ""
        except Exception as e:
            log_objects(e)
