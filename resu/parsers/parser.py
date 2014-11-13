import abc

class Parser(object):
    '''Abstract base class for data parsers.

    Parser provides only the functions that resu needs to deserialize data.

    :var format: The format the parser parses.
    '''

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def format(self):
        pass

    @abc.abstractmethod
    def load(self, data):
        '''
        Return load data from string.

        :arg data: Serialized data in ``format``.
        :type data: str

        :returns: Deserialized data.
        :rtype: Object.
        '''
        pass