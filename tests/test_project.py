#pylint: skip-file
import unittest
import os

import mock
import yaml

import resu.project
import resu.exceptions

class test_copy_data_file(unittest.TestCase):

    def setUp(self):
        self.mock_open = mock.patch('__builtin__.open').start()
        self.mock_path_exists = mock.patch('resu.project.os.path.exists').start()
        self.mock_resource_exists = mock.patch('resu.project.pkg_resources.resource_exists').start()
        self.mock_resource_string = mock.patch('resu.project.pkg_resources.resource_string').start()

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
        mock.patch.stopall()

class test_copy_data_dir(unittest.TestCase):

    def setUp(self):
        self.mock_resource_exists = mock.patch('resu.project.pkg_resources.resource_exists').start()
        self.mock_resource_listdir = mock.patch('resu.project.pkg_resources.resource_listdir').start()
        self.mock_resource_listdir.side_effect = lambda a, b: ['foo','bar','baz']
        self.mock_resource_isdir = mock.patch('resu.project.pkg_resources.resource_isdir').start()
        self.mock_resource_isdir.side_effect = lambda *_: False

        self.mock_path_exists = mock.patch('resu.project.os.path.exists').start()
        self.mock_copy_data_file = mock.patch('resu.project._copy_data_file').start()
        self.mock_mkdir = mock.patch('resu.project.os.mkdir').start()

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
        assert mock.call('resu', 'dir/foo/spam') in self.mock_resource_isdir.call_args_list

    def test_valid_input(self):
        resu.project._copy_data_dir('.','dir')

    def tearDown(self):
        mock.patch.stopall()

class test_combine_data_files(unittest.TestCase):

    def setUp(self):
        self.mock_open = mock.patch('resu.project.open', create=True).start()
        self.mock_open = mock.patch('resu.project.open', create=True).start()

        def open_side_effect(file_name, *flags):
            open_file = mock.MagicMock()
            if file_name == 'invalid.yml':
                enter_mock = mock.Mock()
                enter_mock.read.return_value = ": :"
                open_file.__enter__.return_value = enter_mock
            elif file_name == 'a.yml':
                enter_mock = mock.Mock()
                enter_mock.read.return_value = "1: a"
                open_file.__enter__.return_value = enter_mock
            elif file_name == 'b.yml':
                enter_mock = mock.Mock()
                enter_mock.read.return_value = "2: b"
                open_file.__enter__.return_value = enter_mock
            else:
                open_file.__enter__.side_effect = IOError(" [Errno 2] No such file or directory: '{file}'".format(file=file_name))
            return open_file

        self.mock_open.side_effect = open_side_effect
        self.parser = mock.Mock()
        def parser_load_side_effect(data):
            if data == '1: a':
                return {'1': 'a'}
            elif data == '2: b':
                return {'2': 'b'}
            else:
                raise resu.exceptions.ParserError()
        self.parser.load.side_effect = parser_load_side_effect
        self.mock_merge_dicts = mock.patch('resu.project._merge_dicts').start()


    def test_empty_files_list(self):
        resu.project._combine_data_files([], self.parser)
        assert not self.mock_open.called
        self.mock_merge_dicts.assert_called_once_with([])

    def test_unparsable_file(self):
        with self.assertRaises(resu.exceptions.ParserError):
            resu.project._combine_data_files(['invalid.yml'], self.parser)

    def test_non_existent_file(self):
        with self.assertRaises(IOError):
            resu.project._combine_data_files(['no_such_file.yml'], self.parser)

    def test_one_file(self):
        data = resu.project._combine_data_files(['a.yml'], self.parser)
        self.mock_open.assert_called_once_with('a.yml')
        self.mock_merge_dicts.called_once_with([{'1': 'a'}])

    def test_two_files(self):
        data = resu.project._combine_data_files(['a.yml', 'b.yml'], self.parser)
        self.mock_open.assert_has_calls([mock.call('a.yml'), mock.call('b.yml')])
        self.mock_merge_dicts.called_once_with([{'1': 'a'}, {'2': 'b'}])

    def tearDown(self):
        mock.patch.stopall()

class test_get_template(unittest.TestCase):
    #TODO(skyler) add tests for _get_template

    def setUp(self):
        self.mock_resource_exists = mock.patch('resu.project.pkg_resources.resource_exists').start()
        def resource_exists_side_effect(package, resource):
            if resource == resu.project.TEMPLATES_DIR + "/default.html":
                return True
            return False
        self.mock_resource_exists.side_effect = resource_exists_side_effect
        self.mock_resource_string = mock.patch('resu.project.pkg_resources.resource_string').start()

    def test_existant_resource(self):
        resu.project._get_template()
        resource = resu.project.TEMPLATES_DIR + "/default.html"
        self.mock_resource_string.called_once_with('resu', resource)

    def test_non_existant_resource(self):
        with self.assertRaises(resu.project.MissingPackageDataError):
            resu.project._get_template('xyz.html')
        assert not self.mock_resource_string.called

    def tearDown(self):
        mock.patch.stopall()

class test_build(unittest.TestCase):
    #TODO(skyler) add tests for build
    pass

class test_apply_transforms(unittest.TestCase):

    @mock.patch('resu.Transform.get_composite_transform')
    def test_valid_input(self, mock_get_composite_transform):
        composite = mock.Mock()
        mock_get_composite_transform.return_value = composite
        transforms = []
        data = {}
        resu.project._apply_transforms(transforms, data)
        mock_get_composite_transform.assert_called_once_with(transforms)
        composite.assert_called_once_with(data)

class test_generate_default(unittest.TestCase):

    @mock.patch('resu.project._copy_data_file')
    def test_valid_input(self, mock_copy_data_file):
        resu.project.generate_default()
        mock_copy_data_file.assert_called_once_with('.', resu.project.DATA_DIR, 'resu.yml')

class test_merge_dicts(unittest.TestCase):

    def test_simple(self):
        dicts = [
            {'1': 'a'}, 
            {'2': 'b'}]
        self.assertEquals(resu.project._merge_dicts(dicts),
            {'1': 'a', '2': 'b'})

    def test_recursive_dicts(self):
        dicts = [
            {'1': {'2': 'b'}}, 
            {'1': {'3': 'c'}}]
        self.assertEquals(resu.project._merge_dicts(dicts),
            {'1': {'2': 'b', '3': 'c'}})

    def test_merge_lists(self):
        dicts = [
            {'1': ['a']}, 
            {'1': ['b']}]
        self.assertEquals(resu.project._merge_dicts(dicts),
            {'1': ['a', 'b']})

    def test_list_and_dict(self):
        dicts = [
            {'1': {'2': 'b'}}, 
            {'1': ['b']}]
        with self.assertRaises(resu.exceptions.DataMergeError):
            resu.project._merge_dicts(dicts)

    def test_conflicting_keys(self):
        dicts = [
            {'1': 'a'}, 
            {'1': 'b'}]
        with self.assertRaises(resu.exceptions.DataMergeError):
            resu.project._merge_dicts(dicts)
