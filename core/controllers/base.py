from abc import ABC
from typing import Any, Dict, Optional

from core.commons import log_objects
from core.exceptions.db_not_found_exception import DbNotFoundException
from core.exceptions.payload_exception import PayloadException
from core.objects.dbs_credentials import DBSCredentials
from core.services.dbs import DBS
from core.services.local_db import TinyDBS
from core.services.translator import Translator


class BaseController(ABC):

    STATUS_OK: int = 1
    STATUS_NO_DB: int = 2
    STATUS_ERROR: int = 3

    def __init__(self) -> None:
        """
        __init__

        """
        self.local_db = TinyDBS()

        self.response: Dict[str, Any] = {
            'status': self.STATUS_OK,
            'message': "",
            'database': {
                'name': '',
                'id': 0
            },
            'logs': [],
            'payload': {}
        }

    def _get_response(self,
                      payload: Optional[Dict[str, str]] = None,
                      msg: Optional[str] = None,
                      status = None
                      ) -> Dict[str, Any]:
        """
        _get_response

        Args:
            payload (Dict[str, str]):

        Returns:
            Dict[str, str]
        """

        self.response['payload'] = payload if payload is not None else {}

        if msg is not None:
            self.response['message'] = msg

        if status is not None:
            self.response['status'] = status

        return self.response

    def load_latest_db(self, dbs: Optional[DBS] = None) -> None:
        """
        load_latest_db

        Args:
            dbs (Optional[DBS]): db

        Returns:
            None
        """
        if dbs is None:
            try:

                ldb: DBSCredentials = self.local_db.get_latest_db()
                self.dbs = DBS(ldb)

                self.response['database'] = {
                    'name': ldb.get_name(),
                    'id': ldb.get_id()
                }

            except DbNotFoundException as ex:
                log_objects(ex)
                self.response['status'] = self.STATUS_NO_DB
                self.response['message'] = Translator().translate("db_choose")
                raise PayloadException(self.response['message'], self.response)

            except Exception as ex:
                log_objects(ex)
                self.response['status'] = self.STATUS_ERROR
                self.response['message'] = Translator().translate(str(ex))
                raise PayloadException(self.response['message'], self.response)

        else:
            self.dbs = dbs