from typing import Any, Dict, List, Union

from core.commons.dbs import DBS
from core.commons.utils import Utils
from core.models.info_schema import InfoSchema
from core.models.monitors import MonitorDedlock, Monitors, MonitorBackground, MonitorSemaphores, \
    MonitorBufferAndMemory, MonitorRowOperations, MonitorLatestTransactions, MonitorLatestForeign
from core.models.overview import Overview
from core.models.perf_schema import PerformanceSchema
from core.models.replication import MysqlReplication
from core.models.variables import MySQLVariables


class ApiController:

    def __init__(self, db: DBS) -> None:
        """
        __init__

        Args:
            db (DBS):

        Returns:
            None
        """
        self.db = db.connection
        self.dbx = db

    def get_monitors(self) -> str:
        """
        get_monitors

        Returns:
            str: result as json
        """
        dbStatus: Monitors = Monitors(
            self.dbx,
            MonitorBackground(),
            MonitorSemaphores(),
            MonitorBufferAndMemory(),
            MonitorRowOperations(),
            MonitorLatestTransactions(),
            MonitorLatestForeign(),
            MonitorDedlock()
        )

        return Utils.dict_to_json(dbStatus.get_partial_monitors_result())

    def get_variables(self) -> str:
        """
        get_variables

        Returns:
            str: result as json
        """
        mv = MySQLVariables(self.dbx)
        return Utils.dict_to_json(mv.get_all_variables())

    def get_replication_data(self) -> str:
        """
        get_replication_data

        Returns:
            str: result as json
        """
        mv = MysqlReplication(self.dbx)
        return Utils.dict_to_json(mv.get_replication_log())

    def get_overview(self) -> str:
        """
        get_overview

        Returns:
            str: result as json
        """
        mv = Overview(self.dbx)
        res: Dict[str, Union[List[Dict[str, Any]], Dict[str, Any]]] = {
            "active_processes": mv.get_active_processes(),
            "commands_general_stats": mv.get_commands_general_stats(),
            "keys_hit_rate": mv.get_keys_hit_rate(),
            "cache_hit_rate": mv.get_qcache_hit_rate(),
            "buffer_efficiency": mv.get_buffer_efficiency(),
            "connections_info": mv.get_connections_info(),
            "get_logs_info": mv.get_logs_info()
        }

        print(res)
        return Utils.dict_to_json(res)

    def get_performance_schema(self) -> str:
        """
        get_performance_schema

        Returns:
            str: result as json
        """
        pes = PerformanceSchema(self.dbx)
        res: Dict[str, List[Dict[str, Any]]] = {
            "top_long_queries": pes.get_top_long_queries(),
            "top_long_updates": pes.get_top_long_updates(),
            "index_stats_for_top_tables": pes.get_index_stats_for_top_tables()
        }

        return Utils.dict_to_json(res)

    def get_info_schema(self) -> str:
        """
        get_info_schema

        Returns:
            str: result as json
        """
        ise = InfoSchema(self.dbx)

        big_tables = ise.get_biggest_tables_chached()
        seze_per_engine = ise.get_size_per_engine_cached()
        tables_without_pk = ise.get_tables_without_pk_cached()

        res: Dict[str, List[Dict[str, Any]]] = {
            "get_biggest_tables_chached": big_tables,
            "get_size_per_engine_cached": seze_per_engine,
            "get_tables_without_pk_cached": tables_without_pk
        }

        return Utils.dict_to_json(res)
