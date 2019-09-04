from abc import ABC
from typing import Tuple


class OverviewSql(ABC):
    @property
    def get_active_processes_sql(self) -> str:
        """
        get_active_processes_sql

        Returns:
            str: plain SQL

        """
        return "SELECT * FROM information_schema.PROCESSLIST WHERE COMMAND != %s"

    @property
    def get_commands_general_stats_sql(self) -> str:
        """
        get_commands_general_stats_sql

        Returns:
            str: plain SQL

        """
        return "SHOW GLOBAL STATUS LIKE %s"

    @property
    def get_keys_hit_rate_sql(self) -> str:
        """
        get_keys_hit_rate_sql

        Returns:
            str: plain SQL

        """
        return "SHOW GLOBAL STATUS LIKE 'Key_%'"

    @property
    def get_qcache_hit_rate_sql(self) -> Tuple[str]:
        """
        get_qcache_hit_rate_sql

        Returns:
            str: plain SQL

        """
        return ("SHOW GLOBAL STATUS LIKE 'Qcache%'", "SHOW GLOBAL STATUS LIKE 'Com_select%'")

    @property
    def get_buffer_efficiency_sql(self) -> str:
        """
        get_buffer_efficiency_sql

        Returns:
            str: plain SQL

        """
        return "SHOW GLOBAL STATUS LIKE 'innodb_buffer_pool%';"

    @property
    def get_connections_info_sql(self) -> Tuple[str]:
        """
        get_connections_info_sql

        Returns:
            str: plain SQL

        """
        return ("SELECT @@max_connections;", "SHOW GLOBAL STATUS LIKE 'Connection_errors%';")

    @property
    def get_logs_info_sql(self) -> str:
        """
        get_logs_info_sql

        Returns:
            str: plain SQL

        """
        return "SHOW GLOBAL VARIABLES LIKE 'log%'"
