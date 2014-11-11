#pylint: skip-file
import unittest

import mock

import resu
import resu.transforms
import resu.exceptions
from resu.transforms import Transform

# Subclasses of Transform for testing
class AddTwo(Transform):
    '''Assumes data is an integer and adds 2.'''
    def apply(self, data):
        return data + 2

class MultiplyByTwo(Transform):
    '''Assumes data is an integer and adds 2.'''
    def apply(self, data):
        return data * 2

class test_get_transforms(unittest.TestCase):

    def test_transforms_present(self):
        transforms = Transform.get_transforms()
        assert AddTwo in transforms
        assert MultiplyByTwo in transforms

class test_composite_transform(unittest.TestCase):

    def test_empty_transforms_list(self):
        composite = Transform.get_composite_transform([])
        self.assertEquals(composite, resu.transforms.transform._identity)

    def test_unavailable_transform(self):
        with self.assertRaises(resu.exceptions.TransformNotFoundError):
            Transform.get_composite_transform(['xyz'])

    def test_compose_two_transforms(self):
        composite = Transform.get_composite_transform(
            ['AddTwo', 'MultiplyByTwo'])
        self.assertEquals(composite(2), 8)

class test_identity(unittest.TestCase):

    def test_dictionary(self):
        self.assertEquals(
            resu.transforms.transform._identity({'one': 1}),
            {'one': 1})

class test_compose(unittest.TestCase):

    def test_simple(self):
        f = lambda x: x + 1
        g = lambda x: x * 0
        fog = resu.transforms.transform._compose(f, g)
        self.assertEquals(fog(10), 1)
