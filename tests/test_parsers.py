import mock
import unittest

import resu.parsers

class TestJsonParser(unittest.TestCase):

    def setUp(self):
        self.parser = resu.parsers.JsonParser()
        self.mock_json = mock.patch('resu.parsers.json_parser.json').start()

    def test_load(self):
        self.parser.load("some data")
        self.mock_json.loads.assert_called_once_with("some data")

    def tearDown(self):
        mock.patch.stopall()

class TestYamlParser(unittest.TestCase):

    def setUp(self):
        self.parser = resu.parsers.YamlParser()
        self.mock_yaml = mock.patch('resu.parsers.yaml_parser.yaml').start()

    def test_load(self):
        self.parser.load("some data")
        self.mock_yaml.load.assert_called_once_with("some data")

    def tearDown(self):
        mock.patch.stopall()
