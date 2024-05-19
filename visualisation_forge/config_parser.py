import yaml


class ConfigParser:
    def __init__(self, plot_config_path: str):
        with open(plot_config_path, 'r') as config:
            self.config = yaml.safe_load(config.read())

    @property
    def plots(self):
        return self.config['plots']
