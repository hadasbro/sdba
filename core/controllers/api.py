from typing import Any, Dict, List, Union, Optional
from mysql.connector import errors
from core.controllers.base import BaseController
from core.models.info_schema import InfoSchema
from core.models.monitors import MonitorDedlock, Monitors, MonitorBackground, MonitorSemaphores, \
    MonitorBufferAndMemory, MonitorRowOperations, MonitorLatestTransactions, MonitorLatestForeign
from core.models.overview import Overview
from core.models.perf_schema import PerformanceSchema
from core.models.replication import MysqlReplication
from core.models.variables import MySQLVariables
from core.services.dbs import DBS
from core.services.local_db import TinyDBS
from core.services.translator import Translator


class ApiController(BaseController):
    STATUS_OK: int = 1
    STATUS_NO_DB: int = 2
    STATUS_ERROR: int = 3

    local_db: TinyDBS = None
    dbs: DBS = None
    response: Dict[str, Any] = {}

    def __init__(self, dbs: Optional[DBS] = None) -> None:
        """
        __init__

        Args:
            dbs (Optional[DBS]): db
        """
        super().__init__()
        self.load_latest_db(dbs)

    def get_monitors(self) -> Dict[str, Any]:
        """
        get_monitors

        Returns:
            str: result as json
        """

        try:

            dbStatus: Monitors = Monitors(
                self.dbs,
                MonitorBackground(),
                MonitorSemaphores(),
                MonitorBufferAndMemory(),
                MonitorRowOperations(),
                MonitorLatestTransactions(),
                MonitorLatestForeign(),
                MonitorDedlock()
            )

            return self._get_response(dbStatus.get_partial_monitors_result())

        except errors.ProgrammingError as per:
            return self._get_response(
                None,
                Translator().translate_by_db_code(per),
                self.STATUS_ERROR
            )


    def get_variables(self) -> Dict[str, Any]:
        """
        get_variables

        Returns:
            str: result as json
        """

        try:
            mv = MySQLVariables(self.dbs)
            return self._get_response(mv.get_all_variables())
        except errors.ProgrammingError as per:
            return self._get_response(
                None,
                Translator().translate_by_db_code(per),
                self.STATUS_ERROR
            )

    def get_replication_data(self) -> Dict[str, Any]:
        """
        get_replication_data

        Returns:
            str: result as json
        """

        try:
            mv = MysqlReplication(self.dbs)
            return self._get_response(mv.get_replication_log())
        except errors.ProgrammingError as per:
            return self._get_response(
                None,
                Translator().translate_by_db_code(per),
                self.STATUS_ERROR
            )

    def get_overview(self) -> Dict[str, Any]:
        """
        get_overview

        Returns:
            str: result as json
        """

        try:
            mv = Overview(self.dbs)
            res: Dict[str, Union[List[Dict[str, Any]], Dict[str, Any]]] = {
                "active_processes": mv.get_active_processes(),
                "commands_general_stats": mv.get_commands_general_stats(),
                "keys_hit_rate": mv.get_keys_hit_rate(),
                "cache_hit_rate": mv.get_qcache_hit_rate(),
                "buffer_efficiency": mv.get_buffer_efficiency(),
                "connections_info": mv.get_connections_info(),
                "get_logs_info": mv.get_logs_info()
            }

            return self._get_response(res)

        except errors.ProgrammingError as per:
            return self._get_response(
                None,
                Translator().translate_by_db_code(per),
                self.STATUS_ERROR
            )


    def get_performance_schema(self) -> Dict[str, Any]:
        """
        get_performance_schema

        Returns:
            str: result as json
        """

        try:
            pes = PerformanceSchema(self.dbs)
            res: Dict[str, List[Dict[str, Any]]] = {
                "top_long_queries": pes.get_top_long_queries(),
                "top_long_updates": pes.get_top_long_updates(),
                "index_stats_for_top_tables": pes.get_index_stats_for_top_tables()
            }

            return self._get_response(res)

        except errors.ProgrammingError as per:
            return self._get_response(
                None,
                Translator().translate_by_db_code(per),
                self.STATUS_ERROR
            )

    def get_info_schema(self) -> Dict[str, Any]:
        """
        get_info_schema

        Returns:
            str: result as json
        """
        try:
            ise = InfoSchema(self.dbs)

            big_tables = ise.get_biggest_tables_chached()
            seze_per_engine = ise.get_size_per_engine_cached()
            tables_without_pk = ise.get_tables_without_pk_cached()

            res: Dict[str, List[Dict[str, Any]]] = {
                "get_biggest_tables_chached": big_tables,
                "get_size_per_engine_cached": seze_per_engine,
                "get_tables_without_pk_cached": tables_without_pk
            }

            return self._get_response(res)

        except errors.ProgrammingError as per:
            return self._get_response(
                None,
                Translator().translate_by_db_code(per),
                self.STATUS_ERROR
            )

    def selest_from_test_db(self) -> Dict[str, Any]:
        """
        selest_from_test_db

        Returns:
            Dict[str, Any]
        """
        try:
            mv = Overview(self.dbs)
            res = mv.do_test_in_test_db()

            return self._get_response(res)

        except errors.ProgrammingError as per:
            return self._get_response(
                None,
                Translator().translate_by_db_code(per),
                self.STATUS_ERROR
            )
