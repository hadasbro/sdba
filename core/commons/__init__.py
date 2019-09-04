import os
import sys

from core.commons.query_log import QueryLog
from core.commons.static_logger import StaticLogger, log_objects
from core.models.base_model import BaseModel
from core.models.monitors import Monitor


@log_objects.register(Monitor)
def _(*obj: Monitor):
    """
    _

    Args:
        *obj (Monitor): -

    Returns:

    """
    try:
        StaticLogger.log(obj, lambda uobj: print("Loading data for {} section".format(uobj.get_as_string())))
    except Exception as e:
        log_objects(e)


@log_objects.register(BaseModel)
def _(obj: BaseModel):
    """
    _

    Args:
        obj (BaseModel): -

    Returns:

    """
    try:
        StaticLogger.log([obj], lambda uobj: print("Loading section: {}".format(uobj.get_as_string())))
    except Exception as e:
        log_objects(e)


@log_objects.register(Exception)
def _(*obj: Exception):
    """
    _

    Args:
        *obj (Exception):

    Returns:

    """
    try:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        StaticLogger.log(obj, lambda uobj: print("[ Exception/Error ]: " + uobj.__str__(),
                                                 (exc_type, fname, exc_tb.tb_lineno)))
    except Exception as e:
        log_objects(e)


@log_objects.register(QueryLog)
def _(obj: QueryLog):
    """
    _

    Args:
        obj (QueryLog): -

    Returns:

    """
    try:
        StaticLogger.log([obj], lambda uobj: print("[ SQL QUERY ]: " + obj.__str__()))
    except Exception as e:
        log_objects(e)
