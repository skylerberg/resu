import os

from resu.io import Provider


class File(Provider):
    '''
    Read and write to a file on the local file system.

    :var name: ``file``
    :var return_type: ``str``
    '''

    name = 'file'
    return_type = str

    def __init__(self, path):
        '''
        :arg path: Path to the file.
        :type path: String
        '''
        self.path = path

    def read(self):
        '''
        :returns: Contents of the file specified in ``self.source``.
        :rtype: String

        :raises IOError: if the file does not exist.
        '''
        with open(self.path) as f:
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
        if not force and os.path.isfile(self.path):
            raise IOError('File {0} already exists.'.format(self.path))
        with open(self.path, 'w') as f:
            f.write(content)
