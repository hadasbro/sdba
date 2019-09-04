from core.commons.dbs import DBS


class AdminController:

    def __init__(self, db: DBS) -> None:
        """
        __init__

        Args:
            db (DBS): -

        Returns:
            None
        """
        self.db = db.connection
        self.dbx = db

    def get_databases(self) -> str:
        pass
