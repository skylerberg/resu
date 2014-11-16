import abc

class Parser(object):
    '''Abstract base class for data parsers.

    Parser provides only the functions that resu needs to deserialize data.

    :var name: The format the parser parses.
    '''

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def name(self):
        pass

    @abc.abstractmethod
    def load(self, data):
        '''
        Return load data from string.

        :arg data: Serialized data in ``format``.
        :type data: String

        :returns: Deserialized data.
        :rtype: Object
        '''
        pass
