# MONITORS
from functools import reduce
from typing import Any, Dict, Union, List

from core.services.dbs import DBS, DSBFetchTypes
from core.interfaces.loggable import Loggable
from core.models.base_model import BaseModel
from core.models.sql_traits.overview_sql import OverviewSql


class Overview(BaseModel, OverviewSql, Loggable):
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
        return self.__class__.__name__

    def get_active_processes(self) -> List[Dict[str, Any]]:
        """
        get_active_processes

        Returns:
            List[Dict[str, Any]]: list

        """
        result = self.db.fetchAll(self.get_active_processes_sql, DSBFetchTypes.ASSOC, ("Sleep",))
        return result

    def get_commands_general_stats(self) -> Dict[str, float]:
        """
        get_commands_general_stats

        Returns:
            Dict[str, float]: dict or list

        """
        result = self.db.fetchAll(self.get_commands_general_stats_sql, DSBFetchTypes.ROW, ("Com\_%",))
        all_res = sorted(result, key=lambda k: int(k[1]), reverse=True)
        sum_all = reduce((lambda x, y: int(x) + int(y)), map(lambda el: el[1], all_res))
        res_top3 = all_res[0:3]
        result: Dict[str, float] = dict(
            list(map(lambda el: (el[0].replace(self.COM_COMMAND, ""), round(int(el[1]) / sum_all, 2)), res_top3)))

        return result

    def get_keys_hit_rate(self) -> Dict[str, int]:
        """
        get_keys_hit_rate

        Returns:
            Dict[str, int]: dict
        """
        result: Dict[str, int] = {
            "read_effic": 0,
            "write_effic": 0
        }
        res = self.db.fetchAll(self.get_keys_hit_rate_sql, DSBFetchTypes.ROW)
        all = dict(map(lambda el: (el[0], int(el[1])), res))

        result["read_effic"] = 0 if all["Key_reads"] == 0 else \
            int(round(1 - all["Key_reads"] / all["Key_read_requests"], 2) * 100)
        result["write_effic"] = 0 if all["Key_writes"] == 0 else \
            int(round(1 - all["Key_writes"] / all["Key_write_requests"], 2) * 100)

        return result

    def get_qcache_hit_rate(self) -> Dict[str, int]:
        """
        get_qcache_hit_rate

        Returns:

        """
        result: Dict[str, int] = {
            "qcache_select_hit_rate": 0,
        }
        res = self.db.fetchAll(self.get_qcache_hit_rate_sql[0], DSBFetchTypes.ROW)
        all = dict(map(lambda el: (el[0], int(el[1])), res))
        res = self.db.fetchAll(self.get_qcache_hit_rate_sql[1], DSBFetchTypes.ROW)
        all_com = dict(map(lambda el: (el[0], int(el[1])), res))
        result["qcache_select_hit_rate"] = int(
            round((all["Qcache_hits"] / (all["Qcache_hits"] + all_com["Com_select"])), 2) * 100
        )

        return result

    def get_buffer_efficiency(self) -> Dict[str, Union[float, int]]:
        """
        get_buffer_efficiency

        Returns:
            Dict[str, Union[float, int]]: dict or list
        """
        result: Dict[str, int] = {
            "buffer_efficiency": 0,
            "utilization": 0
        }
        all = dict(self.db.fetchAll(self.get_buffer_efficiency_sql, DSBFetchTypes.ROW))
        result["buffer_efficiency"] = int(
            (1 - int(all["Innodb_buffer_pool_reads"])
             / int(all["Innodb_buffer_pool_read_requests"])) * 100
        )

        result["utilization"] = (int(all["Innodb_buffer_pool_pages_total"]) - int(all["Innodb_buffer_pool_pages_free"])) \
                                / int(all["Innodb_buffer_pool_pages_total"])

        return result

    def get_connections_info(self) -> Dict[str, Any]:
        """
        get_connections_info

        Returns:
            Dict[str, Any]: dict
        """
        result: Dict[str, int] = {
            "max_connections": 0,
            "connection_errs": Dict[str, int]
        }
        con_result = self.db.fetchOne(self.get_connections_info_sql[0], DSBFetchTypes.ROW)
        all_result = self.db.fetchAll(self.get_connections_info_sql[1], DSBFetchTypes.ROW)
        result["max_connections"] = con_result[0]
        result["connection_errs"] = dict(all_result)

        return result

    def get_logs_info(self) -> Dict[str, Any]:
        """
        get_logs_info

        Returns:
            Dict[str, Any]: dict
        """
        con_result = self.db.fetchAll(self.get_logs_info_sql, DSBFetchTypes.ROW)
        result: Dict[str, int] = dict(con_result)

        return result
