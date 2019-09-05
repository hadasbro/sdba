from core.controllers.admin import AdminController
from core.controllers.api import ApiController
from core.controllers.api_mock import ApiMockController


if __name__ == "__main__":
    # mc = ApiController(DBS())

    mc = ApiMockController()
    print(mc.get_monitors())
    print(mc.get_variables())
    print(mc.get_replication_data())
    print(mc.get_overview())
    print(mc.get_performance_schema())
    print(mc.get_info_schema())

    adm = AdminController()
