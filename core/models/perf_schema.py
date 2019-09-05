# MONITORS
from typing import Any, Dict, List

from core.services.dbs import DSBFetchTypes, DBS
from core.interfaces.loggable import Loggable
from core.models.base_model import BaseModel
from core.models.sql_traits.perf_schema_sql import PerfSchemaSql


class PerformanceSchema(BaseModel, PerfSchemaSql, Loggable):
    COM_COMMAND = "Com_"

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
            str: str
        """
        return "Performance schema"

    def get_top_long_queries(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        get_top_long_queries

        Args:
            limit (int):

        Returns:
            List[Dict[str, Any]]: list

        """
        result = self.db.fetchAll(self.get_top_long_queries_sql, DSBFetchTypes.ASSOC, (limit,))

        return result

    def get_top_long_updates(self, limit: int = 10, days_back: int = 3) -> List[Dict[str, Any]]:
        """
        get_top_long_updates

        Args:
            limit (int):
            days_back (int):

        Returns:
            List[Dict[str, Any]]: list

        """
        result = self.db.fetchAll(self.get_top_long_updates_sql, DSBFetchTypes.ASSOC, (days_back, days_back, limit))

        return result

    def get_index_stats_for_top_tables(self, limit_tables: int = 3) -> List[Dict[str, Any]]:
        """
        get_index_stats_for_top_tables

        Args:
            limit_tables (int):

        Returns:
            List[Dict[str, Any]]: list

        """
        all = self.db.fetchAll(self.get_index_stats_for_top_tables_sql, DSBFetchTypes.ROW)
        res: Dict[str, Any] = {}
        for i in all:
            k = i[0] + '.' + i[1]

            if k not in res:
                res[k] = {
                    'no_index': 0,
                    'index': 0
                }

            if i[2] is None:
                res[k]['no_index'] = i[3]
            else:
                res[k]['index'] = res[k]['index'] + i[3]

        return res
