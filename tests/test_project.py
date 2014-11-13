#pylint: skip-file
import unittest
import os

import mock
import yaml

import resu.project
import resu.exceptions

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
                raise Exception()
        self.parser.load.side_effect = parser_load_side_effect
        self.mock_merge_dicts = mock.patch('resu.project._merge_dicts').start()


    def test_empty_files_list(self):
        resu.project._combine_data_files([], self.parser)
        assert not self.mock_open.called
        self.mock_merge_dicts.assert_called_once_with([])

    def test_unparsable_file(self):
        with self.assertRaises(Exception):
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

class test_build(unittest.TestCase):
    #TODO(skyler) add tests for build
    pass

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
