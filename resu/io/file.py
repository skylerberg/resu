import os

from resu.io import Provider
from resu.sources import FileSource


class File(Provider):
    '''
    Read and write to a file on the local file system.

    :var name: ``file``
    :var source_type: ``str``
    :var return_type: ``str``
    '''

    name = 'file'
    source_type = FileSource
    return_type = str

    def read(self):
        '''
        :returns: Contents of the file specified in ``self.source``.
        :rtype: String

        :raises IOError: if the file does not exist.
        '''
        with open(self.source.path) as f:
            return f.read()

    def write(self, content, force=False):
        '''
        :arg content: The content to write to the file.
        :arg force: Flag to write over existing file.
        :type content: String
        :type force: Boolean

        :returns: None

        :raises IOError: When attempting to write over an existing file while
          ``force`` is ``False``.
        '''
        if not force and os.path.isfile(self.source.path):
            raise IOError('File {0} already exists.'.format(self.source.path))
        with open(self.source.path, 'w') as f:
            f.write(content)
