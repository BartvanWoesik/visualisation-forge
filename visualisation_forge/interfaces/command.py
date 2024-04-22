from abc import ABCMeta, abstractmethod


class ICommand(metaclass=ABCMeta):
    """Interface for command structuring"""
    @abstractmethod
    def execute(self, on: any):
        """Executes a command"""
        pass
