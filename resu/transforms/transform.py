import abc

class Transform(object):
    '''
    Abstract base class for transforms.

    :var name: The name of the transform.
    '''

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def name(self):
        pass

    @abc.abstractmethod
    def apply(self, data):
        '''
        Transform a dictionary of data into a new dictionary.

        :arg data: Data to transform.
        :type data: dict

        :returns: ``data`` after having a tranformation applied to it.
        :rtype: Dictionary.
        '''
        pass
