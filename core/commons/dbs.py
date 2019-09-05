import json
from enum import Enum
from typing import Union, Tuple, Dict, Any, List

from mysql.connector import Error, MySQLConnection

from core.commons import log_objects
from core.commons.query_log import QueryLog
from core.commons.utils import Utils
from core.interfaces.json_serializable import JsonSerializable, Dicteadble


class dbs_fetch_num(Enum):
    ALL = 1
    ONE = 2


class dbs_fetch_types(Enum):
    ASSOC = "ASSOC"
    ROW = "ROW"


class db_credentials(JsonSerializable, Dicteadble):

    class TYPE(Enum):
        MYSQL = 1

    __id = 0
    __connection = 0

    def __init__(self,
                 id: int,
                 host: str,
                 user: str,
                 password: str,
                 port: int = 3306,
                 type: TYPE = TYPE.MYSQL,
                 ssl: bool = False
                 ) -> None:
        """
        __init__

        Args:
            id (int): -
            host (str):  -
            user (str):  -
            password (str):  -
            port (int):  -
            type (TYPE):  -
            ssl (bool):  -
        """
        self.__id: int = id
        self.__host: str = host
        self.__type: db_credentials.TYPE = type
        self.__user: str = user
        self.__password: str = password
        self.__port: int = port
        self.__ssl: bool = ssl

    def get_id(self) -> int:
        """
        get_id

        Returns:
            int
        """
        return self.__id

    def get_host(self) -> str:
        """
        get_host

        Returns:
            str
        """
        return self.__host

    def get_type(self) -> 'db_credentials.TYPE':
        """
        get_type

        Returns:
            db_instance.TYPE
        """
        return self.__type

    def get_user(self) -> str:
        """
        get_user

        Returns:
            str
        """
        return self.__user

    def get_password(self) -> str:
        """
        get_password

        Returns:

        """
        return self.__password

    def get_port(self) -> int:
        """
        get_port

        Returns:
            str
        """
        return self.__port

    def get_ssl(self) -> int:
        """
        get_ssl

        Returns:
            int
        """
        return self.__ssl

    def __repr__(self) -> bool:
        """
        __repr__

        Returns:
            bool
        """
        return self.serialize()

    def __str__(self) -> str:
        """
        __str__

        Returns:
            str
        """
        return self.serialize()

    def serialize(self) -> str:
        """
        serialize

        Returns:
            str
        """
        return Utils.dict_to_json((self.__dict__))

    def get_as_dict(self) -> Dict[str, Any]:
        """
        get_as_dict

        Returns:
            Dict[str, Any]: dict
        """
        return {
            'id': self.get_id(),
            'host': self.get_host(),
            'user': self.get_user(),
            'password': self.get_password(),
            'port': self.get_port(),
            'type': self.get_type(),
            'ssl': self.get_ssl()
        }

    @staticmethod
    def from_dict(dval: Dict[str, str]) -> 'db_credentials':
        try:
            return db_credentials(
                dval['id'],
                dval['host'],
                dval['user'],
                dval['password'],
                dval['port'],
                dval['type'],
                dval['ssl']
            )
        except AttributeError as ex:
            raise ex

    @staticmethod
    def from_json(json_str: str) -> 'db_credentials':
        """
        from_json

        Args:
            json_str ():

        Returns:

        """
        ldata = json.loads(json_str)
        try:
            return db_credentials.from_dict(ldata)
        except AttributeError as ex:
            raise ex

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

    def __init__(self, connection: Union[MySQLConnection, None] = None) -> None:
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
            fetch_num: dbs_fetch_num = dbs_fetch_num.ALL,
            fetch_type: dbs_fetch_types = dbs_fetch_types.ROW,
            params: Tuple[Union[str, int, float]] = ()
    ) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        """
        __fetch

        Args:
            query (dbs_fetch_num): -
            fetch_num (dbs_fetch_types): -
            fetch_type (Tuple[Union[str, int, float]]): -
            params (Tuple[Union[str, int, float]]): -

        Returns:
            Union[List[Dict[str, Any]], Dict[str, Any]]
        """

        log_objects(QueryLog(query, params))

        cursor = self._connection.cursor()
        cursor.execute(query, params)
        if fetch_num == dbs_fetch_num.ONE:
            res = cursor.fetchone()
        else:
            res = cursor.fetchall()

        if fetch_type == dbs_fetch_types.ROW:
            return res
        else:
            if fetch_num == dbs_fetch_num.ONE:
                res = [res]
            fields = [column[0] for column in cursor.description]
            result = [dict(line) for line in [zip(fields, row) for row in res]]
            if fetch_num == dbs_fetch_num.ONE:
                return result[0]
            return result

    def fetchAll(self, query: str, fetch_type: dbs_fetch_types = dbs_fetch_types.ROW,
                 params: Tuple[Union[str, int, float]] = ()) -> List[Dict[str, Any]]:
        """
        fetchAll

        Args:
            query (str): -
            fetch_type (dbs_fetch_types): -
            params (Tuple[Union[str, int, float]]): -

        Returns:
            List[Dict[str, Any]]
        """

        return self.__fetch(query, dbs_fetch_num.ALL, fetch_type, params)

    def fetchOne(self, query: str, fetch_type: dbs_fetch_types = dbs_fetch_types.ROW,
                 params: Tuple[Union[str, int, float]] = ()) -> Dict[str, Any]:
        """
        fetchOne

        Args:
            query (str): -
            fetch_type (dbs_fetch_types): -
            params (Tuple[Union[str, int, float]]): -

        Returns:
            Dict[str, Any]
        """
        return self.__fetch(query, dbs_fetch_num.ONE, fetch_type, params)
