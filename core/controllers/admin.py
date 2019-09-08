from typing import Optional, List

from core.commons import log_objects
from core.controllers.base import BaseController
from core.objects.dbs_credentials import DBSCredentials
from core.services.dbs import DBS
from core.services.local_db import TinyDBS


class AdminController(BaseController):

    def __init__(self, dbs: Optional[DBS] = None) -> None:
        """
        __init__

        Args:
            dbs (Optional[DBS]): db
        """
        super().__init__(dbs)
        pass

    def get_databases(self) -> List[DBSCredentials]:
        """
        get_databases

        Returns:
            List[DBSCredentials]: cred
        """
        return self.local_db.get_all_databases()


    @staticmethod
    def add_new_database(
            name: str,
            host: str,
            user: str,
            password: str,
            port: int = 3306,
            type: DBSCredentials.TYPE = DBSCredentials.TYPE.MYSQL,
            ssl: bool = False
    ) -> bool:
        """
        add_new_database

        Args:
            name (str):
            host (str):
            user (str):
            password (str):
            port (int):
            type (DBSCredentials.TYPE):
            ssl (bool):

        Returns:
            bool
        """
        local_db: TinyDBS = TinyDBS()

        last_id: int = local_db.get_last_db_id() + 1
        new_db_cred: DBSCredentials = DBSCredentials(last_id, name, host, user, password, port, type, ssl)

        try:
            local_db.add_new_db(new_db_cred)
            if last_id == 1:
                local_db.set_latest_db(new_db_cred)
            return True
        except Exception as e:
            log_objects(e)
            return False