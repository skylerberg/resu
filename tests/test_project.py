#pylint: skip-file
import unittest
import os

from mock import patch, call, MagicMock, Mock
import yaml

import resu.project
import resu.exceptions

class test_copy_data_file(unittest.TestCase):

    def setUp(self):
        self.mock_open = patch('__builtin__.open').start()
        self.mock_path_exists = patch('resu.project.os.path.exists').start()
        self.mock_resource_exists = patch('resu.project.pkg_resources.resource_exists').start()
        self.mock_resource_string = patch('resu.project.pkg_resources.resource_string').start()

    def test_bad_file(self):
        self.mock_resource_exists.return_value = False
        with self.assertRaises(resu.project.MissingPackageDataError):
            resu.project._copy_data_file('.', '.', 'file_name.txt')
        self.assertEquals(self.mock_open.call_count, 0)

    def test_copy_data_file_file_exists(self):
        self.mock_resource_exists.return_value = True
        self.mock_path_exists.return_value = True
        with self.assertRaises(resu.project.FileExistsError):
            resu.project._copy_data_file('.', '.', 'file_name.txt')
        self.assertEquals(self.mock_open.call_count, 0)

    def test_valid_input(self):
        self.mock_resource_exists.return_value = True
        self.mock_path_exists.return_value = False
        directory = '.'
        file_name = 'file_name.txt'
        resu.project._copy_data_file(directory, directory, file_name)
        self.mock_open.called_once_with(os.path.join(directory, file_name), 'w')

    def tearDown(self):
        patch.stopall()

class test_copy_data_dir(unittest.TestCase):

    def setUp(self):
        self.mock_resource_exists = patch('resu.project.pkg_resources.resource_exists').start()
        self.mock_resource_listdir = patch('resu.project.pkg_resources.resource_listdir').start()
        self.mock_resource_listdir.side_effect = lambda a, b: ['foo','bar','baz']
        self.mock_resource_isdir = patch('resu.project.pkg_resources.resource_isdir').start()
        self.mock_resource_isdir.side_effect = lambda *_: False

        self.mock_path_exists = patch('resu.project.os.path.exists').start()
        self.mock_copy_data_file = patch('resu.project._copy_data_file').start()
        self.mock_mkdir = patch('resu.project.os.mkdir').start()

    def test_non_existent_data_dir(self):
        self.mock_resource_exists.return_value = False
        with self.assertRaises(resu.project.MissingPackageDataError):
            resu.project._copy_data_dir('.','dir')

    def test_dir_already_exists(self):
        self.mock_path_exists.return_value = True
        def raise_OSError(*_):
            raise OSError()
        self.mock_mkdir.side_effect = raise_OSError
        resu.project._copy_data_dir('.','dir')

    def test_file_conflict(self):
        def fail_on_foo(target_dir, data_dir, data_file):
            if data_file == 'foo':
                raise resu.project.FileExistsError('dir/foo already exists.')
        self.mock_resource_exists.return_value = True
        self.mock_copy_data_file.side_effect = fail_on_foo
        warnings = resu.project._copy_data_dir('.','dir')
        self.assertEquals(warnings, ['dir/foo already exists.'])

    def test_nested_folders(self):
        def resource_isdir_side_effect(module, resource):
            if resource == 'dir/foo':
                return True
            return False
        def resource_listdir_side_effect(module, resource):
            if resource == 'dir/foo':
                return ['spam','eggs']
            return ['foo','bar','baz']
        self.mock_resource_isdir.side_effect = resource_isdir_side_effect
        self.mock_resource_listdir.side_effect = resource_listdir_side_effect
        resu.project._copy_data_dir('.','dir')
        assert call('resu', 'dir/foo/spam') in self.mock_resource_isdir.call_args_list

    def test_valid_input(self):
        resu.project._copy_data_dir('.','dir')

    def tearDown(self):
        patch.stopall()

class test_init(unittest.TestCase):

    @patch('resu.project._copy_data_dir')
    def test_valid_input(self, mock_copy_data_dir):
        resu.project.init('.')
        mock_copy_data_dir.assert_called_once_with('.', resu.project.DATA_DIR)

class test_combine_yaml_files(unittest.TestCase):

    def setUp(self):
        self.mock_open = patch('resu.project.open', create=True).start()
        self.mock_open = patch('resu.project.open', create=True).start()
        def open_side_effect(file_name, *flags):
            open_file = MagicMock()
            if file_name == 'invalid.yml':
                enter_mock = Mock()
                enter_mock.read.return_value = ": :"
                open_file.__enter__.return_value = enter_mock
            elif file_name == 'a.yml':
                enter_mock = Mock()
                enter_mock.read.return_value = "key: value"
                open_file.__enter__.return_value = enter_mock
            elif file_name == 'b.yml':
                enter_mock = Mock()
                enter_mock.read.return_value = "other: value"
                open_file.__enter__.return_value = enter_mock
            else:
                open_file.__enter__.side_effect = IOError(" [Errno 2] No such file or directory: '{file}'".format(file=file_name))
            return open_file
        self.mock_open.side_effect = open_side_effect

    def test_empty_files_list(self):
        self.assertEquals(None, resu.project._combine_yaml_files([]))

    def test_invalid_yaml(self):
        with self.assertRaises(yaml.parser.ParserError):
            resu.project._combine_yaml_files(['invalid.yml'])

    def test_non_existent_file(self):
        with self.assertRaises(IOError):
            resu.project._combine_yaml_files(['no_such_file.yml'])

    def test_one_file(self):
        yaml = resu.project._combine_yaml_files(['a.yml'])
        self.assertEquals(yaml, {'key': 'value'})

    def test_two_files(self):
        yaml = resu.project._combine_yaml_files(['a.yml', 'b.yml'])
        self.assertEquals(yaml, {'key': 'value', 'other': 'value'})

    def tearDown(self):
        patch.stopall()
