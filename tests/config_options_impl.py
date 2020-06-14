from config_precedence.config_option import ConfigOption


class DictConfigMixin:

    def has_config_key(self, key):
        return key in self.configs

    def get_config_by_key(self, key):
        return self.configs[key]


class EnvVarConfigOption(DictConfigMixin, ConfigOption):

    configs = {
        "A": 1,
        "B": 2,
        "C": 3,
    }


class ConfigFileConfigOption(DictConfigMixin, ConfigOption):

    configs = {
        "A": 3,
        "B": 1,
        "C": 2,
    }


class OnlineConfigOption(DictConfigMixin, ConfigOption):

    configs = {
        "A": 2,
        "F": 3,
        "G": 1,
    }
