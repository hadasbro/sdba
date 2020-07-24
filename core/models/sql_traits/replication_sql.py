from abc import ABC


class ReplicationSql(ABC):

    @property
    def get_main_status_sql(self) -> str:
        """
        get_main_status_sql

        Returns:
            str: plain SQL
        """
        return "SHOW MASTER STATUS"

    @property
    def get_subordinate_status_sql(self) -> str:
        """
        get_subordinate_status_sql

        Returns:
            str: plain SQL
        """
        # return "SHOW SLAVE STATUS"
        return "SHOW MASTER STATUS"
