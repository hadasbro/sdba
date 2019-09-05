# MONITORS
from typing import Any, Dict, Tuple

from core.commons import log_objects
from core.services.dbs import DBS
from core.commons.htmlizer import HtmlIzer
from core.interfaces.loggable import Loggable
from core.models.base_model import BaseModel
from core.models.sql_traits.variables_sql import VariablesSql


class MySQLVariables(BaseModel, VariablesSql, Loggable):

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
        return "Variables and Settings"

    def get_global_variables(self) -> Dict[str, Any]:
        """
        get_global_variables

        Returns:
            Dict[str, Any]: dict

        """
        records = self.db.fetchAll(self.get_global_variables_sql)
        variables: Dict[str, Any] = dict(records)

        return variables

    def get_session_variables(self) -> Dict[str, Any]:
        """
        get_session_variables

        Returns:
            Dict[str, Any]: dict

        """
        records = self.db.fetchAll(self.get_session_variables_sql)
        variables: Dict[str, Any] = dict(records)

        return variables

    def get_all_variables(self) -> Dict[str, Tuple[Any, ...]]:
        """
        get_all_variables

        Returns:
            Dict[str, Tuple[Any, ...]]: dict

        """
        html: HtmlIzer = HtmlIzer()

        try:

            global_v = self.get_global_variables()
            session_v = self.get_session_variables()

            keys = list(set().union(global_v, session_v))

            _res: Dict[str, Any] = {}

            for ki in keys:
                l, g = "-", "-"
                if ki in session_v:
                    l = html.wrap_types(session_v[ki])
                if ki in global_v:
                    g = html.wrap_types(global_v[ki])

                _res[ki] = (l, g)

            return _res

        except Exception as e:
            return {}
            log_objects(e)
