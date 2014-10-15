#pylint: skip-file
import unittest
import StringIO

import mock

import resu.cli

class test_resu_command(unittest.TestCase):

    def test_no_args(self):
        out = StringIO.StringIO()
        with self.assertRaises(SystemExit):
            resu.cli.resu_command(args=[], out=out)
        output = out.getvalue()
        self.assertEquals(output, resu.cli.RESU_DOC)

    @mock.patch.dict(resu.cli.COMMAND_FUNCTIONS, {'help': mock.MagicMock()})
    def test_valid_args(self):
        resu.cli.resu_command(args=['help'])
        resu.cli.COMMAND_FUNCTIONS['help'].assert_called_once_with([])

    def test_help_option(self):
        out = StringIO.StringIO()
        with self.assertRaises(SystemExit) as cm:
            resu.cli.resu_command(['-h'], out=out)
        output = out.getvalue()
        self.assertEquals(output, resu.cli.RESU_DOC)
        self.assertEquals(cm.exception.code, 0)

    def test_version_option(self):
        out = StringIO.StringIO()
        with self.assertRaises(SystemExit) as cm:
            resu.cli.resu_command(['-v'], out=out)
        output = out.getvalue()
        self.assertEquals(output, resu.__version__ + '\n')
        self.assertEquals(cm.exception.code, 0)

    def test_non_existant_command(self):
        out = StringIO.StringIO()
        with self.assertRaises(SystemExit):
            resu.cli.resu_command(args=['invalid'], out=out)
        output = out.getvalue()
        self.assertEquals(output, resu.cli.RESU_DOC)

    def test_invalid_args(self):
        out = StringIO.StringIO()
        with self.assertRaises(SystemExit):
            resu.cli.resu_command(args=['-z'], out=out)
        output = out.getvalue()
        self.assertEquals(output, resu.cli.RESU_DOC)

class test_init(unittest.TestCase):

    @mock.patch('resu.init')
    def test_no_args(self, mock_init):
        resu.cli.init_command()
        mock_init.assert_called_once_with(directory='.')

    @mock.patch('resu.init')
    def test_directory_option(self, mock_init):
        resu.cli.init_command(['-d', 'home'])
        mock_init.assert_called_once_with(directory='home')

    def test_help_option(self):
        out = StringIO.StringIO()
        with self.assertRaises(SystemExit) as cm:
            resu.cli.init_command(['-h'], out=out)
        output = out.getvalue()
        self.assertEquals(output, resu.cli.INIT_DOC)
        self.assertEquals(cm.exception.code, 0)

    def test_invalid_args(self):
        out = StringIO.StringIO()
        with self.assertRaises(SystemExit) as cm:
            resu.cli.init_command(args=['extra_arg'], out=out)
        output = out.getvalue()
        self.assertEquals(output, resu.cli.INIT_DOC)
        self.assertNotEquals(cm.exception.code, 0)

class test_build(unittest.TestCase):

    @mock.patch('resu.build')
    def test_no_args(self, mock_build):
        resu.cli.build_command()
        mock_build.assert_called_once_with(
            output_file='resume.pdf',
            files=['config.yml', 'resume.yml'])

    @mock.patch('resu.build')
    def test_output_file_option(self, mock_build):
        resu.cli.build_command(['-o', 'resume.html'])
        mock_build.assert_called_once_with(
            output_file='resume.html',
            files=['config.yml', 'resume.yml'])

    def test_help_option(self):
        out = StringIO.StringIO()
        with self.assertRaises(SystemExit) as cm:
            resu.cli.build_command(['-h'], out=out)
        output = out.getvalue()
        self.assertEquals(output, resu.cli.BUILD_DOC)
        self.assertEquals(cm.exception.code, 0)

    def test_invalid_args(self):
        out = StringIO.StringIO()
        with self.assertRaises(SystemExit) as cm:
            resu.cli.build_command(args=['-z'], out=out)
        output = out.getvalue()
        self.assertEquals(output, resu.cli.BUILD_DOC)
        self.assertNotEquals(cm.exception.code, 0)

class test_help(unittest.TestCase):

    def test_no_args(self):
        out = StringIO.StringIO()
        with self.assertRaises(SystemExit) as cm:
            resu.cli.help_command(out=out)
        output = out.getvalue()
        self.assertEquals(output, resu.cli.RESU_DOC)
        self.assertEquals(cm.exception.code, 0)

    def test_command_arg(self):
        out = StringIO.StringIO()
        with self.assertRaises(SystemExit) as cm:
            resu.cli.help_command(args=['init'], out=out)
        output = out.getvalue()
        self.assertEquals(output, resu.cli.INIT_DOC)
        self.assertEquals(cm.exception.code, 0)

    def test_non_existant_command(self):
        out = StringIO.StringIO()
        with self.assertRaises(SystemExit) as cm:
            resu.cli.help_command(args=['xorp'], out=out)
        output = out.getvalue()
        self.assertEquals(output, "Invalid command: 'xorp'")
        self.assertEquals(cm.exception.code, 0)

    def test_invalid_args(self):
        out = StringIO.StringIO()
        with self.assertRaises(SystemExit) as cm:
            resu.cli.help_command(args=['-z'], out=out)
        output = out.getvalue()
        self.assertEquals(output, resu.cli.HELP_DOC)
        self.assertNotEquals(cm.exception.code, 0)
