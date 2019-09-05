from pathlib import Path
from typing import Any, Union

from tinydb import TinyDB, Query

from core.commons import log_objects
from core.commons.dbs import db_credentials
from core.commons.hasher import Hasher
from core.interfaces.singleton import Singleton


class TinyDBS(metaclass=Singleton):

    __metaclass__ = Singleton

    _DDATA_PATH: str = 'dbdata'
    _DATA_FILE: str = 'db.json'

    tdb_db = None
    tdb_table_databases = None

    def __init__(self) -> None:
        """
        __init__

        """

        relative: Union[Path, Any] = Path(__file__)

        absolute = relative.resolve().parents[2] \
            .joinpath(self._DDATA_PATH) \
            .joinpath(self._DATA_FILE)

        try:
            self.tdb_db = TinyDB(absolute)
            self.tdb_tbl_databases = self.tdb_db.table('databases')
            self.tdb_tbl_latest_dbs = self.tdb_db.table('tdb_tbl_latest_dbs')


            # adding test DB
            # test = db_instance(1, "localhost", "root", "", 3306)
            # self.add_new_db(test)
            # self.set_latest_db(test)

        except Exception as e:
            log_objects(e)
            raise e


    def add_new_db(self, db: db_credentials) -> None:
        """
        add_new_db

        Args:
            db (db_credentials):

        Returns:
            None
        """
        try:
            db_cred = db.get_as_dict()
            hashed_data = Hasher.encode_data(db_cred)
            '''
                endode credentials before save to tiny DB
            '''
            data = {
                'id': db_cred['id'],
                'hashed_data': hashed_data
            }

            self.tdb_tbl_databases.insert(data)

        except Exception as e:
            log_objects(e)
            raise e

    def get_db_by_id(self, ldb_id: int) -> Union[db_credentials, None]:
        """
        get_db_by_id

        Args:
            ldb_id (int):

        Returns:
            Union[db_instance, None]: db
        """
        dbi: db_credentials = self.tdb_tbl_databases.search(Query().id == ldb_id)

        if not dbi:
            return None

        db_data = dbi[0]

        db_id: int = db_data['id']
        db_hashed: str = db_data['hashed_data']

        encoded = Hasher.decode_data(db_hashed)

        return db_credentials.from_dict(encoded)

    def get_latest_db(self) -> Union[db_credentials, None]:
        """
        get_latest_db

        Returns:
            Union[db_instance, None]: db
        """
        db_id: int = self.tdb_tbl_latest_dbs.search(Query().last_db_id == 1)

        if not db_id:
            return None

        ldb_id = db_id[0]['id']

        return self.get_db_by_id(ldb_id)

    def set_latest_db(self, db: db_credentials) -> None:
        """
        set_latest_db

        Args:
            db (db_credentials): db

        Returns:
            None
        """
        try:
            Q = Query()
            check = not not self.tdb_tbl_latest_dbs.search(Q.last_db_id == 1)
            if not check:
                # add record
                self.tdb_tbl_latest_dbs.insert({
                    'last_db_id': 1,
                    'id': db.get_id()
                })
            else:
                # only update
                self.tdb_tbl_latest_dbs.update({'id': db.get_id()}, Q.last_db_id == 1)
        except Exception as e:
            log_objects(e)
            print(e)
