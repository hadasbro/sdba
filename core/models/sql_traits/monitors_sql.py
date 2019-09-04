from abc import ABC


class MonitorsSql(ABC):
    @property
    def _get_innodb_status_sql(self) -> str:
        """
        _get_innodb_status_sql

        Returns:
            str: plain SQL
        """
        return "SHOW ENGINE INNODB STATUS"
