from abc import ABC


class PerfSchemaSql(ABC):

    @property
    def get_top_long_queries_sql(self) -> str:
        """
        get_top_long_queries_sql

        Returns:
            str: plain SQL
        """
        return "" \
               "SELECT " \
               "digest_text, last_seen, count_star, TRUNCATE(avg_timer_wait/1000000000000, 6) AS avg_timer_wait " \
               "FROM " \
               "performance_schema.events_statements_summary_by_digest " \
               "WHERE " \
               "LAST_SEEN >= CURRENT_DATE() - INTERVAL 3 day " \
               "ORDER BY avg_timer_wait DESC " \
               "LIMIT %s;"

    @property
    def get_top_long_updates_sql(self) -> str:
        """
        get_top_long_updates_sql

        Returns:
            str: plain SQL
        """
        return "" \
               "SELECT " \
               "digest_text, count_star / update_total * 100 as percentage_of_all_updates, last_seen " \
               "FROM " \
               "performance_schema.events_statements_summary_by_digest, " \
               "(SELECT sum(count_star) update_total " \
               "FROM performance_schema.events_statements_summary_by_digest " \
               "WHERE digest_text LIKE 'UPDATE%' AND  LAST_SEEN >= CURRENT_DATE() - INTERVAL %s day) update_totals " \
               "WHERE digest_text LIKE 'UPDATE%' AND  LAST_SEEN >= CURRENT_DATE() - INTERVAL %s day " \
               "ORDER BY percentage_of_all_updates DESC " \
               "LIMIT %s"

    @property
    def get_index_stats_for_top_tables_sql(self) -> str:
        """
        get_index_stats_for_top_tables_sql

        Returns:
            str: plain SQL
        """
        return "" \
               "SELECT " \
               "object_schema AS table_schema, object_name AS table_name, index_name, count_fetch " \
               "FROM " \
               "performance_schema.table_io_waits_summary_by_index_usage " \
               "WHERE " \
               "`object_schema` IN('test_database', 'prfbonus_system') AND `object_name` IN('wallet_transactions', 'Network', 'casino_bonus') " \
               "GROUP BY " \
               "object_schema, object_name, index_name " \
               "ORDER BY object_schema, object_name " \
               "LIMIT 70"
