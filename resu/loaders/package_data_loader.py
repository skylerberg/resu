from collections import namedtuple

import pkg_resources

from resu.loaders import Loader

class PackageDataSource(namedtuple('PackageDataSource', ['package', 'path'])):
    '''
    :var package: The name of a package.
    :var path: The path to a file within the package.
    '''
    pass

class PackageDataLoader(Loader):
    '''
    Loads the contents of a file stored in a Python package.

    :var name: ``'package_data'``
    :var source_type: :class:`PackageDataSource`
    :var return_type: ``str``
    '''

    name = 'package_data'
    source_type = PackageDataSource
    return_type = str

    def load(self, source):
        '''
        :arg source: The location of a file within a package.
        :type source: :class:`PackageDataSource`

        :returns: The contents stored in ``source``.
        :rtype: String.
        '''
        return pkg_resources.resource_string(source.package, source.path)
