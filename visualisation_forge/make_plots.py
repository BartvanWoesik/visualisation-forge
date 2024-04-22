import traceback

from interfaces.plots import IPlots
from config_parser import ConfigParser
from plots_controller import CommandControl, MethodCommand


def main(plot_config_path: str | None = None):
    cp = ConfigParser(plot_config_path=plot_config_path)

    commands = {name: [MethodCommand(method=k, **v) for k, v in vals['commands'].items()]
                for name, vals in cp.plots.items()}

    for figure, command_sequence in commands.items():
        try:
            CommandControl.operate_cmd_sequence(obj=IPlots.implementations[figure](**cp.plots[figure]['init_kwargs']),
                                                commands=command_sequence)
        except Exception as e:
            print(f"Failed to create or write {figure} plot. Error: {str(e)},\ntraceback: {traceback.format_exc()}")
