import re
from abc import abstractmethod, ABC
from copy import deepcopy
from typing import Any, List, Dict, Tuple

from core.commons import log_objects
from core.commons.regexper import Regexper
from core.commons.utils import Utils
from core.interfaces.base import Base
from core.interfaces.loggable import Loggable
from core.models.base_model import BaseModel
from core.models.sql_traits.monitors_sql import MonitorsSql
from core.services.dbs import DBS


class Monitor(BaseModel, MonitorsSql, Loggable):

    @property
    def monitor_tag(self) -> str:
        """
        monitor_tag

        Returns:
            str
        """
        pass

    @property
    def result_composed(self) -> Any:
        """
        result_composed

        Returns:
            str
        """
        return self._result_composed

    @property
    def log_content(self) -> str:
        """
        log_content

        Returns:
            str
        """
        return self._log_content

    @result_composed.setter
    def result_composed(self, rc) -> None:
        self._result_composed = rc

    @log_content.setter
    def log_content(self, log) -> str:
        self._log_content = log

    def __init__(self) -> None:
        """
        __init__

        """
        super().__init__()
        self._result_composed: str = None
        self._log_content: str = None

    def __str__(self) -> str:
        """
        __str__

        Returns:
            str
        """
        return f'{self.monitor_tag}'

    def __repr__(self) -> str:
        """
        __repr__

        Returns:
            str
        """
        return f'MONITOR: {self.__class__.__name__} ' \
               f'TAG: {self.monitor_tag} ' \
               f'CONTENT: {self._log_content}'

    def get_as_string(self) -> str:
        """
        get_as_string

        Returns:
            str
        """
        return "InnoDB Monitors"

    @staticmethod
    def module_level_function(param1, param2=None, *args, **kwargs):
        """
        module_level_function

        Args:
            param1 ():
            param2 ():
            *args ():
            **kwargs ():

        Returns:
            str
        """
        if param1 == param2:
            raise ValueError('param1 may not be equal to param2')
        return True

    @staticmethod
    def set_xpath_dict_value(dict: Dict[Any, Any], val, *key_pa) -> None:
        """
        set_xpath_dict_value

        Args:
            dict (Dict[Any, Any]):
            val ():
            *key_pa ():

        Returns:
            None
        """
        ik = key_pa[0]
        if type(dict[ik]) == type({}) and len(key_pa) > 1:
            try:
                return Monitor.set_xpath_dict_value(dict[ik], val, *key_pa[1:])
            except IndexError as e:
                log_objects(e)
                pass
            except Exception as e:
                log_objects(e)
            raise IndexError
        else:
            dict[ik] = val

    @staticmethod
    def get_xpath_dict_value(dict: Dict[Any, Any], *key_pa) -> Any:
        """
        get_xpath_dict_value

        Args:
            dict (Dict[Any, Any]): -
            *key_pa ():

        Returns:
            Any
        """
        ik = key_pa[0]
        if type(dict[ik]) == type({}) and len(key_pa) > 1:
            try:
                return Monitor.get_xpath_dict_value(dict[ik], *key_pa[1:])
            except IndexError as e:
                log_objects(e)
            except Exception as e:
                log_objects(e)
        else:
            return dict[ik]

    def get_result(self) -> Any:  # MonitorLogResult
        """
        get_result

        Returns:
            Any
        """

        # temporary commented
        # (always retur new result)
        # if self.result_composed is not None:
        #     return self.result_composed
        log_objects(self)

        return self._prepare_result()

    def _prepare_result(self) -> Any:
        """
        _prepare_result

        Returns:

        """
        return self.default_parser()

    def default_parser(self) -> List[str]:
        """
        default_parser

        Returns:
            List[str]: list
        """
        return Utils.filter_empty(self.log_content.splitlines(False))

    def _set_result_by_xpath(self, dl_result: List[Dict[Any, Any]], value: Any, *key_pa: str) -> None:
        """
        _set_result_by_xpath

        Args:
            dl_result (List[Dict[Any, Any]]): -
            value (Any): -
            *key_pa (str): -

        Returns:
            None

        """
        for ixx in dl_result:
            if self.get_xpath_dict_value(ixx, *key_pa) is None:
                self.set_xpath_dict_value(ixx, value, *key_pa)
                break

    def get_as_string(self) -> str:
        """
        get_as_string

        Returns:
            str

        """
        return self.__str__()


