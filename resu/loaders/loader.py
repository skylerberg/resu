import abc

class Loader(object):
    '''
    Abstract base class for Loaders.

    Loader classes are responsible for fetching external resources.

    For example, if the user is loading a resume off of their local file system,
    then they can use the :class:`resu.loaders.FSLoader` to load their files.
    After these files are loaded, they are ready to be parsed by a
    :class:`resu.Parser`.
    '''

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def source_type(self):
        pass

    @abc.abstractproperty
    def return_type(self):
        pass

    @abc.abstractmethod
    def load(self, sources):
        '''
        :returns: The contents stored in ``sources``.
        :rtype: Object.
        '''
        pass
