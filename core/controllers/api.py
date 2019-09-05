from typing import Any, Dict, List, Union

from core.commons.tiny_dbs import TinyDBS
from core.commons.utils import Utils
from core.models.info_schema import InfoSchema
from core.models.monitors import MonitorDedlock, Monitors, MonitorBackground, MonitorSemaphores, \
    MonitorBufferAndMemory, MonitorRowOperations, MonitorLatestTransactions, MonitorLatestForeign
from core.models.overview import Overview
from core.models.perf_schema import PerformanceSchema
from core.models.replication import MysqlReplication
from core.models.variables import MySQLVariables


class ApiController:

    STATUS_OK: int = 1
    STATUS_NO_DB: int = 2
    STATUS_ERROR: int = 3

    def __init__(self) -> None:
        """
        __init__

        Returns:
            None
        """
        tiny_db = TinyDBS()
        ldb = tiny_db.get_latest_db()

        print(ldb)
        db = None
        self.dbx = db


    def __get_response(self, payload: Dict[str, str]) -> Dict[str, str]:
        """
        __get_response

        Args:
            payload (Dict[str, str]):

        Returns:
            Dict[str, str]
        """
        response: Dict[str, Any] = {
            'status': self.STATUS_ERROR,
            'message': "",
            'database': {
                'name': '',
                'id': 0
            },
            'logs': [],
            'payload': payload
        }

        return Utils.dict_to_json(response)


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

        return self.__get_response(dbStatus.get_partial_monitors_result())

    def get_variables(self) -> str:
        """
        get_variables

        Returns:
            str: result as json
        """
        mv = MySQLVariables(self.dbx)
        return self.__get_response(mv.get_all_variables())

    def get_replication_data(self) -> str:
        """
        get_replication_data

        Returns:
            str: result as json
        """
        mv = MysqlReplication(self.dbx)
        return self.__get_response(mv.get_replication_log())

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

        return self.__get_response(res)

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

        return self.__get_response(res)

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

        return self.__get_response(res)
