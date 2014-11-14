#pylint: skip-file
import unittest
import os

import mock
import yaml

import resu.example
import resu.exceptions

class test_copy_data_file(unittest.TestCase):

    def setUp(self):
        self.mock_open = mock.patch('__builtin__.open').start()
        self.mock_path_exists = mock.patch('resu.example.os.path.exists').start()
        self.mock_resource_exists = mock.patch('resu.example.pkg_resources.resource_exists').start()
        self.mock_resource_string = mock.patch('resu.example.pkg_resources.resource_string').start()

    def test_bad_file(self):
        self.mock_resource_exists.return_value = False
        with self.assertRaises(resu.example.MissingPackageDataError):
            resu.example._copy_data_file('.', '.', 'file_name.txt')
        self.assertEquals(self.mock_open.call_count, 0)

    def test_copy_data_file_file_exists(self):
        self.mock_resource_exists.return_value = True
        self.mock_path_exists.return_value = True
        with self.assertRaises(resu.example.FileExistsError):
            resu.example._copy_data_file('.', '.', 'file_name.txt')
        self.assertEquals(self.mock_open.call_count, 0)

    def test_valid_input(self):
        self.mock_resource_exists.return_value = True
        self.mock_path_exists.return_value = False
        directory = '.'
        file_name = 'file_name.txt'
        resu.example._copy_data_file(directory, directory, file_name)
        self.mock_open.called_once_with(os.path.join(directory, file_name), 'w')

    def tearDown(self):
        mock.patch.stopall()

class test_generate_default(unittest.TestCase):

    @mock.patch('resu.example._copy_data_file')
    def test_valid_input(self, mock_copy_data_file):
        resu.example.generate_default()
        mock_copy_data_file.assert_called_once_with('.', resu.example.DATA_DIR, 'resu.yml')
