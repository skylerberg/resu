'''
To make it easier to deal with IO, this module defines a set of namedtuples to
specify the location of a resource to read or write.
'''

from collections import namedtuple


class PackageDataSource(namedtuple('PackageDataSource', 'package path')):
    '''
    :var package: The name of a package.
    :var path: The path to a file within the package.
    :type package: String
    :type path: String
    '''
    pass


class FileSource(namedtuple('FileSource', 'path')):
    '''
    :var path: The path to a file on the local filesystem.
    :type path: String
    '''
    pass
