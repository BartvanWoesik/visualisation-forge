from abc import ABCMeta, abstractmethod


class Plots(metaclass=ABCMeta):
    """
    Abstract base class for creating plots.
    """

    _implementations: dict[str, callable] = {}

    @abstractmethod
    def create_image(self):
        ...

    @abstractmethod
    def write(self):
        ...

    def create_and_write(self):
        """
        Creates the density plot and saves it to a file.
        """
        self.create_image()
        self.write()

    def __init_subclass__(cls) -> None:
        Plots._implementations[cls.__name__] = cls
        return cls
