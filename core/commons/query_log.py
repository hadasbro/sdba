from typing import Tuple, Union


class QueryLog:
    def __init__(self, query: str, params: Tuple[Union[str, int, float]] = ()) -> None:
        """
        __init__

        Args:
            query (str): -
            params ( Tuple[Union[str, int, float]]): -

        Returns:
            None
        """
        self.query = query
        self.params = params

    def __str__(self) -> str:
        """
        __str__

        Returns:
            str
        """
        if len(self.params) > 0:
            try:
                sql = self.query
                sql = sql \
                    .replace("%s", "_percent_s_") \
                    .replace("%", "%%") \
                    .replace("_percent_s_", "%s")
                return sql % tuple(
                    map(
                        lambda x: "'{}'".format(x.__str__().replace("'", "\"")), self.params
                    )
                )
            except Exception:
                return "Query Log Exception"
        else:
            return self.query
