from pkg_resources import resource_string

from resu.io import Provider
from resu.io import PackageDataSource


class PackageData(Provider):
    '''
    Reads the contents of files stored in Python packages.

    :var name: ``'package_data'``
    :var source_type: :class:`PackageDataSource`
    :var return_type: ``str``
    '''

    name = 'package_data'
    source_type = PackageDataSource
    return_type = str

    def read(self):
        '''
        :arg source: The location of a file within a package.
        :type source: :class:`PackageDataSource`

        :returns: The contents stored in ``self.source``.
        :rtype: String
        '''
        return resource_string(self.source.package, self.source.path)

    def write(self, content, force=False):
        '''
        :raises IOError: when called. Writing to a Python package is not
          allowed.
        '''
        raise IOError('Cannot write into python package')
