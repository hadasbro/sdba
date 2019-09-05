from core.commons.dbs import DBS


class AdminController:

    def __init__(self) -> None:
        """
        __init__

        Returns:
            None
        """
        db = None
        self.db = db.connection
        self.dbx = db

    def get_databases(self) -> str:
        pass
