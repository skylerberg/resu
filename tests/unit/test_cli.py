# pylint: skip-file
import unittest
import StringIO

import mock

import resu.cli


class TestRun(unittest.TestCase):

    def setUp(self):
        self.mock_build = mock.patch('resu.build').start()
        self.mock_get_example = mock.patch('resu.get_example').start()
        self.out = StringIO.StringIO()

    def test_no_args(self):
        resu.cli.run(args=[], out=self.out)
        output = self.out.getvalue()
        self.assertEquals(output, '')
        self.mock_build.assert_called_once()

    def test_alternate_data_file(self):
        resu.cli.run(args='resume.yml', out=self.out)
        output = self.out.getvalue()
        self.assertEquals(output, '')
        self.mock_build.assert_called_once()

    def test_alternate_output_file(self):
        resu.cli.run(args=['-o', 'resu.md'], out=self.out)
        output = self.out.getvalue()
        self.assertEquals(output, '')
        self.mock_build.assert_called_once()

    def test_alternate_parser(self):
        resu.cli.run(args=['-p', 'json'], out=self.out)
        output = self.out.getvalue()
        self.assertEquals(output, '')
        self.mock_build.assert_called_once()

    def test_alternate_template(self):
        resu.cli.run(args=['-t', 'fancy'], out=self.out)
        output = self.out.getvalue()
        self.assertEquals(output, '')
        self.mock_build.assert_called_once()

    def test_help_option(self):
        resu.cli.run(args=['-h'], out=self.out)
        output = self.out.getvalue()
        self.assertEquals(output, resu.cli.CLI_DOC)
        assert not self.mock_build.called

    def test_version_option(self):
        resu.cli.run(args=['-v'], out=self.out)
        output = self.out.getvalue().strip()
        self.assertEquals(output, resu.__version__)
        assert not self.mock_build.called

    def test_generate_option(self):
        resu.cli.run(args=['-g'], out=self.out)
        output = self.out.getvalue()
        self.assertEquals(output, '')
        assert not self.mock_build.called

    def test_invalid_option(self):
        with self.assertRaises(SystemExit) as cm:
            resu.cli.run(args=['-z'], out=self.out)
        self.assertNotEquals(cm.exception.code, 0)
        output = self.out.getvalue()
        self.assertEquals(output, resu.cli.CLI_DOC)
        assert not self.mock_build.called

    def tearDown(self):
        mock.patch.stopall()
