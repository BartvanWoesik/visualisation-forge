from interfaces.command import ICommand


class MethodCommand(ICommand):
    """Class to execute commands on an object"""
    def __init__(self, method: str, *args, **kwargs):
        self.method = method
        self.args = args
        self.kwargs = kwargs

    def execute(self, on: any):
        """Executes the command on the object"""
        getattr(on, self.method)(*self.args, **self.kwargs)


class CommandControl:
    """Implements the execution orchestration of the commands"""
    @staticmethod
    def operate_cmd_sequence(obj: any, commands: list[ICommand]):
        """Executes a list of commands on an object"""
        for command in commands:
            command.execute(obj)

