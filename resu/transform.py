import abc

from resu.exceptions import TransformNotFoundError

class Transform(object):
    '''
    Abstract base class for transforms.
    '''

    __metaclass__ = abc.ABCMeta

    @classmethod
    def get_transforms(cls):
        '''
        Get a list all available transforms.

        :returns: All subclasses of :class:`Transform`.
        :rtype: List of subclasses of :class:`Transform`.
        '''
        return cls.__subclasses__()

    @classmethod
    def get_composite_transform(cls, transforms):
        '''
        Running the composite function returned by this function is the
        equivalent of running each transform in the same order supplied.

        :arg transforms: An ordered list of names of transforms.
        :type transforms: [str]

        :returns: A function composed of the application of each transform given.
        :rtype: Function.
        '''
        transform_lookup = {}
        for transform in cls.get_transforms():
            transform_lookup[transform.__name__] = transform()
        composite = _identity
        for transform_name in transforms:
            if not transform_name in transform_lookup:
                raise TransformNotFoundError(
                    "{transform} not found.".format(transform=transform_name))
            transform = transform_lookup[transform_name]
            composite = _compose(transform.apply, composite)
        return composite

    @abc.abstractmethod
    def apply(self, data):
        '''
        Transform a dictionary of data into a new dictionary.

        :arg data: Data to transform.
        :type data: dict

        :returns: ``data`` after having a tranformation applied to it.
        :rtype: Dictionary.
        '''
        raise NotImplementedError

def _identity(data):
    '''
    The single argument identity function.
    '''
    return data

def _compose(f, g):
    '''
    Return the composition of two functions taking a single argument.
    '''
    return lambda data: f(g(data))
