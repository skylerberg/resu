import unittest
import StringIO
import os
import shutil

import resu.cli
from resu.exceptions import FeatureNotFound


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

    def test_generate_twice(self):
        resu.cli.run(args=['-g'], out=self.out)
        with self.assertRaises(IOError):
            resu.cli.run(args=['-g'], out=self.out)

    def tearDown(self):
        shutil.rmtree('/tmp/resu')


class TestListAvailable(unittest.TestCase):

    def test(self):
        self.out = StringIO.StringIO()
        resu.cli.run(args=['-l'], out=self.out)
        # Check to make sure some expected strings are included
        output = self.out.getvalue()
        assert 'templates' in output
        assert 'default' in output


class TestBuild(unittest.TestCase):

    def setUp(self):
        self.out = StringIO.StringIO()
        os.mkdir('/tmp/resu')  # Append uuid
        os.chdir('/tmp/resu')

    def test_basic(self):
        resu.cli.run(args=['-g'], out=self.out)
        resu.cli.run(args=[], out=self.out)
        assert os.path.isfile('resu.html')
        self.assertEquals(self.out.getvalue(), '')

    def test_specify_output_file(self):
        resu.cli.run(args=['-g'], out=self.out)
        resu.cli.run(args=['-o', 'other.html'], out=self.out)
        assert os.path.isfile('other.html')
        self.assertEquals(self.out.getvalue(), '')

    def test_non_existant_parser(self):
        resu.cli.run(args=['-g'], out=self.out)
        with self.assertRaises(FeatureNotFound):
            resu.cli.run(args=['-p', 'gibberish'], out=self.out)
        assert not os.path.isfile('resu.html')

    def tearDown(self):
        shutil.rmtree('/tmp/resu')


class TestExtension(unittest.TestCase):

    def setUp(self):
        extension = '''
from resu.templates import Template
from resu import io

Template(name='test_template',
     source=io.PackageData('resu', 'examples/templates/default.html'),
     example=io.PackageData('resu', 'examples/resu.yml'))
'''
        self.out = StringIO.StringIO()
        os.mkdir('/tmp/resu')  # Append uuid
        os.chdir('/tmp/resu')
        with open('test_template.py', 'w') as f:
            f.write(extension)

    def test_list_extension(self):
        resu.cli.run(args=['-g'], out=self.out)
        resu.cli.run(args=['-l', '-e', 'test_template'], out=self.out)
        output = self.out.getvalue()
        assert 'test_template' in output

    def test_using_template(self):
        resu.cli.run(args=['-g'], out=self.out)
        resu.cli.run(args=['-e', 'test_template', '-t', 'test_template'],
                     out=self.out)
        assert os.path.isfile('resu.html')

    def tearDown(self):
        shutil.rmtree('/tmp/resu')
