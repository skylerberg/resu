from resu.loaders import Loader

class File(Loader):
    '''
    '''

    return_type = str

    def load(self, source):
        '''
        :returns: The contents stored in ``source``.
        :rtype: String.
        '''
        with open(source) as f:
            return f.read()
