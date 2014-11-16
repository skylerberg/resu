import os

from resu.loaders import Loader
from resu.sources import FileSource

class FileLoader(Loader):
    '''
    Loads the contents of a file.

    :var name: ``file``
    :var source_type: ``str``
    :var return_type: ``str``
    '''

    name = 'file'
    source_type = FileSource
    return_type = str

    def read(self, source):
        '''
        :returns: The contents stored in ``source``.
        :rtype: String
        '''
        with open(source.path) as f:
            return f.read()

    def write(self, source, content, force=False):
        '''
        :arg source: The file to write.
        :arg content: The content to write to the file.
        :arg force: Flag to write over existing file.
        :type source: :class:`FileSource`
        :type content: String
        :type force: Boolean

        :returns: None

        :raises IOError: When attempting to write over an existing file while
          ``force`` is ``False``.
        '''
        if not force and os.path.isfile(source.path):
            raise IOError('File {0} already exists.'.format(source.path))
        with open(source.path, 'w') as f:
            f.write(content)
