from collections import namedtuple

class PackageDataSource(namedtuple('PackageDataSource', ['package', 'path'])):
    '''
    :var package: The name of a package.
    :var path: The path to a file within the package.
    :type package: String
    :type path: String
    '''
    pass
