class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        __call__
        Args:
            *args (): -
            **kwargs (): -

        Returns:
            Singleton: the same object/same instance
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
