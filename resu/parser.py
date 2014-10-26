'''
An abstract class representating a parser.
'''

import abc

class DataParser(object):
    '''Abstract base class for data parsers.

    DataParser provides only the functions that resu needs to deserialize data.
    '''

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def load(self, data):
        '''Return load data from string.'''
        raise NotImplementedError