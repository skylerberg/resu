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

    def test(self):
        resu.cli.run(args=['-g'], out=self.out)
        assert os.path.isfile('resu.yml')

    def tearDown(self):
        shutil.rmtree('/tmp/resu')
