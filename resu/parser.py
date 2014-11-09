'''
An abstract class representating a parser.
'''

import abc

class Parser(object):
    '''Abstract base class for data parsers.

    Parser provides only the functions that resu needs to deserialize data.
    '''

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def format(self):
        '''Specify the format the parser parses.'''
        raise NotImplementedError

    @abc.abstractmethod
    def load(self, data):
        '''Return load data from string.'''
        raise NotImplementedError

    @classmethod
    def get_parser(cls, format):
        '''Return a parser for a given format.'''
        for subclass in cls.__subclasses__():
            if format == subclass.format:
                return subclass
