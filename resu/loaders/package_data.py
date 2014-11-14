from collections import namedtuple

import pkg_resources

from resu.loaders import Loader

class PackageData(Loader):
    '''
    '''

    return_type = str

    def load(self, source):
        '''
        :arg source: 
        :type source: :class:`PackageDataSource`

        :returns: The contents stored in ``source``.
        :rtype: String.
        '''
        return pkg_resources.resource_string(source.package, source.path)

class PackageDataSource(namedtuple('PackageDataSource', 'package path')):
    '''
    '''
    pass
