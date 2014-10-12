#pylint: skip-file
import unittest
from StringIO import StringIO

from mock import patch, MagicMock

from resu import cli

class test_resu_command(unittest.TestCase):

    def test_no_args(self):
        out = StringIO()
        with self.assertRaises(SystemExit):
            cli.resu_command(args=[], out=out)
        output = out.getvalue()
        self.assertEquals(output, cli.RESU_DOC)

    @patch.dict(cli.COMMAND_FUNCTIONS, {'help': MagicMock()})
    def test_valid_args(self):
        cli.resu_command(args=['help'])
        cli.COMMAND_FUNCTIONS['help'].assert_called_once_with([])

    def test_help_option(self):
        out = StringIO()
        with self.assertRaises(SystemExit) as cm:
            cli.resu_command(['-h'], out=out)
        output = out.getvalue()
        self.assertEquals(output, cli.RESU_DOC)
        self.assertEquals(cm.exception.code, 0)

    def test_version_option(self):
        out = StringIO()
        with self.assertRaises(SystemExit) as cm:
            cli.resu_command(['-v'], out=out)
        output = out.getvalue()
        self.assertEquals(output, cli.__version__ + '\n')
        self.assertEquals(cm.exception.code, 0)

    def test_non_existant_command(self):
        out = StringIO()
        with self.assertRaises(SystemExit):
            cli.resu_command(args=['invalid'], out=out)
        output = out.getvalue()
        self.assertEquals(output, cli.RESU_DOC)

    def test_invalid_args(self):
        out = StringIO()
        with self.assertRaises(SystemExit):
            cli.resu_command(args=['-z'], out=out)
        output = out.getvalue()
        self.assertEquals(output, cli.RESU_DOC)

class test_init(unittest.TestCase):

    @patch('resu.cli.init')
    def test_no_args(self, mock_init):
        cli.init_command()
        mock_init.assert_called_once_with(directory='.')

    @patch('resu.cli.init')
    def test_directory_option(self, mock_init):
        cli.init_command(['-d', 'home'])
        mock_init.assert_called_once_with(directory='home')

    def test_help_option(self):
        out = StringIO()
        with self.assertRaises(SystemExit) as cm:
            cli.init_command(['-h'], out=out)
        output = out.getvalue()
        self.assertEquals(output, cli.INIT_DOC)
        self.assertEquals(cm.exception.code, 0)

    def test_invalid_args(self):
        out = StringIO()
        with self.assertRaises(SystemExit) as cm:
            cli.init_command(args=['extra_arg'], out=out)
        output = out.getvalue()
        self.assertEquals(output, cli.INIT_DOC)
        self.assertNotEquals(cm.exception.code, 0)

class test_build(unittest.TestCase):

    @patch('resu.cli.build')
    def test_no_args(self, mock_build):
        cli.build_command()
        mock_build.assert_called_once_with(
            output_file='resume.pdf',
            files=['config.yml', 'resume.yml'])

    @patch('resu.cli.build')
    def test_output_file_option(self, mock_build):
        cli.build_command(['-o', 'resume.html'])
        mock_build.assert_called_once_with(
            output_file='resume.html',
            files=['config.yml', 'resume.yml'])

    def test_help_option(self):
        out = StringIO()
        with self.assertRaises(SystemExit) as cm:
            cli.build_command(['-h'], out=out)
        output = out.getvalue()
        self.assertEquals(output, cli.BUILD_DOC)
        self.assertEquals(cm.exception.code, 0)

    def test_invalid_args(self):
        out = StringIO()
        with self.assertRaises(SystemExit) as cm:
            cli.build_command(args=['-z'], out=out)
        output = out.getvalue()
        self.assertEquals(output, cli.BUILD_DOC)
        self.assertNotEquals(cm.exception.code, 0)

class test_help(unittest.TestCase):

    def test_no_args(self):
        out = StringIO()
        with self.assertRaises(SystemExit) as cm:
            cli.help_command(out=out)
        output = out.getvalue()
        self.assertEquals(output, cli.RESU_DOC)
        self.assertEquals(cm.exception.code, 0)

    def test_command_arg(self):
        out = StringIO()
        with self.assertRaises(SystemExit) as cm:
            cli.help_command(args=['init'], out=out)
        output = out.getvalue()
        self.assertEquals(output, cli.INIT_DOC)
        self.assertEquals(cm.exception.code, 0)

    def test_non_existant_command(self):
        out = StringIO()
        with self.assertRaises(SystemExit) as cm:
            cli.help_command(args=['xorp'], out=out)
        output = out.getvalue()
        self.assertEquals(output, "Invalid command: 'xorp'")
        self.assertEquals(cm.exception.code, 0)

    def test_invalid_args(self):
        out = StringIO()
        with self.assertRaises(SystemExit) as cm:
            cli.help_command(args=['-z'], out=out)
        output = out.getvalue()
        self.assertEquals(output, cli.HELP_DOC)
        self.assertNotEquals(cm.exception.code, 0)
