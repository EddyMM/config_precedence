import unittest

from config_precedence.config_precedence import ConfigPrecedence
from .config_options_impl import (
    EnvVarConfigOption, ConfigFileConfigOption, OnlineConfigOption)


class ConfigPrecedenceTestCase(unittest.TestCase):

    def setUp(self):
        self.config_options = [
            EnvVarConfigOption(1),
            ConfigFileConfigOption(3),
            OnlineConfigOption(2)
        ]

        self.cp = ConfigPrecedence(self.config_options)

    def test_sorting_config_options(self):

        sorted_config_options = self.cp.sorted_config_options(reverse=False)

        self.assertEqual(sorted_config_options[0], self.config_options[0])
        self.assertEqual(sorted_config_options[1], self.config_options[2])
        self.assertEqual(sorted_config_options[2], self.config_options[1])

        sorted_config_options = self.cp.sorted_config_options(reverse=True)

        self.assertEqual(sorted_config_options[0], self.config_options[1])
        self.assertEqual(sorted_config_options[1], self.config_options[2])
        self.assertEqual(sorted_config_options[2], self.config_options[0])

    def test_config_precedence(self):
        self.assertEqual(self.cp.get_config_by_key("A"), 1)
        self.assertEqual(self.cp.get_config_by_key("B"), 2)
        self.assertEqual(self.cp.get_config_by_key("C"), 3)
        self.assertEqual(self.cp.get_config_by_key("F"), 3)
        self.assertEqual(self.cp.get_config_by_key("G"), 1)
