from typing import Dict, Any

from core.commons.decorators import json_response
from core.controllers import AdminController
from core.exceptions.payload_exception import PayloadException
from core.objects.dbs_credentials import DBSCredentials


@json_response
def eel_get_databases() -> str:
    try:
        mc = AdminController()
        return mc.get_databases()

    except PayloadException as ex:
        return ex.payload


@json_response
def eel_add_new_database(data: Dict[str, Any]) -> str:
    try:
        name = data['name'] if 'name' in data.keys() else ""
        host = data['host'] if 'host' in data.keys() else ""
        user = data['user'] if 'user' in data.keys() else ""
        password = data['password'] if 'password' in data.keys() else ""
        port = data['port'] if 'port' in data.keys() else 3306
        type = data['type'] if 'type' in data.keys() else DBSCredentials.TYPE.MYSQL
        ssl = data['ssl'] if 'ssl' in data.keys() else False

        return AdminController().add_new_database(name, host, user, password, port, type, ssl)

    except PayloadException as ex:
        return ex.payload


# result = eel_get_databases()
result = eel_add_new_database({
    'name': "My Great DB 5",
    'host': "127.0.0.1",
    'user': "test",
    'password': "test"
})
print(result)
