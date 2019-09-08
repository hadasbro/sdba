from core.commons.decorators import json_response
from core.controllers import ApiMockController
from core.exceptions.payload_exception import PayloadException

@json_response
def eel_mock_get_overview() -> str:
    """
    eel_mock_get_overview

    Returns:
        str
    """
    try:
        mc = ApiMockController()
        return mc.get_overview()
    except PayloadException as ex:
        return ex.payload

@json_response
def eel_mock_get_monitors() -> str:
    """
    eel_mock_get_monitors

    Returns:
        str
    """
    try:
        mc = ApiMockController()
        return mc.get_monitors()
    except PayloadException as ex:
        return ex.payload

@json_response
def eel_mock_get_variables() -> str:
    """
    eel_mock_get_variables

    Returns:
        str
    """
    try:
        mc = ApiMockController()
        return mc.get_variables()
    except PayloadException as ex:
        return ex.payload

@json_response
def eel_mock_get_replication_data() -> str:
    """
    eel_mock_get_replication_data

    Returns:
        str
    """
    try:
        mc = ApiMockController()
        return mc.get_replication_data()
    except PayloadException as ex:
        return ex.payload

@json_response
def eel_mock_get_performance_schema() -> str:
    """
    eel_mock_get_performance_schema
        str
    Returns:

    """
    try:
        mc = ApiMockController()
        return mc.get_performance_schema()
    except PayloadException as ex:
        return ex.payload

@json_response
def eel_mock_get_info_schema() -> str:
    """
    eel_mock_get_info_schema

    Returns:
        str
    """
    try:
        mc = ApiMockController()
        return mc.get_info_schema()
    except PayloadException as ex:
        return ex.payload





result = eel_mock_get_overview()
result = eel_mock_get_monitors()
result = eel_mock_get_variables()
result = eel_mock_get_replication_data()
result = eel_mock_get_performance_schema()
result = eel_mock_get_info_schema()

print(result)
