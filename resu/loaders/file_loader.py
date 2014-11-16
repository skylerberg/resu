from resu.loaders import Loader

class FileLoader(Loader):
    '''
    Loads the contents of a file.

    :var name: ``file``
    :var source_type: ``str``
    :var return_type: ``str``
    '''

    name = 'file'
    source_type = str
    return_type = str

    def load(self, source):
        '''
        :returns: The contents stored in ``source``.
        :rtype: String.
        '''
        with open(source) as f:
            return f.read()
