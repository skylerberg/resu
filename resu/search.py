# pylint: disable=protected-access
'''
This module provides functions to search for members of subclasses.
'''

from resu.exceptions import FeatureNotFound


def available(class_, id_attr='name'):
    '''
    List all instances or subclasses of a class that.

    :arg class_: The class to find an instance or subclass of.
    :arg id_attr: Attribute used to identify instances or subclasses of a littl
      ``class_``.
    :type class_: Class
    :type id_attr: String
    '''
    ret = list()
    for instance in class_.__dict__.get('instances', []):
        if instance._asdict().get(id_attr, ''):
            ret.append(instance._asdict()[id_attr])
    for subclass in class_.__subclasses__():
        if id_attr in subclass.__dict__:
            ret.append(subclass.__dict__[id_attr])
    return ret


def find(class_, target, id_attr='name'):
    '''
    Find an instance of or a subclass that can be identified by the value of a
    particular attribute of the instance or subclass.

    :arg class_: The class to find an instance or subclass of.
    :arg target: The desired value of the ``id_attr`` for the instance.
    :arg id_attr: Attribute used to identify instances or subclasses of
      ``class_``.
    :type class_: Class
    :type target: Object
    :type id_attr: String

    :returns: An instance or subclass of ``class_`` where
      ``id_attr == target``.
    :rtype: Class or ``class_``

    :raises FeatureNotFound: if there is no class matching the parameters.
    '''
    for instance in class_.__dict__.get('instances', []):
        if instance._asdict().get(id_attr, '') == target:
            return instance
    for subclass in class_.__subclasses__():
        if subclass.__dict__[id_attr] == target:
            return subclass
    raise FeatureNotFound('No {0} with {1} equal to "{2}"'.format(
        class_.__name__,
        id_attr,
        target))
