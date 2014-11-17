import abc


class Loader(object):
    '''
    Abstract base class for Loaders.

    Loader classes are responsible for fetching external resources.

    For example, if the user is loading a resume off of their local file
    system, then they can use the :class:`resu.loaders.FSLoader` to load their
    files. After these files are loaded, they are ready to be parsed by a
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

    @abc.abstractmethod
    def read(self, source):
        '''
        :returns: The contents stored in ``sources``.
        :rtype: Object

        :raises IOError: if the source cannot be read.
        '''
        pass

    @abc.abstractmethod
    def write(self, source, content, force):
        '''
        :arg source: Information needed to write the content.
        :arg content: Content to write.
        :arg force: Flag to specify whether or not to override existing
          resources.
        :type source: Object
        :type content: Object
        :type force: Boolean

        :returns: None

        :raises IOError: when attempting to write over an existing resource
          while ``force`` is ``False`` or when attempting to write to a
          readonly resource.
        '''
        pass
