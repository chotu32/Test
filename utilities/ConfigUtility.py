import os
from os.path import dirname

from _pytest import unittest
from properties.p import Property


class ConfigUtility:
    project_root = dirname(dirname(__file__))
    global configPath
    configPath = (os.path.join(project_root, "config.ini"))

    # to load config.ini
    def test_config(self, key):
        prop = Property()
        filepath = prop.load_property_files(configPath)
        prop2 = filepath.__getitem__(key)
        return prop2
