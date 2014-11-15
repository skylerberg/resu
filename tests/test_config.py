#pylint: skip-file
import unittest

import resu
import resu.parsers

# Subclasses of Parser for testing
class GibberishParser(resu.parsers.Parser):
    '''Parses gibberish'''
    
    format = 'gibberish'

    def load(self, data):
        pass

class TestConfig(unittest.TestCase):

    def setUp(self):
        self.config = resu.Config()

    def test_get_parser(self):
        self.config.parser = 'gibberish'
        assert isinstance(self.config.get_parser(), GibberishParser)

    def test_get_non_existant_parser(self):
        self.config.parser = 'unknown'
        self.assertEquals(self.config.get_parser(), None)
