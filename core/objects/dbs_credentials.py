import json
from enum import Enum
from typing import Dict, Any, Union
from core.commons.utils import Utils


class DBSCredentials:
    class TYPE(Enum):
        MYSQL = 1

    __id = 0
    __connection = 0

    def __init__(self,
                 id: int,
                 name: str,
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
            name (name):  -
            host (str):  -
            user (str):  -
            password (str):  -
            port (int):  -
            type (TYPE):  -
            ssl (bool):  -
        """
        self.__id: int = id
        self.__name: str = name
        self.__host: str = host
        self.__type: DBSCredentials.TYPE = type
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

    def get_name(self) -> str:
        """
        get_name

        Returns:
            str
        """
        return self.__name

    def get_host(self) -> str:
        """
        get_host

        Returns:
            str
        """
        return self.__host

    def get_type(self) -> 'DBSCredentials.TYPE':
        """
        get_type

        Returns:
            DBSCredentials.TYPE
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

    def __repr__(self) -> str:
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
        return Utils.dict_to_json(self.__dict__)

    def get_as_dict(self) -> Dict[str, Any]:
        """
        get_as_dict

        Returns:
            Dict[str, Any]: dict
        """
        return {
            'id': self.get_id(),
            'name': self.get_name(),
            'host': self.get_host(),
            'user': self.get_user(),
            'password': self.get_password(),
            'port': self.get_port(),
            'type': self.get_type(),
            'ssl': self.get_ssl()
        }

    @staticmethod
    def from_dict(dval: Dict[str, Union[str, int, TYPE, bool]]) -> 'DBSCredentials':
        """
        from_dict

        Args:
            dval:

        Returns:
            DBSCredentials
        """
        try:
            return DBSCredentials(
                dval['id'],
                dval['name'],
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
    def from_json(json_str: str) -> 'DBSCredentials':
        """
        from_json

        Args:
            json_str ():

        Returns:

        """
        ldata = json.loads(json_str)
        try:
            return DBSCredentials.from_dict(ldata)
        except AttributeError as ex:
            raise ex
