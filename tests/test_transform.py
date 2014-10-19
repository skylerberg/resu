#pylint: skip-file
import unittest

import mock

import resu
import resu.transform

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
