from abc import ABCMeta, abstractmethod


class Plots(metaclass=ABCMeta):
    """
    Abstract base class for creating plots.
    """
    implementations: dict[str, callable] = {}

    def __init_subclass__(cls) -> None:
        Plots.implementations[cls.__name__] = cls

    @abstractmethod
    def create_image(self) -> any:
        ...

    @abstractmethod
    def write(self) -> None:
        ...

    def create_and_write(self) -> None:
        """
        Creates the density plot and saves it to a file.
        """
        self.create_image()
        self.write()
