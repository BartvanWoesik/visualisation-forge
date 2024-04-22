import traceback

from visualisation_forge.interfaces import Plots
from config_parser import ConfigParser
from make_orchestrator import CommandControl, MethodCommand


def main(plot_config_path: str | None = None):
    cp = ConfigParser(plot_config_path=plot_config_path)

    commands = {name: [MethodCommand(method=k, **v) for k, v in vals['commands'].items()]
                for name, vals in cp.plots.items()}

    for figure, command_sequence in commands.items():
        try:
            CommandControl.operate_cmd_sequence(obj=Plots.implementations[figure](**cp.plots[figure]['init_kwargs']),
                                                commands=command_sequence)
        except Exception as e:
            print(f"Failed to create or write {figure} plot. Error: {str(e)},\ntraceback: {traceback.format_exc()}")


if __name__ == "__main__":
    main()
