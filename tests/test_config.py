#pylint: skip-file
import unittest

import resu
import resu.parsers
import resu.transforms

# Subclasses of Parser for testing
class GibberishParser(resu.parsers.Parser):
    '''Parses gibberish'''
    
    format = 'gibberish'

    def load(self, data):
        pass

# Subclasses of Transform for testing
class AddTwo(resu.transforms.Transform):
    '''Assumes data is an integer and adds 2.'''

    name = 'add-two'

    def apply(self, data):
        return data + 2

class MultiplyByTwo(resu.transforms.Transform):
    '''Assumes data is an integer and adds 2.'''

    name = 'multiply-by-two'

    def apply(self, data):
        return data * 2


class TestConfig(unittest.TestCase):

    def setUp(self):
        self.config = resu.Config()

    def test_get_parser(self):
        self.config.parser_format = 'gibberish'
        assert isinstance(self.config.get_parser(), GibberishParser)

    def test_get_non_existant_parser(self):
        self.config.parser_format = 'unknown'
        self.assertEquals(self.config.get_parser(), None)

    def test_empty_transforms_list(self):
        composite = self.config.get_transform()
        self.assertEquals(composite, resu.config._identity)

    def test_compose_two_transforms(self):
        self.config.transforms = ['add-two', 'multiply-by-two']
        composite = self.config.get_transform()
        self.assertEquals(composite(2), 8)

class test_identity(unittest.TestCase):

    def test_dictionary(self):
        self.assertEquals(
            resu.config._identity({'one': 1}),
            {'one': 1})

class test_compose(unittest.TestCase):

    def test_simple(self):
        f = lambda x: x + 1
        g = lambda x: x * 0
        fog = resu.config._compose(f, g)
        self.assertEquals(fog(10), 1)