class BaseMonitors(ABC):
    @abstractmethod
    def _parse_status_log(log: str) -> None:
        """
        _parse_status_log

        Returns:
            None
        """
        pass


class Monitors(Base, MonitorsSql, BaseMonitors):
    LOG_SEPARATOR_REGEXP: str = "[\-]{4,}([\w\s\\\/]+)[\-]{2,}"

    @Base.default_kwargs(html=True, memoize=False)
    def __init__(self, db: DBS, *monitors: Tuple[Monitor, ...], **options: Dict[str, Any]) -> None:
        """
        __init__

        Args:
            db (DBS):
            *monitors (Tuple[Monitor, ...]):
            **options (Dict[str, Any]):
        """

        self.monitors = list(
            filter(
                lambda x: isinstance(x, Monitor), monitors
            )
        )
        self.options = options
        self.status_log = ""
        self.db = db

        self._parse_status_log()

    def _get_innodb_status(self) -> str:
        """
        _get_innodb_status

        Returns:
            None

        """

        try:
            # with open('../test-monitor.txt', 'r') as f2:
            #     log_str = f2.read()
            #     return log_str

            res = self.db.fetchOne(self._get_innodb_status_sql)
            return res[2]

        except Exception as e:
            log_objects(e)
            return ""

    def _parse_status_log(self) -> None:
        """
        _parse_status_log

        Returns:
            None

        """

        log_str: str = self._get_innodb_status()

        splitted_log_content = re.compile(self.LOG_SEPARATOR_REGEXP, re.MULTILINE).split(log_str)

        # Dict {monitor_tag:monitor_object}
        monitor_tags: Dict[str, Monitor] = {var.monitor_tag: var for var in self.monitors if isinstance(var, Monitor)}

        set_constent: str = None

        for x in splitted_log_content:

            if set_constent is not None:
                monitor_tags[set_constent]._log_content = x
                set_constent = None
                continue

            x = Regexper.clean_str([re.compile("[\-]?", re.MULTILINE)], x.strip())

            if x.strip() == "" or x is None:
                break

            if x in monitor_tags.keys():
                set_constent = x

    def get_partial_monitors_result(self) -> Dict[str, Any]:  # Dict[str, MonitorLogResult]
        """
        get_partial_monitors_result

        Returns:
            Dict[str, Any]: dict

        """
        general_result: Dict[str, Any] = dict((x.monitor_tag, x.get_result()) for x in self.monitors)

        return general_result


