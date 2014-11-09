#pylint: skip-file
import unittest

import resu

# Subclasses of Parser for testing
class GibberishParser(resu.Parser):
    '''Parses gibberish'''
    
    format = 'gibberish'

    def load(self, data):
        pass

class test_get_parser(unittest.TestCase):

    def test_get_parser(self):
        self.assertEquals(resu.Parser.get_parser('gibberish'), GibberishParser)

    def test_get_non_existant_parser(self):
        self.assertEquals(resu.Parser.get_parser('unknown'), None)
