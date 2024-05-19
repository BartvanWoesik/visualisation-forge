import traceback

from interfaces.plots import IPlots
from config_parser import ConfigParser
from plots_controller import CommandControl, MethodCommand


class MakePlots:
    # y_pred: any
    # model: any#callable | None = None

    def __init__(self, x, y, model: callable, plot_config_path: str = "../plot_config.yaml"):
        # if self.y_pred is None:
        self.y_pred = model.predict(x, y)
        # self.

        self.config = ConfigParser(plot_config_path=plot_config_path)
        self.commands = {name: [MethodCommand(method=k, **v) for k, v in vals['commands'].items()]
                         for name, vals in self.config.plots.items()}

    def make(self):
        for figure, command_sequence in self.commands.items():
            try:
                CommandControl.operate_cmd_sequence(
                    obj=IPlots.implementations[figure](**self.config.plots[figure]['init_kwargs']),
                    commands=command_sequence)
            except Exception as e:
                print(f"Failed to create or write {figure} plot. Error: {str(e)},\ntraceback: {traceback.format_exc()}")
