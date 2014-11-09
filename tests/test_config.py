#pylint: skip-file
import unittest

import mock

import resu
import resu.config

class TestConfig(unittest.TestCase):

    def setUp(self):
        self.mock_get_parser  = mock.patch('resu.Parser.get_parser').start()
        self.config = resu.config.Config()

    def test_get_parser_no_args(self):
        self.config.get_parser()
        self.mock_get_parser.assert_called_once_with(resu.config.DATA_PARSER_FORMAT)

    def test_get_parser_command_line_arg(self):
        self.config.set_command_line_options({'parser': 'json'})
        self.config.get_parser()
        self.mock_get_parser.assert_called_once_with('json')

    def tearDown(self):
        mock.patch.stopall()
