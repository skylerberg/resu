#pylint: skip-file
import unittest

import resu.parsers

# Subclasses of Parser for testing
class GibberishParser(resu.parsers.Parser):
    '''Parses gibberish'''
    
    format = 'gibberish'

    def load(self, data):
        pass

class test_get_parser(unittest.TestCase):

    def test_get_parser(self):
        self.assertEquals(resu.parsers.Parser.get_parser('gibberish'), GibberishParser)

    def test_get_non_existant_parser(self):
        self.assertEquals(resu.parsers.Parser.get_parser('unknown'), None)