class MonitorDedlock(Monitor):
    monitor_tag: str = "LATEST DETECTED DEADLOCK"
    LOG_SEPARATOR_REGEXP: str = "(WAITING FOR THIS LOCK TO BE GRANTED" \
                                "|HOLDS THE LOCK" \
                                "|TRANSACTION:\s?TRANSACTION\s[0-9]+,(.*[\n|\r|\r\n|\n\r]))"

    '''
    RegExp
    '''
    re_sql_start = re.compile("(MySQL thread id)", re.MULTILINE)
    re_sql_end = re.compile("(\*\*\*[\s?0-9]+)", re.MULTILINE)
    re_ip = re.compile("(([0-9]+\.)+[0-9]+)+", re.MULTILINE)
    re_row_locks = re.compile(".*\s([0-9]+)\srow lock\(s\)")
    re_lock = re.compile(".*LOCKS space id [0-9]+")
    re_lock_gap = re.compile("(not\sgap|gap)")
    re_ltype = re.compile("(lock[\s_\-]mode ([A-Z]+) locks)")
    re_trans_status = re.compile("TRANSACTION\s?([0-9]+)\s?(.*)")
    re_do = re.compile("(HOLDS THE LOCK|WAITING FOR THIS LOCK TO BE GRANTED)")

    def __init__(self) -> None:
        """
        __init__

        """
        super().__init__()
        self.set = None

    def _set_result_by_xpath(self, dl_result: List[Dict[Any, Any]], value: Any, *key_pa: str) -> None:
        """
        _set_result_by_xpath

        Args:
            dl_result (List[Dict[Any, Any]]): -
            value (Any): -
            *key_pa (str): -

        Returns:
            None

        """
        for ixx in dl_result:
            if self.get_xpath_dict_value(ixx, *key_pa) is None:
                self.set_xpath_dict_value(ixx, value, *key_pa)
                break

    def _prepare_result(self) -> Dict[str, str]:
        """
        _prepare_result

        Returns:
            Dict[str, str]: dict

        """
        da_pattern = {
            "tid": None,  # 123 [transaction ID]
            "status": None,  # active [status]
            "uip": None,  # user 192.0.0.1 [use and IP]
            "query": None,  # SELECT * FROM abc [query]
            "lock": {
                "do": None,  # is waiting, trying to set up lock
                "tab_key": None,  # `PRIMARY` of table `abc` [table and key]
                "ltype": None,  # X [lock type]
                "is_gap": None,  # no [is gap lock or not]
                "lrecords_num": None  # 520 [wants to lock records...]
            }
        }

        da = deepcopy(da_pattern)
        db = deepcopy(da_pattern)
        dc = deepcopy(da_pattern)

        dl_result = [da, db, dc]

        if self.log_content is None:
            lc = ""
        else:
            lc = self.log_content

        splitted_log_content = re.compile(self.LOG_SEPARATOR_REGEXP, re.MULTILINE).split(lc)

        for k in splitted_log_content:

            if k is None:
                continue

            k_lines = k.splitlines(False)
            sql_acumulator = ""
            feed_sql_acumulator: bool = False

            for single_line in k_lines:

                # what does transaction do
                if self.re_do.match(single_line.__str__()):
                    rsearch = self.re_do.search(single_line)
                    self._set_result_by_xpath(dl_result, rsearch.group(1), "lock", "do")

                # transaction id and status
                if self.re_trans_status.match(single_line.__str__()):
                    rsearch = self.re_trans_status.search(single_line)
                    trans_id = rsearch.group(1)
                    trans_status = rsearch.group(2)
                    self._set_result_by_xpath(dl_result, trans_id, "tid")
                    self._set_result_by_xpath(dl_result, Regexper.clean_str([","], trans_status).strip(), "status")

                # number of locked records
                if self.re_row_locks.match(single_line.__str__()):
                    rsearch = self.re_row_locks.search(single_line)
                    row_locks = rsearch.group(1)
                    self._set_result_by_xpath(dl_result, row_locks, "lock", "lrecords_num")

                # on table and key
                if self.re_lock.match(single_line.__str__()):
                    index_info = Regexper.find_between(single_line, "index", "trx id")
                    self._set_result_by_xpath(dl_result, index_info, "lock", "tab_key")

                # gap lock
                gap = self.re_lock_gap.search(single_line)
                if gap is not None:
                    is_gap = gap.group(1).strip() != "not gap"
                    self._set_result_by_xpath(dl_result, is_gap, "lock", "is_gap")

                # lock type (X, S, XI, SI etc.)
                ltype = self.re_ltype.search(single_line)
                if ltype is not None:
                    ltype = ltype.group(2).strip()
                if ltype is not None:
                    self._set_result_by_xpath(dl_result, ltype, "lock", "ltype")

                if self.re_sql_start.match(single_line.__str__()):

                    feed_sql_acumulator = True

                    rsearch = self.re_ip.search(single_line)
                    if rsearch is not None:
                        # user and IP
                        ip = rsearch.group(1)
                        pos = single_line.find(ip)
                        sl = single_line[(pos + len(ip)):].split("[\s]?")
                        user = sl[0].strip()
                        user = re.split(r'[\s]+', user)
                        self._set_result_by_xpath(dl_result, user[0] + "@" + ip, "uip")

                elif feed_sql_acumulator is True and self.re_sql_end.match(single_line.__str__()):
                    # SQL queries
                    feed_sql_acumulator = False
                    self._set_result_by_xpath(dl_result, Utils.clear_breaks(sql_acumulator), "query")

                elif feed_sql_acumulator is True and not self.re_sql_end.match(single_line.__str__()):
                    sql_acumulator += Regexper.clean_white_chars(single_line)

        dict_trans2_header = dict(filter(lambda ix: ix[0] in ["tid", "status", "uip", "query"], dl_result[1].items()))

        dict_trans2_body = dict(filter(lambda ix: ix[0] in ["lock"], dl_result[2].items()))

        mrg = Utils.dict_of_dicts_merge(dict_trans2_header, dict_trans2_body)

        dl_result.pop()
        dl_result.append(mrg)

        self.result_composed = dl_result

        return self.result_composed


