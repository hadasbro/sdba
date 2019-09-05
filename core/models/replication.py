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

        master_status = self.get_master_status()
        slave_status = self.get_slave_status()

        result: Dict[str, str] = {
            "master_important_values": {},
            "master_full_log": master_status,
            "slave_important_values": {},
            "slave_full_log": slave_status,
            "conslusion": {}
        }

        key_keys_slave = (
            "Seconds_Behind_Master",
            "Master_Log_File",
            "Read_Master_Log_Pos",
            "Relay_Log_File",
            "Relay_Log_Pos",
            "Relay_Master_Log_File",
            "Last_Error",
            "Last_IO_Error",
            "Last_SQL_Error"
        )

        key_keys_master = ("File", "Position")

        for ik in key_keys_master:
            if ik in master_status:
                result["master_important_values"][ik] = master_status[ik]

        for ik in key_keys_slave:
            if ik in slave_status:
                result["slave_important_values"][ik] = slave_status[ik]

        result["conslusion"] = "conslusion"

        return result

    def get_master_status(self) -> Dict[str, str]:
        """
        get_master_status

        Returns:
            Dict[str, str]:
        """

        try:
            result = self.db.fetchOne(self.get_master_status_sql, DSBFetchTypes.ASSOC)
            return result
        except Exception as e:
            log_objects(e)

    def get_slave_status(self) -> Dict[str, Any]:
        """
        get_slave_status

        Returns:
            Dict[str, Any]: dict
        """

        try:
            result = self.db.fetchOne(self.get_slave_status_sql, DSBFetchTypes.ASSOC)
            return result
        except Exception as e:
            log_objects(e)
