from functools import reduce
from pathlib import Path
from typing import Any, Union, List, Dict

from tinydb import TinyDB, Query

from core.commons import log_objects
from core.objects.dbs_credentials import DBSCredentials
from core.services.hasher import Hasher
from core.exceptions.db_not_found_exception import DbNotFoundException
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

        except Exception as e:
            log_objects(e)
            raise e


    def add_new_db(self, db: DBSCredentials) -> None:
        """
        add_new_db

        Args:
            db (DBSCredentials):

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

    def get_last_db_id(self) -> int:
        """
        get_last_db_id

        Returns:
            int: max id
        """
        adbs: List[DBSCredentials] = self.get_all_databases()
        if not adbs:
            return 0

        return reduce(lambda a, b: a if a > b else b, list(map(lambda el: int(el.get_id()), adbs)))

    def get_all_databases(self) -> List[DBSCredentials]:
        """
        get_all_databases

        Returns:
            List[DBSCredentials]: cred list
        """
        def map_to_dbcred(db_data):
            db_hashed: str = db_data['hashed_data']
            encoded = Hasher.decode_data(db_hashed)
            return DBSCredentials.from_dict(encoded)

        allDbs: List[DBSCredentials] = []

        dbi: List[Dict[str, str]] = self.tdb_tbl_databases.all()

        allDbs = list(map(lambda el: map_to_dbcred(el), dbi))

        return allDbs

    def get_db_by_id(self, ldb_id: int) -> DBSCredentials:
        """
        get_db_by_id

        Args:
            ldb_id (int):

        Returns:
            DBSCredentials: db

        Raises:
            DbNotFoundException: exc
        """
        dbi: DBSCredentials = self.tdb_tbl_databases.search(Query().id == ldb_id)

        if not dbi:
            raise DbNotFoundException()

        db_data = dbi[0]

        # db_id: int = db_data['id']
        db_hashed: str = db_data['hashed_data']

        encoded = Hasher.decode_data(db_hashed)

        return DBSCredentials.from_dict(encoded)

    def get_latest_db(self) -> DBSCredentials:
        """
        get_latest_db

        Returns:
            DBSCredentials: db

        Raises:
            DbNotFoundException: exc

        """

        db_id: int = self.tdb_tbl_latest_dbs.search(Query().last_db_id == 1)

        if not db_id:
            raise DbNotFoundException()

        ldb_id = db_id[0]['id']

        return self.get_db_by_id(ldb_id)

    def set_latest_db(self, db: DBSCredentials) -> None:
        """
        set_latest_db

        Args:
            db (DBSCredentials): db

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
