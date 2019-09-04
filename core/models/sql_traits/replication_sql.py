from abc import ABC


class ReplicationSql(ABC):

    @property
    def get_master_status_sql(self) -> str:
        """
        get_master_status_sql

        Returns:
            str: plain SQL
        """
        return "SHOW MASTER STATUS"

    @property
    def get_slave_status_sql(self) -> str:
        """
        get_slave_status_sql

        Returns:
            str: plain SQL
        """
        # return "SHOW SLAVE STATUS"
        return "SHOW MASTER STATUS"
