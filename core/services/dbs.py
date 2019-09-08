from enum import Enum
from typing import Union, Tuple, Dict, Any, List

from mysql.connector import Error, MySQLConnection

from core.commons import log_objects
from core.commons.query_log import QueryLog


class DBSFetchNum(Enum):
    ALL = 1
    ONE = 2


class DSBFetchTypes(Enum):
    ASSOC = "ASSOC"
    ROW = "ROW"


class DBS:

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

    @staticmethod
    def parse_db_error(db_err: Exception):
        # ...
        # parse error code
        #  if per.errno == 1142: access denied
        raise

    def __init__(self, credentials=None) -> None:
        """
        __init__

        """

        try:

            mysql_con = MySQLConnection()

            mysql_con.connect(
                host=credentials.get_host(),
                user=credentials.get_user(),
                passwd=credentials.get_password()
            )

            self._connected = True
            self._connection = mysql_con

        except Error as e:
            log_objects(e)
            raise e

        finally:
            pass

    def __fetch(
            self,
            query: str,
            fetch_num: DBSFetchNum = DBSFetchNum.ALL,
            fetch_type: DSBFetchTypes = DSBFetchTypes.ROW,
            params: Tuple[Union[str, int, float]] = ()
    ) -> Union[List[Dict[str, Any]], Dict[str, Any]]:

        """
        __fetch

        Args:
            query (DBSFetchNum): -
            fetch_num (DSBFetchTypes): -
            fetch_type (Tuple[Union[str, int, float]]): -
            params (Tuple[Union[str, int, float]]): -

        Returns:
            Union[List[Dict[str, Any]], Dict[str, Any]]
        """

        log_objects(QueryLog(query, params))

        cursor = self._connection.cursor()
        cursor.execute(query, params)

        if fetch_num == DBSFetchNum.ONE:
            res = cursor.fetchone()
        else:
            res = cursor.fetchall()

        if res is None:
            res = []

        if fetch_type == DSBFetchTypes.ROW:
            return res
        else:
            if fetch_num == DBSFetchNum.ONE:
                res = [res]
            fields = [column[0] for column in cursor.description]
            result = [dict(line) for line in [zip(fields, row) for row in res]]
            if fetch_num == DBSFetchNum.ONE:
                return result[0]
            return result

    def fetchAll(self, query: str, fetch_type: DSBFetchTypes = DSBFetchTypes.ROW,
                 params: Tuple[Union[str, int, float]] = ()) -> List[Dict[str, Any]]:
        """
        fetchAll

        Args:
            query (str): -
            fetch_type (DSBFetchTypes): -
            params (Tuple[Union[str, int, float]]): -

        Returns:
            List[Dict[str, Any]]
        """

        return self.__fetch(query, DBSFetchNum.ALL, fetch_type, params)

    def fetchOne(self, query: str, fetch_type: DSBFetchTypes = DSBFetchTypes.ROW,
                 params: Tuple[Union[str, int, float]] = ()) -> Dict[str, Any]:
        """
        fetchOne

        Args:
            query (str): -
            fetch_type (DSBFetchTypes): -
            params (Tuple[Union[str, int, float]]): -

        Returns:
            Dict[str, Any]
        """
        return self.__fetch(query, DBSFetchNum.ONE, fetch_type, params)
