# MONITORS
from typing import Any, Dict
from core.commons import log_objects
from core.services.dbs import DBS, DSBFetchTypes
from core.interfaces.loggable import Loggable
from core.models.base_model import BaseModel
from core.models.sql_traits.replication_sql import ReplicationSql


class MysqlReplication(BaseModel, ReplicationSql, Loggable):

    def __init__(self, db: DBS) -> None:
        """
        __init__

        Args:
            db (DBS):
        """

        super().__init__()
        self.db = db

    def get_as_string(self) -> str:
        """
        get_as_string

        Returns:

        """
        return "Replication"

    def get_replication_log(self) -> Dict[str, Any]:
        """
        get_replication_log

        Returns:
            Dict[str, Any]: dict
        """

        main_status = self.get_main_status()
        subordinate_status = self.get_subordinate_status()

        if main_status is None or subordinate_status is None:
            return {}

        result: Dict[str, str] = {
            "main_important_values": {},
            "main_full_log": main_status,
            "subordinate_important_values": {},
            "subordinate_full_log": subordinate_status,
            "conslusion": {}
        }

        key_keys_subordinate = (
            "Seconds_Behind_Main",
            "Main_Log_File",
            "Read_Main_Log_Pos",
            "Relay_Log_File",
            "Relay_Log_Pos",
            "Relay_Main_Log_File",
            "Last_Error",
            "Last_IO_Error",
            "Last_SQL_Error"
        )

        key_keys_main = ("File", "Position")

        for ik in key_keys_main:
            if ik in main_status:
                result["main_important_values"][ik] = main_status[ik]

        for ik in key_keys_subordinate:
            if ik in subordinate_status:
                result["subordinate_important_values"][ik] = subordinate_status[ik]

        result["conslusion"] = "conslusion"

        return result

    def get_main_status(self) -> Dict[str, str]:
        """
        get_main_status

        Returns:
            Dict[str, str]:
        """

        try:
            result = self.db.fetchOne(self.get_main_status_sql, DSBFetchTypes.ASSOC)
            return result
        except Exception as e:
            log_objects(e)
            raise e

    def get_subordinate_status(self) -> Dict[str, Any]:
        """
        get_subordinate_status

        Returns:
            Dict[str, Any]: dict
        """

        try:
            result = self.db.fetchOne(self.get_subordinate_status_sql, DSBFetchTypes.ASSOC)
            return result
        except Exception as e:
            log_objects(e)
            raise e
