from abc import ABCMeta, abstractmethod


class Plots(metaclass=ABCMeta):
    _implementations: dict[str, callable] = {}

    @abstractmethod
    def create_image(self, data):
        ...

    @abstractmethod
    def write(self, path):
        ...

    def __init_subclass__(cls) -> None:
        Plots._implementations[cls.__name__] = cls
        return cls