import abc

class Parser(object):
    '''Abstract base class for data parsers.

    Parser provides only the functions that resu needs to deserialize data.

    :var format: The format the parser parses.
    :type format: str
    '''

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def format(self):
        raise NotImplementedError

    @abc.abstractmethod
    def load(self, data):
        '''
        Return load data from string.

        :arg data: Serialized data in ``format``.
        :type data: str

        :returns: Deserialized data.
        :rtype: Object.
        '''
        raise NotImplementedError

    @classmethod
    def get_parser(cls, format):
        '''
        Return a parser for a given format.

        :arg format: Name of serialization format the desired parser handles.
        :type format: str

        :returns: Parser class for specified format.
        :rtype: Subclass of :class:`Parser`.
        '''
        for subclass in cls.__subclasses__():
            if format == subclass.format:
                return subclass
