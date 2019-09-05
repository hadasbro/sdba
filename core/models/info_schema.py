# MONITORS
from typing import Any, Dict, List

from core.services.dbs import DBS, DSBFetchTypes
from core.commons.memoizer import Memoize
from core.interfaces.loggable import Loggable
from core.models.base_model import BaseModel
from core.models.sql_traits.info_schema_sql import InfoSchemaSql


class InfoSchema(BaseModel, InfoSchemaSql, Loggable):

    def __init__(self, db: DBS) -> None:
        """
        __init__

        Args:
            db (DBS):

        Returns:
            None
        """
        super().__init__()
        self.db = db

    def get_as_string(self) -> str:
        """
        get_as_string

        Returns:
            str
        """
        return "Information Schema"

    @staticmethod
    def info_schema_cached():
        return True

    @Memoize
    def get_biggest_tables_chached(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        get_biggest_tables_chached

        Args:
            limit (int):

        Returns:
            List[Dict[str, Any]]: list
        """
        return self.get_biggest_tables(limit)

    @Memoize
    def get_size_per_engine_cached(self) -> List[Dict[str, Any]]:
        """
        get_size_per_engine_cached

        Returns:
            List[Dict[str, Any]]: list
        """
        return self.get_size_per_engine()

    @Memoize
    def get_tables_without_pk_cached(self) -> List[Dict[str, Any]]:
        """
        get_tables_without_pk_cached

        Returns:
            List[Dict[str, Any]]: list
        """
        return self.get_tables_without_pk()

    def get_biggest_tables(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        get_biggest_tables

        Args:
            limit (int):

        Returns:
            List[Dict[str, Any]]: list
        """
        result = self.db.fetchAll(self.get_biggest_tables_sql, DSBFetchTypes.ASSOC, (limit,))

        return result

    def get_size_per_engine(self) -> List[Dict[str, Any]]:
        """
        get_size_per_engine

        Returns:
            List[Dict[str, Any]]: list
        """
        result = self.db.fetchAll(self.get_size_per_engine_sql, DSBFetchTypes.ASSOC, (5,))
        return result

    def get_tables_without_pk(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        get_tables_without_pk

        Args:
            limit (int):

        Returns:
            List[Dict[str, Any]]: list
        """
        result = self.db.fetchAll(self.get_tables_without_pk_sql, DSBFetchTypes.ASSOC, (limit,))

        return result
