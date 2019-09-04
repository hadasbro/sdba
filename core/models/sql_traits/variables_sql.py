from abc import ABC


class VariablesSql(ABC):

    @property
    def get_global_variables_sql(self) -> str:
        """
        get_global_variables_sql

        Returns:
            str: plain SQL
        """
        return "SHOW GLOBAL VARIABLES"

    @property
    def get_session_variables_sql(self) -> str:
        """
        get_session_variables_sql

        Returns:
            str: plain SQL
        """
        return "SHOW SESSION VARIABLES"
