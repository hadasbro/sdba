from core.commons import log_objects


class HtmlIzer():

    def __init__(self, wrp: str = '<span class="{}">{}</span>') -> None:

        self.wrapper = wrp

    @staticmethod
    def is_number(n: str) -> bool:
        """
        is_number

        Args:
            n (str): -

        Returns:
            bool: True - yes, False - no
        """
        try:
            float(n)
        except ValueError as e:
            return False
        except Exception as e:
            log_objects(e)
        return True

    @staticmethod
    def is_on_off(mstr: str) -> bool:
        """
        is_on_off

        Args:
            mstr (str): -

        Returns:
            bool: True/False
        """
        return mstr.strip().upper() == "ON" or mstr.strip().upper() == "OFF"

    @staticmethod
    def is_path(mstr: str) -> bool:
        """
        is_path

        Args:
            mstr (str): -

        Returns:
            bool
        """
        return mstr.__contains__("\/") or mstr.__contains__("\\")

    def span_number(self, n: str) -> None:
        """
        span_number

        Args:
            n (): -

        Returns:

        """
        return self.wrapper.format('span_number', n)

    def span_on_off(self, n: str) -> None:
        """
        span_on_off

        Args:
            n (str): -

        Returns:

        """
        return self.wrapper.format('span_on_off', n)

    def span_path(self, n: str) -> None:
        """
        span_path

        Args:
            n (str): -

        Returns:

        """
        return self.wrapper.format('span_path', n)

    def span_normal(self, n: str) -> None:
        """
        span_normal

        Args:
            n (str): -

        Returns:

        """
        return self.wrapper.format('span_normal', n)

    def wrap_types(self, mstr: str) -> str:
        """
        wrap_types

        Args:
            mstr (str): -

        Returns:

        """
        if HtmlIzer.is_number(mstr):
            res = self.span_number(mstr)
        elif HtmlIzer.is_on_off(mstr):
            res = self.span_on_off(mstr)
        elif HtmlIzer.is_path(mstr):
            res = self.span_path(mstr)
        else:
            res = self.span_normal(mstr)

        return res
