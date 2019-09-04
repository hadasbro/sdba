from enum import Enum
from typing import Union, Tuple, Dict, Any, List

from mysql.connector import Error, MySQLConnection

from core.commons import log_objects
from core.commons.query_log import QueryLog


class DBS_fetch_num(Enum):
    ALL = 1
    ONE = 2


class DBS_fetch_types(Enum):
    ASSOC = "ASSOC"
    ROW = "ROW"


class DBS():

    @property
    def connected(self) -> bool:
        """
        connected

        Returns:
            bool
        """
        return self._connected

    @property
    def connection(self) -> int:
        """
        connection

        Returns:
            int
        """
        return self._connection

    @connected.setter
    def connected(self, rc: bool) -> None:
        self._connected = rc

    @connection.setter
    def connection(self, rc: Union[MySQLConnection, None]) -> Union[MySQLConnection, None]:
        self._connection = rc

    def __init__(self, connection: Union[MySQLConnection, None]) -> None:
        """
        __init__

        Args:
            connection ():
        """
        self._connected = False
        self._connection: Union[MySQLConnection, None] = None

        try:

            pass

        except Error as e:
            log_objects(e)

        finally:
            pass

    def __fetch(
            self,
            query: str,
            fetch_num: DBS_fetch_num = DBS_fetch_num.ALL,
            fetch_type: DBS_fetch_types = DBS_fetch_types.ROW,
            params: Tuple[Union[str, int, float]] = ()
    ) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        """
        __fetch

        Args:
            query (DBS_fetch_num): -
            fetch_num (DBS_fetch_types): -
            fetch_type (Tuple[Union[str, int, float]]): -
            params (Tuple[Union[str, int, float]]): -

        Returns:
            Union[List[Dict[str, Any]], Dict[str, Any]]
        """

        log_objects(QueryLog(query, params))

        cursor = self._connection.cursor()
        cursor.execute(query, params)
        if fetch_num == DBS_fetch_num.ONE:
            res = cursor.fetchone()
        else:
            res = cursor.fetchall()

        if fetch_type == DBS_fetch_types.ROW:
            return res
        else:
            if fetch_num == DBS_fetch_num.ONE:
                res = [res]
            fields = [column[0] for column in cursor.description]
            result = [dict(line) for line in [zip(fields, row) for row in res]]
            if fetch_num == DBS_fetch_num.ONE:
                return result[0]
            return result

    def fetchAll(self, query: str, fetch_type: DBS_fetch_types = DBS_fetch_types.ROW,
                 params: Tuple[Union[str, int, float]] = ()) -> List[Dict[str, Any]]:
        """

        Args:
            query (str): -
            fetch_type (DBS_fetch_types): -
            params (Tuple[Union[str, int, float]]): -

        Returns:
            List[Dict[str, Any]]
        """

        return self.__fetch(query, DBS_fetch_num.ALL, fetch_type, params)

    def fetchOne(self, query: str, fetch_type: DBS_fetch_types = DBS_fetch_types.ROW,
                 params: Tuple[Union[str, int, float]] = ()) -> Dict[str, Any]:
        """
        fetchOne
        Args:
            query (str): -
            fetch_type (DBS_fetch_types): -
            params (Tuple[Union[str, int, float]]): -

        Returns:
            Dict[str, Any]
        """
        return self.__fetch(query, DBS_fetch_num.ONE, fetch_type, params)
