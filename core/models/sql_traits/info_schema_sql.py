from abc import ABC


class InfoSchemaSql(ABC):

    @property
    def get_biggest_tables_sql(self) -> str:
        """
        get_biggest_tables_sql

        Returns:
            str: plain SQL
        """
        return "" \
               "SELECT " \
               "table_name AS `Table`, table_schema AS `Database`, round(((data_length + index_length) / 1024 / 1024 / 1024), 2) `seze_in_gb` " \
               "FROM information_schema.TABLES " \
               "ORDER BY seze_in_gb DESC " \
               "LIMIT %s"

    @property
    def get_biggest_tables_sql(self) -> str:
        """
        get_biggest_tables_sql

        Returns:
            str: plain SQL

        """
        return "" \
               "SELECT " \
               "ENGINE, COUNT(*) AS count_tables, SUM(DATA_LENGTH+INDEX_LENGTH) AS size, SUM(INDEX_LENGTH) AS index_size " \
               "FROM information_schema.TABLES " \
               "WHERE TABLE_SCHEMA NOT IN ('mysql', 'INFORMATION_SCHEMA','PERFORMANCE_SCHEMA') AND ENGINE IS NOT NULL " \
               "GROUP BY ENGINE " \
               "LIMIT %s"

    @property
    def get_tables_without_pk_sql(self) -> str:
        """
        get_tables_without_pk_sql

        Returns:
            str: plain SQL

        """
        return "" \
               "SELECT t.TABLE_SCHEMA, t.TABLE_NAME, t.TABLE_ROWS " \
               "FROM information_schema.TABLES t " \
               "LEFT JOIN " \
               "information_schema.TABLE_CONSTRAINTS tc " \
               "ON t.table_schema = tc.table_schema AND t.table_name = tc.table_name AND tc.constraint_type = 'PRIMARY KEY' " \
               "WHERE tc.constraint_name IS NULL AND t.table_type = 'BASE TABLE' " \
               "ORDER BY TABLE_ROWS DESC " \
               "LIMIT %s"

    @property
    def get_size_per_engine_sql(self) -> str:
        """
        get_size_per_engine_sql

        Returns:
            str: plain SQL

        """
        return "" \
               "SELECT ENGINE, COUNT(*) AS count_tables, SUM(DATA_LENGTH+INDEX_LENGTH) AS size, SUM(INDEX_LENGTH) AS index_size " \
               "FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA NOT IN ('mysql', 'INFORMATION_SCHEMA','PERFORMANCE_SCHEMA') AND ENGINE IS NOT NULL " \
               "GROUP BY ENGINE " \
               "LIMIT %s"
