from typing import Dict

from core.controllers import ApiMockController, ApiController

print("abc")
# mc = ApiMockController()


def eel_start()  -> Dict[str, str]:
    mc = ApiController()
    return mc.get_overview()


    # mc = ApiMockController()
    # print(mc.get_monitors())
    # print(mc.get_variables())
    # print(mc.get_replication_data())
    # print(mc.get_overview())
    # print(mc.get_performance_schema())
    # print(mc.get_info_schema())



eel_start()
print("abc 2")
