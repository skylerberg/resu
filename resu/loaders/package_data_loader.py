import pkg_resources

from resu.loaders import Loader
from resu.sources import PackageDataSource

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

    def read(self, source):
        '''
        :arg source: The location of a file within a package.
        :type source: :class:`PackageDataSource`

        :returns: The contents stored in ``source``.
        :rtype: String
        '''
        return pkg_resources.resource_string(source.package, source.path)
