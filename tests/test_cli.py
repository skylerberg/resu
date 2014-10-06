#pylint: skip-file
import unittest
from StringIO import StringIO

from mock import patch

from pyres import cli

class test_pyres_command(unittest.TestCase):

    def test_no_args(self):
        out = StringIO()
        with self.assertRaises(SystemExit):
            cli.pyres_command(args=[], out=out)
        output = out.getvalue()
        self.assertEquals(output, cli.PYRES_DOC)

    def test_valid_args(self):
        cli.pyres_command(args=['help'])

    def test_invalid_args(self):
        out = StringIO()
        with self.assertRaises(SystemExit):
            cli.pyres_command(args=['invalid'], out=out)
        output = out.getvalue()
        self.assertEquals(output, cli.PYRES_DOC)

class test_init(unittest.TestCase):

    @patch('pyres.cli.init')
    def test_no_args(self, mock_init):
        cli.init_command()
        mock_init.assert_called_once_with(directory='.')

    @patch('pyres.cli.init')
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
