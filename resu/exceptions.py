'''
Resu favors using exceptions from built into Python when there already exists
an appropriately named exception. For example, Resu will raise an IOError when
asked to write data into an installed Python package, see
:class:`resu.io.PackageData`. This module contains all exceptions that Resu
needs to raise that are not included in Python.
'''


class FeatureNotFound(Exception):
    '''
    This exception should be raised whenever there is an attempt to access a
    feature that does not exist in Resu. Examples include trying to find a
    :class:`resu.parsers.Parser` to parse an unsupported format like ini, or
    trying to find a :class:`resu.io.Provider` to save a document into a SQL
    database.
    '''
    pass
