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

class test_copy_data_dir(unittest.TestCase):

    def setUp(self):
        self.mock_resource_exists = mock.patch('resu.example.pkg_resources.resource_exists').start()
        self.mock_resource_listdir = mock.patch('resu.example.pkg_resources.resource_listdir').start()
        self.mock_resource_listdir.side_effect = lambda a, b: ['foo','bar','baz']
        self.mock_resource_isdir = mock.patch('resu.example.pkg_resources.resource_isdir').start()
        self.mock_resource_isdir.side_effect = lambda *_: False

        self.mock_path_exists = mock.patch('resu.example.os.path.exists').start()
        self.mock_copy_data_file = mock.patch('resu.example._copy_data_file').start()
        self.mock_mkdir = mock.patch('resu.example.os.mkdir').start()

    def test_non_existent_data_dir(self):
        self.mock_resource_exists.return_value = False
        with self.assertRaises(resu.example.MissingPackageDataError):
            resu.example._copy_data_dir('.','dir')

    def test_dir_already_exists(self):
        self.mock_path_exists.return_value = True
        def raise_OSError(*_):
            raise OSError()
        self.mock_mkdir.side_effect = raise_OSError
        resu.example._copy_data_dir('.','dir')

    def test_file_conflict(self):
        def fail_on_foo(target_dir, data_dir, data_file):
            if data_file == 'foo':
                raise resu.example.FileExistsError('dir/foo already exists.')
        self.mock_resource_exists.return_value = True
        self.mock_copy_data_file.side_effect = fail_on_foo
        warnings = resu.example._copy_data_dir('.','dir')
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
        resu.example._copy_data_dir('.','dir')
        assert mock.call('resu', 'dir/foo/spam') in self.mock_resource_isdir.call_args_list

    def test_valid_input(self):
        resu.example._copy_data_dir('.','dir')

    def tearDown(self):
        mock.patch.stopall()

class test_get_template(unittest.TestCase):

    def setUp(self):
        self.mock_resource_exists = mock.patch('resu.example.pkg_resources.resource_exists').start()
        def resource_exists_side_effect(package, resource):
            if resource == resu.example.TEMPLATES_DIR + "/default.html":
                return True
            return False
        self.mock_resource_exists.side_effect = resource_exists_side_effect
        self.mock_resource_string = mock.patch('resu.example.pkg_resources.resource_string').start()

    def test_existant_resource(self):
        resu.example.get_template()
        resource = resu.example.TEMPLATES_DIR + "/default.html"
        self.mock_resource_string.called_once_with('resu', resource)

    def test_non_existant_resource(self):
        with self.assertRaises(resu.example.MissingPackageDataError):
            resu.example.get_template('xyz.html')
        assert not self.mock_resource_string.called

    def tearDown(self):
        mock.patch.stopall()

class test_generate_default(unittest.TestCase):

    @mock.patch('resu.example._copy_data_file')
    def test_valid_input(self, mock_copy_data_file):
        resu.example.generate_default()
        mock_copy_data_file.assert_called_once_with('.', resu.example.DATA_DIR, 'resu.yml')
