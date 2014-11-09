#pylint: skip-file
import unittest
import StringIO

import mock

import resu
import resu.cli

class test_run(unittest.TestCase):

    def setUp(self):
        self.mock_generate_default = mock.patch('resu.example.generate_default').start()
        self.mock_build = mock.patch('resu.build').start()
        self.out = StringIO.StringIO()

    def test_no_args(self):
        resu.cli.run(args=[], out=self.out)
        output = self.out.getvalue()
        self.assertEquals(output, '')
        assert not self.mock_generate_default.called
        self.mock_build.assert_called_once_with()

    def test_alternate_data_files(self):
        resu.cli.run(args=['config.yml', 'resume.yml'], out=self.out)
        output = self.out.getvalue()
        self.assertEquals(output, '')
        assert not self.mock_generate_default.called
        self.mock_build.assert_called_once_with(
            data_files=['config.yml', 'resume.yml'])

    def test_alternate_output_file(self):
        resu.cli.run(args=['-o', 'resu.md'], out=self.out)
        output = self.out.getvalue()
        self.assertEquals(output, '')
        assert not self.mock_generate_default.called
        self.mock_build.assert_called_once_with(output_file='resu.md')

    def test_alternate_parser(self):
        resu.cli.run(args=['-p', 'json'], out=self.out)
        output = self.out.getvalue()
        self.assertEquals(output, '')
        assert not self.mock_generate_default.called
        self.mock_build.assert_called_once_with(parser='json')

    def test_alternate_template(self):
        resu.cli.run(args=['-t', 'fancy'], out=self.out)
        output = self.out.getvalue()
        self.assertEquals(output, '')
        assert not self.mock_generate_default.called
        self.mock_build.assert_called_once_with(template='fancy')

    def test_help_option(self):
        resu.cli.run(args=['-h'], out=self.out)
        output = self.out.getvalue()
        self.assertEquals(output, resu.cli.CLI_DOC)
        assert not self.mock_generate_default.called
        assert not self.mock_build.called

    def test_version_option(self):
        resu.cli.run(args=['-v'], out=self.out)
        output = self.out.getvalue().strip()
        self.assertEquals(output, resu.__version__)
        assert not self.mock_generate_default.called
        assert not self.mock_build.called

    def test_generate_option(self):
        resu.cli.run(args=['-g'], out=self.out)
        output = self.out.getvalue()
        self.assertEquals(output, '')
        self.mock_generate_default.assertCalled_once_with()
        assert not self.mock_build.called

    def test_invalid_option(self):
        with self.assertRaises(SystemExit) as cm:
            resu.cli.run(args=['-z'], out=self.out)
        self.assertNotEquals(cm.exception.code, 0)
        output = self.out.getvalue()
        self.assertEquals(output, resu.cli.CLI_DOC)
        assert not self.mock_generate_default.called
        assert not self.mock_build.called

    def tearDown(self):
        mock.patch.stopall()