class MonitorBackground(Monitor):
    monitor_tag: str = "BACKGROUND THREAD"

    def __init__(self) -> None:
        """
        __init__
        """
        super().__init__()


class MonitorBufferAndMemory(Monitor):
    monitor_tag: str = "BUFFER POOL AND MEMORY"

    def __init__(self) -> None:
        """
        __init__

        """
        super().__init__()


class MonitorBufferHash(Monitor):
    monitor_tag: str = "INSERT BUFFER AND ADAPTIVE HASH INDEX"

    def __init__(self) -> None:
        """
        __init__

        """
        super().__init__()


class MonitorBufferIndyvidualy(Monitor):
    monitor_tag: str = "INDIVIDUAL BUFFER POOL INFO"

    def __init__(self) -> None:
        """
        __init__

        """
        super().__init__()


class MonitorFile(Monitor):
    monitor_tag: str = "FILE I/O"

    def __init__(self) -> None:
        """
        __init__

        """
        super().__init__()


class MonitorLatestForeign(Monitor):
    monitor_tag = "LATEST FOREIGN KEY ERROR"

    '''
    RegExp
    '''
    re_sql_start = re.compile("(MySQL thread id)", re.MULTILINE)
    re_sql_end = re.compile("(key|Foreign).*fails", re.MULTILINE)
    re_ip = re.compile("(([0-9]+\.)+[0-9]+)+", re.MULTILINE)
    re_fkey_end = re.compile("Trying to")
    re_trans_status = re.compile("TRANSACTION\\s?([0-9]+)\\s?(.*)")

    def __init__(self) -> None:
        """
        __init__

        """
        super().__init__()
        self.set = None

    def _prepare_result(self) -> List[str]:
        """
        _prepare_result

        Returns:
            List[str]: list

        """
        da_pattern = {
            "tid": None,  # 123 [transaction ID]
            "status": None,  # active [status]
            "uip": None,  # user 192.0.0.1 [use and IP]
            "query": None,  # SELECT * FROM abc [query]
            "do": None  # Trying to insert record...
        }

        da = deepcopy(da_pattern)
        dl_result = [da]

        if self.log_content is None:
            lc = ""
        else:
            lc = self.log_content

        splitted_log_content = [lc]

        for k in splitted_log_content:

            if k is None:
                continue

            k_lines = k.splitlines(False)
            sql_acumulator = ""
            msg_acumulator = ""
            feed_sql_acumulator: bool = False
            feed_msg_acumulator: bool = False

            for single_line in k_lines:

                # transaction id and status
                if self.re_trans_status.match(single_line):
                    rsearch = self.re_trans_status.search(single_line)
                    trans_id = rsearch.group(1)
                    trans_status = rsearch.group(2)
                    self._set_result_by_xpath(dl_result, trans_id, "tid")
                    self._set_result_by_xpath(dl_result, Regexper.clean_str([","], trans_status).strip(),
                                              "status")

                if self.re_sql_start.match(single_line):
                    feed_sql_acumulator = True
                    rsearch = self.re_ip.search(single_line)
                    if rsearch is not None:
                        # user and IP
                        ip = rsearch.group(1)
                        pos = single_line.find(ip)
                        sl = single_line[(pos + len(ip)):].split("[\\s]?")
                        user = sl[0].strip()
                        user = re.split(r'[\s]+', user)
                        self._set_result_by_xpath(dl_result, user[0] + "@" + ip, "uip")

                elif feed_sql_acumulator is True and self.re_sql_end.match(single_line):
                    feed_sql_acumulator = False
                    self._set_result_by_xpath(dl_result, Utils.clear_breaks(sql_acumulator), "query")

                elif feed_sql_acumulator is True and not self.re_sql_end.match(single_line):
                    sql_acumulator += Regexper.clean_white_chars(single_line)

                if self.re_sql_end.match(single_line):
                    feed_msg_acumulator: bool = True
                    msg_acumulator += Regexper.clean_white_chars(single_line)
                elif feed_msg_acumulator is True and self.re_fkey_end.match(single_line):
                    feed_msg_acumulator = False
                    self._set_result_by_xpath(dl_result, msg_acumulator, "do")
                elif feed_msg_acumulator is True and not self.re_fkey_end.match(single_line):
                    msg_acumulator += Regexper.clean_white_chars(single_line)

        self.result_composed = dl_result

        return self.result_composed


