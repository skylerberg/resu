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
