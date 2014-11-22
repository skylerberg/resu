import mock
import unittest

import resu.io


class TestPackageData(unittest.TestCase):

    def setUp(self):
        self.mock_resource_string = mock.patch(
            'resu.io.package_data.resource_string',
            return_value='file contents').start()
        self.package_data = resu.io.PackageData('mod', 'file')

    def test_read(self):
        self.assertEquals(self.package_data.read(), 'file contents')
        self.mock_resource_string.assert_called_once()

    def test_write(self):
        with self.assertRaises(IOError):
            self.package_data.write('content')
        assert not self.mock_resource_string.called

    def tearDown(self):
        mock.patch.stopall()
