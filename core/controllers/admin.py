from typing import Optional, List, Dict, Any

from core.commons import log_objects
from core.commons.utils import Utils
from core.controllers.base import BaseController
from core.exceptions.payload_exception import PayloadException
from core.objects.dbs_credentials import DBSCredentials
from core.services.dbs import DBS
from core.services.local_db import TinyDBS
from core.services.translator import Translator


class AdminController(BaseController):

    def __init__(self, dbs: Optional[DBS] = None) -> None:
        """
        __init__

        Args:
            dbs (Optional[DBS]): db
        """
        super().__init__()

    def get_databases(self) -> Dict[str, Any]:
        """
        get_databases

        Returns:
            List[DBSCredentials]: cred
        """

        dbs: List[DBSCredentials] = self.local_db.get_all_databases()

        if not not dbs:
            try:
                self.load_latest_db()
            except Exception:
                pass

        return self._get_response(dbs)

    def add_new_database(
            self,
            name: str,
            host: str,
            user: str,
            password: str,
            port: int = 3306,
            type: DBSCredentials.TYPE = DBSCredentials.TYPE.MYSQL,
            ssl: bool = False
    ) -> Dict[str, Any]:
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

        if Utils.strempty(name) or Utils.strempty(host) or Utils.strempty(user):
            self.response['status'] = self.STATUS_ERROR
            self.response['message'] = Translator().translate("inforrect_db_data")
            raise PayloadException(self.response['message'], self.response)

        last_id: int = local_db.get_last_db_id() + 1
        new_db_cred: DBSCredentials = DBSCredentials(last_id, name, host, user, password, port, type, ssl)

        try:
            local_db.add_new_db(new_db_cred)
            if last_id == 1:
                local_db.set_latest_db(new_db_cred)
                self.response['database'] = {
                    'name': new_db_cred.get_name(),
                    'id': new_db_cred.get_id()
                }
            else:
                self.load_latest_db()

            self.response['message'] = Translator().translate("success")
            return self._get_response()

        except Exception as e:
            log_objects(e)
            return self._get_response()
