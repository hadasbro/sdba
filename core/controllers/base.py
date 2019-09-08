from abc import ABC
from typing import Any, Dict, Optional

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

    def __init__(self, dbs: Optional[DBS] = None) -> None:
        """
        __init__

        Args:
            dbs(Optional[DBS]): db connection instance

        Raises:
            PayloadException: exception with payload to return from API

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

        if dbs is None:
            try:

                ldb: DBSCredentials = self.local_db.get_latest_db()
                self.dbs = DBS(ldb)

                self.response['database'] = {
                    'name': ldb.get_name(),
                    'id': ldb.get_id()
                }

            except DbNotFoundException:
                self.response['status'] = self.STATUS_NO_DB
                self.response['message'] = Translator().translate("db_choose")
                raise PayloadException("", self.response)

            except Exception as ex:
                self.response['status'] = self.STATUS_ERROR
                self.response['message'] = Translator().translate(str(ex))
                raise PayloadException("", self.response)

        else:
            self.dbs = dbs
