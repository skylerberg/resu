#pylint: skip-file
import unittest

import mock

import resu
import resu.transform
import resu.exceptions

# Subclasses of Transform for testing
class AddTwo(resu.Transform):
    '''Assumes data is an integer and adds 2.'''
    def apply(self, data):
        return data + 2

class MultiplyByTwo(resu.Transform):
    '''Assumes data is an integer and adds 2.'''
    def apply(self, data):
        return data * 2

class test_get_transforms(unittest.TestCase):

    def test_transforms_present(self):
        transforms = resu.Transform.get_transforms()
        assert AddTwo in transforms
        assert MultiplyByTwo in transforms

class test_composite_transform(unittest.TestCase):

    def test_empty_transforms_list(self):
        composite = resu.Transform.get_composite_transform([])
        self.assertEquals(composite, resu.transform._identity)

    def test_unavailable_transform(self):
        with self.assertRaises(resu.exceptions.TransformNotFoundError):
            resu.Transform.get_composite_transform(['xyz'])

    def test_compose_two_transforms(self):
        composite = resu.Transform.get_composite_transform(
            ['AddTwo', 'MultiplyByTwo'])
        self.assertEquals(composite(2), 8)

class test_identity(unittest.TestCase):

    def test_dictionary(self):
        self.assertEquals(
            resu.transform._identity({'one': 1}),
            {'one': 1})

class test_compose(unittest.TestCase):

    def test_simple(self):
        f = lambda x: x + 1
        g = lambda x: x * 0
        fog = resu.transform._compose(f, g)
        self.assertEquals(fog(10), 1)
