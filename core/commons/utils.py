import json
import re
from typing import List, Any, Dict, Union


class Utils:

    @staticmethod
    def list_to_str_lit(elements: List[Any]) -> List[str]:
        """
        list_to_str_lit

        Args:
            elements (List[Any]): -

        Returns:
            List[str]: list
        """
        return list(map(lambda x: x.__str__(), elements))

    @staticmethod
    def dict_of_dicts_merge(x: Dict[Any, Any], y: Dict[Any, Any]) -> Dict[Any, Any]:
        """
        dict_of_dicts_merge

        Args:
            x (Dict[Any, Any]): -
            y (Dict[Any, Any]): -

        Returns:
            Dict[Any, Any]: dict
        """
        return {**x, **y}

    @staticmethod
    def filter_empty(elements: List[str]) -> List[str]:
        """
        filter_empty

        Args:
            elements (List[str]): -

        Returns:
            List[str]: list
        """
        return list(filter(lambda x: x != "", elements))

    @staticmethod
    def dict_to_json(dict_obj: Dict[str, Any]) -> str:
        """
        dict_to_json

        Args:
            dict_obj (Dict[str, Any]): -

        Returns:
            str
        """
        return json.dumps(dict_obj, default=str)

    @staticmethod
    def clear_breaks(mstr: Union[str, List[str]], charlist: str = "[\n\t\r]+") -> Union[str, List[str]]:
        """
        clear_breaks

        Args:
            mstr (Union[str, List[str]]): -
            charlist (str): -

        Returns:
            Union[str, List[str]]: list or str
        """
        c_breaks = lambda x: re.sub(r"" + charlist, "", x)

        if isinstance(mstr, list):
            return list(map(c_breaks, mstr))
        else:
            return c_breaks(mstr)
