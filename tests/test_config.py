#pylint: skip-file
import unittest

import mock

import resu
import resu.config

class TestConfig(unittest.TestCase):

    def setUp(self):
        self.mock_get_parser = mock.patch('resu.Parser.get_parser').start()
        self.mock_get_composite_transform = mock.patch('resu.Transform.get_composite_transform').start()
        self.mock_resu_get_template = mock.patch('resu.get_template').start()
        self.config = resu.config.Config()

    def test_get_parser(self):
        self.config.get_parser()
        self.mock_get_parser.assert_called_once_with(resu.config.PARSER_FORMAT)

    def test_get_parser_command_line_arg(self):
        self.config.set_command_line_options({'parser': 'json'})
        self.config.get_parser()
        self.mock_get_parser.assert_called_once_with('json')

    def test_get_data_files(self):
        self.assertEquals(self.config.get_data_files(), resu.config.DATA_FILES)

    def test_get_data_files_command_line_arg(self):
        kwargs = {'data_files': ['resu.yml', 'config.yml']}
        self.config.set_command_line_options(kwargs)
        self.assertEquals(self.config.get_data_files(), ['resu.yml', 'config.yml'])

    def test_get_transform(self):
        self.config.get_transform()
        self.mock_get_composite_transform.assert_called_once_with(())

    def test_get_transform_user_data_options(self):
        kwargs = {'transforms': ['Anonymize']}
        self.config.set_user_data_options(kwargs)
        self.config.get_transform()
        self.mock_get_composite_transform.assert_called_once_with(['Anonymize'])

    def test_get_template_engine(self):
        self.assertEquals(self.config.get_template_engine(), resu.config.TEMPLATE_ENGINE)

    def test_get_template(self):
        self.config.get_template()
        self.mock_resu_get_template.assert_called_once_with()

    def test_get_output_file(self):
        self.assertEquals(self.config.get_output_file(), resu.config.OUTPUT_FILE)

    def test_get_output_file_command_line_options(self):
        kwargs = {'output_file': 'resume.html'}
        self.config.set_command_line_options(kwargs)
        self.assertEquals(self.config.get_output_file(), 'resume.html')

    def test_get_output_file_user_data_options(self):
        kwargs = {'output_file': 'resume.html'}
        self.config.set_user_data_options(kwargs)
        self.assertEquals(self.config.get_output_file(), 'resume.html')

    def tearDown(self):
        mock.patch.stopall()
