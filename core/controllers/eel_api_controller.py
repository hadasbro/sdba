from typing import Any, Dict

from core.commons.decorators import json_response
from core.controllers import ApiController
from core.exceptions.payload_exception import PayloadException


@json_response
def eel_get_overview() -> Dict[str, Any]:
    """
    eel_get_overview

    Returns:
        str
    """
    try:
        mc = ApiController()
        return mc.get_overview()
    except PayloadException as ex:
        return ex.payload


@json_response
def eel_get_monitors() -> Dict[str, Any]:
    """
    eel_get_monitors

    Returns:
        str
    """
    try:
        mc = ApiController()
        return mc.get_monitors()
    except PayloadException as ex:
        return ex.payload


@json_response
def eel_get_variables() -> Dict[str, Any]:
    """
    eel_get_variables

    Returns:
        str
    """
    try:
        mc = ApiController()
        return mc.get_variables()
    except PayloadException as ex:
        return ex.payload


@json_response
def eel_get_replication_data() -> Dict[str, Any]:
    """
    eel_get_replication_data

    Returns:
        str
    """
    try:
        mc = ApiController()
        return mc.get_replication_data()
    except PayloadException as ex:
        return ex.payload


@json_response
def eel_get_performance_schema() -> Dict[str, Any]:
    """
    eel_get_performance_schema
        str
    Returns:

    """
    try:
        mc = ApiController()
        return mc.get_performance_schema()
    except PayloadException as ex:
        return ex.payload


@json_response
def eel_get_info_schema() -> Dict[str, Any]:
    """
    eel_get_info_schema

    Returns:
        str
    """
    try:
        mc = ApiController()
        return mc.get_info_schema()
    except PayloadException as ex:
        return ex.payload


@json_response
def eel_do_test_in_test_db() -> Dict[str, Any]:
    """
    eel_do_test_in_test_db

    Returns:
        str
    """
    try:
        mc = ApiController()
        return mc.selest_from_test_db()
    except PayloadException as ex:
        return ex.payload


result = eel_get_overview()
result = eel_get_monitors()
result = eel_get_variables()
result = eel_get_replication_data()
result = eel_get_performance_schema()
result = eel_get_info_schema()
print(result)
