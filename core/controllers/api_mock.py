from typing import Dict, Any

from core.controllers import ApiController
from core.controllers.base import BaseController


class ApiMockController(BaseController):

    def __init__(self) -> None:
        pass

    def _get_response(self, payload: Dict[str, str]) -> Dict[str, Any]:
        """
        _get_response

        Args:
            payload (Dict[str, str]):

        Returns:
            Dict[str, str]
        """
        response: Dict[str, Any] = {
            'status': ApiController.STATUS_OK,
            'database': {
                'name': 'Test Database',
                'id': 0
            },
            'logs': [],
            'payload': payload
        }

        return response

    def get_monitors(self) -> Dict[str, Any]:
        return self._get_response({
            "BACKGROUND THREAD": [
                "srv_main_thread loops: 111 srv_active, 0 srv_shutdown, 1606 srv_idle",
                "srv_main_thread log flush and writes: 222"
            ],
            "SEMAPHORES": [
                "OS WAIT ARRAY INFO: reservation count 1212",
                "OS WAIT ARRAY INFO: signal count 3131",
                "Mutex spin waits 121, rounds 44121, OS waits 33344",
                "RW-shared spins 22223, rounds 343, OS waits 777",
                "RW-excl spins 34443, rounds 44, OS waits 6666",
                "Spin rounds per wait: -2205.65 mutex, 19.80 RW-shared, -33.79 RW-excl"
            ],
            "BUFFER POOL AND MEMORY": [
                "Total memory allocated 12222; in additional pool allocated 0",
                "Dictionary memory allocated 444",
                "Buffer pool size   666",
                "Free buffers       77",
                "Database pages     888",
                "Old database pages 999",
                "Modified db pages  00",
                "Pending reads 0",
                "Pending writes: LRU 0, flush list 0, single page 0",
                "Pages made young 1877997976, not young 24728163129",
                "14.68 youngs/s, 26.53 non-youngs/s",
                "Pages read 1212121, created 22211, written 1111",
                "8.61 reads/s, 11.57 creates/s, 105.28 writes/s",
                "Buffer pool hit rate 1000 / 1000, young-making rate 0 / 1000 not 0 / 1000",
                "Pages read ahead 0.00/s, evicted without access 0.00/s, Random read ahead 0.00/s",
                "LRU len: 5439209, unzip_LRU len: 0",
                "I/O sum[93408]:cur[320], unzip sum[0]:cur[0]"
            ],
            "ROW OPERATIONS": [
                "0 queries inside InnoDB, 0 queries in queue",
                "5 read views open inside InnoDB",
                "Main thread process no. 32576, id 1111, state: sleeping",
                "Number of rows inserted 112, updated 222, deleted 444, read 111",
                "458.48 inserts/s, 967.14 updates/s, 39.50 deletes/s, 4109620.80 reads/s"
            ],
            "TRANSACTIONS": [
                {
                    "uip": "test_login@100.200.30.64",
                    "trans_id": "10406209113",
                    "operation": "update",
                    "sql_info": [
                        "COMMIT",
                        "Trx read view will not see trx with id >= 111, sees < 222",
                        "mysql tables in use 1, locked 1"
                    ],
                    "general_info": [
                        "COMMIT",
                        "Trx read view will not see trx with id >= 111, sees < 222",
                        "mysql tables in use 1, locked 1"
                    ]
                },
                {
                    "uip": "test_login@100.200.30.64",
                    "trans_id": "10406209099",
                    "operation": "update",
                    "sql_info": [
                        "COMMIT",
                        "Trx read view will not see trx with id >= 333, sees < 11112",
                        "mysql tables in use 1, locked 1"
                    ],
                    "general_info": [
                        "COMMIT",
                        "Trx read view will not see trx with id >= 1122, sees < 44444",
                        "mysql tables in use 1, locked 1"
                    ]
                },
                {
                    "uip": "test_login@100.200.30.201",
                    "trans_id": "10406209090",
                    "operation": "statistics",
                    "sql_info": [
                        "INSERT IGNORE INTO",
                        "`test_database`.`test_table`",
                        "SET",
                        "`key` = 'tkey_36271479',",
                        "`value` = 1,",
                        "`date_modified` = NOW()"
                    ],
                    "general_info": [
                        "INSERT IGNORE INTO",
                        "`test_database`.`test_table`",
                        "SET",
                        "`key` = 'tkey_36271479',",
                        "`value` = 1,",
                        "`date_modified` = NOW()"
                    ]
                },
                {
                    "uip": "test@100.200.300.40",
                    "trans_id": "10383605280",
                    "operation": "update",
                    "sql_info": [
                        "SELECT",
                        "`user`,",
                        "`pass`",
                        "FROM",
                        "`test_database`.`test_table`",
                        "WHERE",
                        "`dpre` = 'test'",
                        "AND",
                        "`domain` = 'test_value'",
                        "Trx read view will not see trx with id >= 111, sees < 222",
                        "mysql tables in use 1, locked 1"
                    ],
                    "general_info": [
                        "SELECT",
                        "`user`,",
                        "`pass`",
                        "FROM",
                        "`test_database`.`test_table`",
                        "WHERE",
                        "`dpre` = 'test'",
                        "AND",
                        "`domain` = 'test_value'",
                        "Trx read view will not see trx with id >= 1112, sees < 3333",
                        "mysql tables in use 1, locked 1"
                    ]
                },
                {
                    "uip": "test_login@100.200.300.40",
                    "trans_id": "10406209082",
                    "operation": "init",
                    "sql_info": [
                        "INSERT INTO `test_database`.`test_re`",
                        "SET",
                        "`date`=''2011-08-13 17:50:51',",
                        "`type`='periodic',",
                        "`name`='test_tt',",
                        "`error_message`='Could not connect to host',",
                        "20 lock struct(s), heap size 2936, 10 row lock(s), undo log entries 9"
                    ],
                    "general_info": [
                        "INSERT INTO `test_database`.`test_re`",
                        "SET",
                        "`date`=''2011-08-13 17:50:51',",
                        "`type`='periodic',",
                        "`name`='test_tt',",
                        "`error_message`='Could not connect to host',",
                        "20 lock struct(s), heap size 2936, 10 row lock(s), undo log entries 9"
                    ]
                },
                {
                    "uip": "test_login@100.200.30.25",
                    "trans_id": "10405870559",
                    "operation": "Sending data",
                    "sql_info": [
                        "COMMIT",
                        "Trx read view will not see trx with id >= 111, sees < 222",
                        "mysql tables in use 1, locked 0"
                    ],
                    "general_info": [
                        "COMMIT",
                        "Trx read view will not see trx with id >= 111, sees < 222",
                        "mysql tables in use 1, locked 0"
                    ]
                },
                {
                    "uip": "test_login@100.200.30.25",
                    "trans_id": "10406085949",
                    "operation": "Sending data",
                    "sql_info": [
                        "SELECT * FROM `test_debee`.`my_tests` WHERE rf LIKE '%xaaaa%' LIMIT 1",
                        "Trx read view will not see trx with id >= 111, sees < 222",
                        "mysql tables in use 1, locked 0"
                    ],
                    "general_info": [
                        "SELECT * FROM `test_debee`.`my_tests` WHERE rf LIKE '%ttttrr%' LIMIT 1",
                        "Trx read view will not see trx with id >= 111, sees < 222",
                        "mysql tables in use 1, locked 0"
                    ]
                }
            ],
            "LATEST FOREIGN KEY ERROR": [
                {
                    "tid": "342685090715",
                    "status": "ACTIVE 0 sec inserting",
                    "uip": "test_login@100.200.300.40",
                    "query": "INSERT INTO `test_database`.`test_tbl` SET `id` = 0, ON DUPLICATE KEY UPDATE `date_a` = NOW()",
                    "do": "Foreign key constraint fails for table `test_database`.`test_tbl`:, CONSTRAINT `test_tbl_ibfk_1` FOREIGN KEY (`id`) rfS `test_ref` (`id`) ON DELETE CASCADE"
                }
            ],
            "LATEST DETECTED DEADLOCK": [
                {
                    "tid": "369548792723",
                    "status": "ACTIVE 0 sec fetching rows",
                    "uip": "test_login@100.200.300.40",
                    "query": "UPDATE `prftest`.`test_ceb` SET `a` = 'a1', `b` = NOW() WHERE `expiration_date` <= NOW() AND `c` IN ('x')",
                    "lock": {
                        "do": "WAITING FOR THIS LOCK TO BE GRANTED",
                        "tab_key": " `PRIMARY` of table `prftest`.`test_ceb` ",
                        "ltype": "X",
                        "is_gap": False,
                        "lrecords_num": "520"
                    }
                },
                {
                    "tid": "369548792259",
                    "status": "ACTIVE 0 sec starting index read",
                    "uip": "test_login@100.200.300.40",
                    "query": "UPDATE `prftest`.`test_ceb` SET `a` = 'a1', `b` = NOW() WHERE `expiration_date` <= NOW() AND `c` IN ('x')",
                    "lock": {
                        "do": "HOLDS THE LOCK",
                        "tab_key": " `PRIMARY` of table `prftest`.`test_ceb` ",
                        "ltype": "X",
                        "is_gap": False,
                        "lrecords_num": "3056"
                    }
                },
                {
                    "tid": "369548792259",
                    "status": "ACTIVE 0 sec starting index read",
                    "uip": "test_login@100.200.300.40",
                    "query": "UPDATE `prftest`.`test_ceb` SET `a` = 'a1', `b` = NOW() WHERE `expiration_date` <= NOW() AND `c` IN ('x')",
                    "lock": {
                        "do": "WAITING FOR THIS LOCK TO BE GRANTED",
                        "tab_key": " `PRIMARY` of table `prftest`.`test_ceb` ",
                        "ltype": "X",
                        "is_gap": False,
                        "lrecords_num": None
                    }
                }
            ]
        })

    def get_variables(self) -> Dict[str, Any]:
        return self._get_response({
            "sync_binlog": [
                "<span class='span_number'>1</span>",
                "<span class='span_number'>1</span>"
            ],
            "binlog_order_commits": [
                "<span class='span_on_off'>ON</span>",
                "<span class='span_on_off'>ON</span>"
            ],
            "relay_log_space_limit": [
                "<span class='span_number'>0</span>",
                "<span class='span_number'>0</span>"
            ],
            "timestamp": [
                "<span class='span_number'>1566754039.850771</span>",
                "-"
            ],
            "sql_warnings": [
                "<span class='span_on_off'>OFF</span>",
                "<span class='span_on_off'>OFF</span>"
            ],
            "innodb_rollback_on_timeout": [
                "<span class='span_on_off'>OFF</span>",
                "<span class='span_on_off'>OFF</span>"
            ],
            "max_connect_errors": [
                "<span class='span_number'>1000000</span>",
                "<span class='span_number'>1000000</span>"
            ],
            "storage_engine": [
                "<span class='span_normal'>InnoDB</span>",
                "<span class='span_normal'>InnoDB</span>"
            ],
            "gtid_next": [
                "<span class='span_normal'>AUTOMATIC</span>",
                "-"
            ],
            "gtid_mode": [
                "<span class='span_on_off'>OFF</span>",
                "<span class='span_on_off'>OFF</span>"
            ],
            "license": [
                "<span class='span_normal'>GPL</span>",
                "<span class='span_normal'>GPL</span>"
            ],
            "version_compile_os": [
                "<span class='span_normal'>Linux</span>",
                "<span class='span_normal'>Linux</span>"
            ],
            "innodb_sync_array_size": [
                "<span class='span_number'>1</span>",
                "<span class='span_number'>1</span>"
            ],
            "subordinate_compressed_protocol": [
                "<span class='span_on_off'>ON</span>",
                "<span class='span_on_off'>ON</span>"
            ],
            "sql_auto_is_null": [
                "<span class='span_on_off'>OFF</span>",
                "<span class='span_on_off'>OFF</span>"
            ],
            "optimizer_search_depth": [
                "<span class='span_number'>62</span>",
                "<span class='span_number'>62</span>"
            ],
            "automatic_sp_privileges": [
                "<span class='span_on_off'>ON</span>",
                "<span class='span_on_off'>ON</span>"
            ],
            "big_tables": [
                "<span class='span_on_off'>OFF</span>",
                "<span class='span_on_off'>OFF</span>"
            ],
            "collation_database": [
                "<span class='span_normal'>latin1_swedish_ci</span>",
                "<span class='span_normal'>latin1_swedish_ci</span>"
            ],
            "innodb_flush_method": [
                "<span class='span_normal'>O_DIRECT</span>",
                "<span class='span_normal'>O_DIRECT</span>"
            ],
            "skip_show_database": [
                "<span class='span_on_off'>OFF</span>",
                "<span class='span_on_off'>OFF</span>"
            ],
            "innodb_ft_cache_size": [
                "<span class='span_number'>8000000</span>",
                "<span class='span_number'>8000000</span>"
            ],
            "innodb_read_ahead_threshold": [
                "<span class='span_number'>56</span>",
                "<span class='span_number'>56</span>"
            ],
            "delay_key_write": [
                "<span class='span_on_off'>ON</span>",
                "<span class='span_on_off'>ON</span>"
            ],
            "default_tmp_storage_engine": [
                "<span class='span_normal'>InnoDB</span>",
                "<span class='span_normal'>InnoDB</span>"
            ],
            "innodb_lock_wait_timeout": [
                "<span class='span_number'>50</span>",
                "<span class='span_number'>50</span>"
            ],
            "innodb_ft_user_stopword_table": [
                "<span class='span_normal'></span>",
                "<span class='span_normal'></span>"
            ],
            "have_dynamic_loading": [
                "<span class='span_normal'>YES</span>",
                "<span class='span_normal'>YES</span>"
            ],
            "subordinate_pending_jobs_size_max": [
                "<span class='span_number'>16777216</span>",
                "<span class='span_number'>16777216</span>"
            ],
            "report_host": [
                "<span class='span_normal'></span>",
                "<span class='span_normal'></span>"
            ],
            "large_files_support": [
                "<span class='span_on_off'>ON</span>",
                "<span class='span_on_off'>ON</span>"
            ]
        })

    def get_replication_data(self) -> Dict[str, Any]:
        return self._get_response({
            "main_important_values": {
                "File": "mysql-bin-log.1",
                "Position": 12
            },
            "main_full_log": {
                "File": "mysql-bin-log.31",
                "Position": 33,
                "Binlog_Do_DB": "",
                "Binlog_Ignore_DB": "",
                "Executed_Gtid_Set": ""
            },
            "subordinate_important_values": {
                "Seconds_Behind_Main": " 0",
                "Main_Log_File": " main-bin.11",
                "Read_Main_Log_Pos": " 1307",
                "Relay_Log_File": " subordinate-relay-bin.211",
                "Relay_Log_Pos": " 1508",
                "Relay_Main_Log_File": " main-bin.222",
                "Last_Error": "",
                "Last_IO_Error": "",
                "Last_SQL_Error": ""
            },
            "subordinate_full_log": {
                "Subordinate_IO_State": " Waiting for main to send event",
                "Main_Host": " localhost",
                "Main_User": " repl",
                "Main_Port": " 13000",
                "Connect_Retry": " 60",
                "Main_Log_File": " main-bin.000002",
                "Read_Main_Log_Pos": " 1307",
                "Relay_Log_File": " subordinate-relay-bin.000003",
                "Relay_Log_Pos": " 1508",
                "Relay_Main_Log_File": " main-bin.000002",
                "Subordinate_IO_Running": " Yes",
                "Subordinate_SQL_Running": " Yes",
                "Replicate_Do_DB": "",
                "Replicate_Ignore_DB": "",
                "Replicate_Do_Table": "",
                "Replicate_Ignore_Table": "",
                "Replicate_Wild_Do_Table": "",
                "Replicate_Wild_Ignore_Table": "",
                "Last_Errno": " 0",
                "Last_Error": "",
                "Skip_Counter": " 0",
                "Exec_Main_Log_Pos": " 1307",
                "Relay_Log_Space": " 1858",
                "Until_Condition": " None",
                "Until_Log_File": "",
                "Until_Log_Pos": " 0",
                "Main_SSL_Allowed": " No",
                "Main_SSL_CA_File": "",
                "Main_SSL_CA_Path": "",
                "Main_SSL_Cert": "",
                "Main_SSL_Cipher": "",
                "Main_SSL_Key": "",
                "Seconds_Behind_Main": " 0",
                "Main_SSL_Verify_Server_Cert": " No",
                "Last_IO_Errno": " 0",
                "Last_IO_Error": "",
                "Last_SQL_Errno": " 0",
                "Last_SQL_Error": "",
                "Replicate_Ignore_Server_Ids": "",
                "Main_Server_Id": " 1",
                "Main_UUID": " abc-cda ",
                "Main_Info_File": " ",
                "SQL_Delay": " 0",
                "SQL_Remaining_Delay": " NULL",
                "Subordinate_SQL_Running_State": " Reading event from the relay log",
                "Main_Retry_Count": " 10",
                "Main_Bind": "",
                "Last_IO_Error_Timestamp": "",
                "Last_SQL_Error_Timestamp": "",
                "Main_SSL_Crl": "",
                "Main_SSL_Crlpath": "",
                "Retrieved_Gtid_Set": " abc-cda ",
                "Executed_Gtid_Set": " abc-cda ",
                "Auto_Position": " 1",
                "Replicate_Rewrite_DB": "",
                "Channel_name": "",
                "Main_TLS_Version": " TLSv1.2",
                "Main_public_key_path": " xxx.yyy",
                "Get_main_public_key": " 0"
            },
            "conslusion": "conslusion"
        })

    def get_overview(self) -> Dict[str, Any]:
        return self._get_response({
            "active_processes": [
                {
                    "ID": 1,
                    "USER": "test_user",
                    "HOST": "localhost",
                    "DB": None,
                    "COMMAND": "Daemon",
                    "TIME": 55,
                    "STATE": "Waiting for next activation",
                    "INFO": None
                },
                {
                    "ID": 13167282,
                    "USER": "test_login",
                    "HOST": "100.200.300.11:998",
                    "DB": "test_database",
                    "COMMAND": "Query",
                    "TIME": 0,
                    "STATE": "executing",
                    "INFO": "SELECT * FROM information_schema.PROCESSLIST  WHERE COMMAND != 'Sleep'"
                }
            ],
            "commands_general_stats": {
                "select": 0.2,
                "update": 0.15,
                "insert": 0.14
            },
            "keys_hit_rate": {
                "read_effic": 100,
                "write_effic": 94
            },
            "cache_hit_rate": {
                "qcache_select_hit_rate": 65
            },
            "buffer_efficiency": {
                "buffer_efficiency": 99,
                "utilization": 0.75
            },
            "connections_info": {
                "max_connections": 300,
                "connection_errs": {
                    "Connection_errors_accept": "0",
                    "Connection_errors_internal": "0",
                    "Connection_errors_max_connections": "494",
                    "Connection_errors_peer_address": "0",
                    "Connection_errors_select": "0",
                    "Connection_errors_tcpwrap": "0"
                }
            },
            "get_logs_info": {
                "log_bin": "ON",
                "log_bin_basename": "/logs/xx/mysql-bin-log",
                "log_bin_index": "/logs/xx/mysql-bin-log.index",
                "log_bin_trust_function_creators": "OFF",
                "log_bin_use_v1_row_events": "OFF",
                "log_error": "/logs/xx/mysql-error.log",
                "log_output": "FILE",
                "log_queries_not_using_indexes": "ON",
                "log_subordinate_updates": "OFF",
                "log_slow_admin_statements": "OFF",
                "log_slow_subordinate_statements": "OFF",
                "log_throttle_queries_not_using_indexes": "0",
                "log_warnings": "1"
            }
        })

    def get_performance_schema(self) -> Dict[str, Any]:
        return self._get_response({
            "top_long_queries": [
                {
                    "digest_text": "INSERT INTO `test` . `test` ( `a` , `b` , `c` , `d` , `e` , `f` , `g` ) VALUES ( ?, ... , NOW ( ) , ?, ... ) ",
                    "last_seen": "2012-08-22 10:01:30",
                    "count_star": 867,
                    "avg_timer_wait": "29.768109"
                },
                {
                    "digest_text": "CALL `test_db` . `testSp` (...) ",
                    "last_seen": "2012-08-22 08:25:21",
                    "count_star": 35,
                    "avg_timer_wait": "22.161064"
                },
                {
                    "digest_text": "FLUSH LOCAL TABLES ",
                    "last_seen": "2012-08-22 04:00:05",
                    "count_star": 216,
                    "avg_timer_wait": "15.172443"
                },
                {
                    "digest_text": "INSERT IGNORE INTO `test` . `testdb` ( DATE , `a` , `b` , `c` , `d` , `e`) VALUES (...) ",
                    "last_seen": "2012-08-19 16:25:56",
                    "count_star": 671,
                    "avg_timer_wait": "7.191730"
                },
                {
                    "digest_text": "INSERT INTO `test` . test ( SYSTEM_USER , ACTION , `url` , `input` , `output` , `requested` , `responded` ) VALUES (...) ",
                    "last_seen": "2012-08-22 16:49:55",
                    "count_star": 5019,
                    "avg_timer_wait": "4.943876"
                },
                {
                    "digest_text": "UPDATE `testdb` . `testtab` AS SYSTEM_USER SET `user` . `tm` = NOW ( ) WHERE `user` . `id` = ? ",
                    "last_seen": "2012-08-22 16:49:24",
                    "count_star": 2768,
                    "avg_timer_wait": "4.178116"
                },
                {
                    "digest_text": "SELECT * FROM `test_database` . `testtbl` WHERE `a` = ? ORDER BY `id` DESC LIMIT ? ",
                    "last_seen": "2012-08-21 17:20:38",
                    "count_star": 107,
                    "avg_timer_wait": "2.004437"
                },
                {
                    "digest_text": "UPDATE `test_database` . `test_table` SET `a` = ? WHERE `id` = ? ",
                    "last_seen": "2012-08-21 17:29:53",
                    "count_star": 114,
                    "avg_timer_wait": "1.920300"
                },
                {
                    "digest_text": "CALL `newSp` (...) ",
                    "last_seen": "2012-08-22 16:56:21",
                    "count_star": 2334,
                    "avg_timer_wait": "1.453093"
                },
                {
                    "digest_text": "CALL `testSo` (?) ",
                    "last_seen": "2012-08-22 14:31:26",
                    "count_star": 337,
                    "avg_timer_wait": "1.448291"
                }
            ],
            "top_long_updates": [
                {
                    "digest_text": "UPDATE `test_database` . `test_table` SET `c` = NOW ( ) , `a` = ? WHERE `b` = ? ",
                    "percentage_of_all_updates": "24.5456",
                    "last_seen": "2012-08-22 18:00:17"
                },
                {
                    "digest_text": "UPDATE `test_database` . `test_table` SET `a` = ? , `b` = ? , `c` = ? , `st` = NOW ( ) , `last_tick_time` = NOW ( ) WHERE `id` = ? ",
                    "percentage_of_all_updates": "24.5403",
                    "last_seen": "2012-08-22 18:00:17"
                },
                {
                    "digest_text": "UPDATE `test_database` . `test_table` SET `a` = ? , `b` = NOW ( ) WHERE `id` = ? ",
                    "percentage_of_all_updates": "22.7884",
                    "last_seen": "2012-08-22 18:00:18"
                },
                {
                    "digest_text": "UPDATE `test_database` `test_table` JOIN `test_table2` `tg` ON `t` . `a` = `tg` . `id` LEFT JOIN `a` `tw` ON `t` . `c` = `tw` . `test_id` SET `t` ."
                                   " `test_states_id` = ?  WHERE `t` . `end_date` <= ?",
                    "percentage_of_all_updates": "3.8957",
                    "last_seen": "2012-08-22 18:00:12"
                },
                {
                    "digest_text": "UPDATE `test_database`.test_table SET DATA = ? , `modified_at` = ? WHERE `session_id` = ? ",
                    "percentage_of_all_updates": "1.0790",
                    "last_seen": "2012-08-21 15:42:40"
                },
                {
                    "digest_text": "UPDATE `test_database` . `test_table` AS `fr` INNER JOIN `t_cg_test` . `fer_testpls` AS `frp` ON `fr` . `id` = `frp` . `fte` ",
                    "percentage_of_all_updates": "0.7791",
                    "last_seen": "2012-08-22 18:00:17"
                },
                {
                    "digest_text": "UPDATE `test_database` . `test_table` AS `frp` INNER JOIN `t_cg_test` . `fer` AS `fr` ON `frp` . `fte` = `fr` . `id` AND `fr` . `der` != ?",
                    "percentage_of_all_updates": "0.7791",
                    "last_seen": "2012-08-22 18:00:17"
                },
                {
                    "digest_text": "UPDATE `test_database` . `test_table` `fr` SET `fr` . `n_testpls` = ( SELECT COUNT ( * ) FROM `t_cg_test` . `fer_testpls` `frp` WHERE `frp` . `flag` = ?  ",
                    "percentage_of_all_updates": "0.7791",
                    "last_seen": "2012-08-22 18:00:17"
                },
                {
                    "digest_text": "UPDATE `test_database` SET `token` = ? , `timestamp` = ? , `current_site` = ? WHERE `login` = ? ",
                    "percentage_of_all_updates": "0.7564",
                    "last_seen": "2012-08-21 15:41:11"
                },
                {
                    "digest_text": "UPDATE `test_database` . `test_table` SET `status` = ? , `progress` = ? , `end_time` = NOW ( ) , `last_tick_time` = NOW ( ) WHERE `id` = ? ",
                    "percentage_of_all_updates": "0.3932",
                    "last_seen": "2012-08-22 18:00:17"
                }
            ],
            "index_stats_for_top_tables": {
                "test.test_database": {
                    "no_index": 10370499,
                    "index": 28389561
                },
                "test_database.test": {
                    "no_index": 4783678,
                    "index": 1262971
                }
            }
        })

    def get_info_schema(self) -> Dict[str, Any]:
        return self._get_response({
            "get_biggest_tables_chached": [
                {
                    "Table": "test_table1",
                    "Database": "tast_db1",
                    "seze_in_gb": "4.44"
                },
                {
                    "Table": "test_table2",
                    "Database": "tast_db1",
                    "seze_in_gb": "3.12"
                },
                {
                    "Table": "test_table3",
                    "Database": "tast_db1",
                    "seze_in_gb": "1.99"
                },
                {
                    "Table": "test_table4",
                    "Database": "tast_db1",
                    "seze_in_gb": "1.33"
                },
                {
                    "Table": "test_table5",
                    "Database": "tast_db1",
                    "seze_in_gb": "1.31"
                },
                {
                    "Table": "test_table6",
                    "Database": "tast_db1",
                    "seze_in_gb": "0.99"
                },
                {
                    "Table": "test_table7",
                    "Database": "tast_db1",
                    "seze_in_gb": "0.88"
                },
                {
                    "Table": "test_table8",
                    "Database": "tast_db1",
                    "seze_in_gb": "0.85"
                },
                {
                    "Table": "test_table9",
                    "Database": "tast_db1",
                    "seze_in_gb": "0.80"
                },
                {
                    "Table": "test_table10",
                    "Database": "test_database",
                    "seze_in_gb": "0.77"
                }
            ],
            "get_size_per_engine_cached": [
                {
                    "ENGINE": "InnoDB",
                    "count_tables": 22858,
                    "size": "1212333",
                    "index_size": "434343"
                },
                {
                    "ENGINE": "MyISAM",
                    "count_tables": 1733,
                    "size": "535343",
                    "index_size": "4433"
                }
            ],
            "get_tables_without_pk_cached": [
                {
                    "TABLE_SCHEMA": "test_database",
                    "TABLE_NAME": "variables_by_thread",
                    "TABLE_ROWS": 100
                },
                {
                    "TABLE_SCHEMA": "test_database",
                    "TABLE_NAME": "session_connect_attrs",
                    "TABLE_ROWS": 100
                },
                {
                    "TABLE_SCHEMA": "test_database",
                    "TABLE_NAME": "session_account_connect_attrs",
                    "TABLE_ROWS": 100
                },
                {
                    "TABLE_SCHEMA": "test_database",
                    "TABLE_NAME": "test_table",
                    "TABLE_ROWS": 100
                },
                {
                    "TABLE_SCHEMA": "test_database",
                    "TABLE_NAME": "test_table",
                    "TABLE_ROWS": 100
                },
                {
                    "TABLE_SCHEMA": "test_database",
                    "TABLE_NAME": "test_table",
                    "TABLE_ROWS": 100
                },
                {
                    "TABLE_SCHEMA": "test_database",
                    "TABLE_NAME": "test_table",
                    "TABLE_ROWS": 100
                },
                {
                    "TABLE_SCHEMA": "test_database",
                    "TABLE_NAME": "test_table",
                    "TABLE_ROWS": 100
                },
                {
                    "TABLE_SCHEMA": "test_database",
                    "TABLE_NAME": "test_table",
                    "TABLE_ROWS": 100
                },
                {
                    "TABLE_SCHEMA": "test_database",
                    "TABLE_NAME": "status_by_thread",
                    "TABLE_ROWS": 100
                }
            ]
        })
