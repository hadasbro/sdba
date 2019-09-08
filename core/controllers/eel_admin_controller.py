from typing import Dict, Any

from core.commons.utils import Utils
from core.controllers import AdminController
from core.exceptions.payload_exception import PayloadException
from core.objects.dbs_credentials import DBSCredentials


def eel_get_databases() -> str:

    try:
        mc = AdminController()
        return mc.get_databases()

    except PayloadException as ex:
        return Utils.dict_to_json(ex.payload)

def eel_add_new_database(data: Dict[str, Any]) -> str:

    try:
        name = data['name']
        host = data['host']
        user = data['user']
        password = data['password']
        port = data['host'] if 'host' in data.keys() else 3306
        type = data['type'] if 'type' in data.keys() else DBSCredentials.TYPE.MYSQL
        ssl = data['ssl'] if 'ssl' in data.keys() else False

        return AdminController.add_new_database(name, host, user, password, port, type, ssl)

    except PayloadException as ex:
        return Utils.dict_to_json(ex.payload)




# result = eel_get_databases()
result = eel_add_new_database({
    'name': "My Great DB 2",
    'host': "localhost",
    'user': "root",
    'password': ""
})


print(result)