class MonitorLatestTransactions(Monitor):
    monitor_tag: str = "TRANSACTIONS"
    LOG_SEPARATOR_REGEXP: str = "MySQL thread(.*[\n|\r|\r\n|\n\r])"

    '''
    RegExp
    '''
    re_ip = re.compile("(([0-9]+\.)+[0-9]+)+", re.MULTILINE)
    re_next_trans = re.compile(".*id ([0-9]+), OS")

    def info__init__(self) -> None:
        """
        info__init__

        Returns:
            None

        """
        super().__init__()
        self.set = None

    def _prepare_result(self) -> List[str]:
        """
        _prepare_result

        Returns:
            List[str]: list

        """
        da_pattern: Dict[str, Any] = {
            "uip": None,  # user 192.0.0.1 [use and IP]
            "trans_id": None,  # 7712234344
            "operation": None,  # Sending data
            "sql_info": None,  # SELECT * FROM abc [query]
            "general_info": None,  # SELECT * FROM abc [query]
        }

        dl_result: List[Dict[str, str]] = []

        if self.log_content is None:
            lc = ""
        else:
            lc = self.log_content

        splitted_log_content = re.compile(self.LOG_SEPARATOR_REGEXP, re.MULTILINE).split(lc)

        log_sql: List[str] = []
        log_general: List[str] = []

        splitted_log_content = splitted_log_content[4:]

        for k in splitted_log_content:

            da = deepcopy(da_pattern)

            k_lines = k.splitlines(False)

            for single_line in k_lines:

                if single_line is None:
                    continue

                if single_line.strip().startswith("---"):
                    continue

                rsearch = self.re_ip.search(single_line)
                if rsearch is not None:
                    # user and IP
                    ip = rsearch.group(1)
                    pos = single_line.find(ip)
                    sl = single_line[pos:]
                    sl = re.split(r'[\s]+', sl)

                    if len(sl) < 2:
                        continue

                    ip = sl[0].strip()
                    user = sl[1].strip()
                    oper = " ".join(sl[2:])

                    da["uip"] = user + "@" + ip
                    da["operation"] = oper

                if self.re_next_trans.match(single_line):

                    tid = self.re_next_trans.search(single_line)
                    tid = tid.groups()[0]
                    da["trans_id"] = tid

                    log_sql = Utils.filter_empty(log_sql)
                    log_general = Utils.filter_empty(log_sql)

                    if len(log_sql) > 2:
                        da["sql_info"] = Utils.clear_breaks(log_sql)
                        da["general_info"] = Utils.clear_breaks(log_general)
                        dl_result.append(da)
                        da = deepcopy(da_pattern)
                    log_sql.clear()
                    log_general.clear()
                    log_general.append(single_line)

                elif not self.re_next_trans.match(single_line):
                    log_sql.append(single_line)
                    log_general.append(single_line)

                else:
                    pass

        self.result_composed = dl_result

        return self.result_composed


class MonitorLog(Monitor):
    monitor_tag: str = "LOG"

    def __init__(self) -> None:
        """
        __init__

        """
        super().__init__()


class MonitorRowOperations(Monitor):
    monitor_tag: str = "ROW OPERATIONS"

    def __init__(self) -> None:
        """
        __init__

        """
        super().__init__()


class MonitorSemaphores(Monitor):
    monitor_tag: str = "SEMAPHORES"

    def __init__(self) -> None:
        """
        __init__

        """
        super().__init__()
