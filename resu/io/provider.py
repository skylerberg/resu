import abc


class Provider(object):
    '''
    Abstract base class for for IO providers.

    Providers are responsible for fetching and writing resources.

    For example, if the user is loading a resume off of their local file
    system, then they can use the :class:`resu.io.File` to read their files.
    After these files are read, they are ready to be parsed by a
    :class:`resu.Parser`.
    '''

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def name(self):  # pylint: disable=missing-docstring
        pass

    @abc.abstractproperty
    def source_type(self):  # pylint: disable=missing-docstring
        pass

    @abc.abstractproperty
    def return_type(self):  # pylint: disable=missing-docstring
        pass

    def __init__(self, source):
        self.source = source

    @abc.abstractmethod
    def read(self):
        '''
        :returns: The contents stored in ``self.source``.
        :rtype: Object

        :raises IOError: if the source cannot be read.
        '''
        pass

    @abc.abstractmethod
    def write(self, content, force):
        '''
        :arg content: Content to write.
        :arg force: Flag to specify whether or not to override existing
          resources.
        :type content: Object
        :type force: Boolean

        :returns: None

        :raises IOError: when attempting to write over an existing resource
          while ``force`` is ``False`` or when attempting to write to a
          readonly resource.
        '''
        pass
