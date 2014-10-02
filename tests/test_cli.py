import unittest
from StringIO import StringIO


from pyres import cli

class test_pyres(unittest.TestCase):

    def test_no_args(self):
        out = StringIO()
        with self.assertRaises(SystemExit):
            cli.pyres(args=[], out=out)
        output = out.getvalue()
        self.assertEquals(output, cli.PYRES_DOC)

    def test_valid_command(self):
        cli.pyres(args=['init'])

    def test_invalid_command(self):
        out = StringIO()
        with self.assertRaises(SystemExit):
            cli.pyres(args=['invalid'], out=out)
        output = out.getvalue()
        self.assertEquals(output, cli.PYRES_DOC)
