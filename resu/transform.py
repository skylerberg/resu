'''Definition of Transform abstract base class.'''

import abc

from resu.exceptions import TransformNotFoundError

class Transform(object):
    '''Abstract base class for transforms.'''

    __metaclass__ = abc.ABCMeta

    @classmethod
    def get_transforms(cls):
        '''Return a list all available transforms.'''
        return cls.__subclasses__()

    @classmethod
    def get_composite_transform(cls, transforms):
        '''
        Return a function composed of the application of each transforms each
        transfrom from a given list.

        Running the composite function returned by this function is the
        equivalent of running each transform in the same order supplied.
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
        '''Transform a dictionary of data into a new dictionary.'''
        raise NotImplementedError

def _identity(data):
    '''The single argument identity function.'''
    return data

def _compose(f, g):
    '''Return the composition of two functions taking a single argument.'''
    return lambda data: f(g(data))
