from pkg_resources import resource_string

from resu.io import Provider


class PackageData(Provider):
    '''
    Reads the contents of files stored in Python packages.

    :var name: ``'package_data'``
    :var return_type: ``str``
    '''

    name = 'package_data'
    return_type = str

    def __init__(self, package, path):
        '''
        :arg package: Package to retrieve file from.
        :arg path: Path to file inside of package.
        :type package: String
        :type path: String
        '''
        self.package = package
        self.path = path

    def read(self):
        '''
        :arg source: The location of a file within a package.
        :type source: :class:`PackageDataSource`

        :returns: The contents stored in ``self.source``.
        :rtype: String
        '''
        return resource_string(self.package, self.path)

    def write(self, content, force=False):
        '''
        :raises IOError: when called. Writing to a Python package is not
          allowed.
        '''
        raise IOError('Cannot write into python package')
