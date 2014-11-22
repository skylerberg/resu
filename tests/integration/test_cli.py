import unittest
import StringIO
import os
import shutil

import resu.cli


class TestGetExample(unittest.TestCase):

    def setUp(self):
        self.out = StringIO.StringIO()
        os.mkdir('/tmp/resu')  # Append uuid
        os.chdir('/tmp/resu')

    def test_basic(self):
        resu.cli.run(args=['-g'], out=self.out)
        assert os.path.isfile('resu.yml')
        self.assertEquals(self.out.getvalue(), '')

    def test_specify_output_file(self):
        resu.cli.run(args=['-g', '-o', 'other.yml'], out=self.out)
        assert os.path.isfile('other.yml')
        self.assertEquals(self.out.getvalue(), '')

    def tearDown(self):
        shutil.rmtree('/tmp/resu')


class TestListAvailable(unittest.TestCase):

    def setUp(self):
        self.out = StringIO.StringIO()

    def test(self):
        resu.cli.run(args=['-l'], out=self.out)
        # Check to make sure some expected strings are included
        output = self.out.getvalue()
        assert 'templates' in output
        assert 'default' in output
