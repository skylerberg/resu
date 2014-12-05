import abc

class Converter(object):
    '''Abstract base class for file type converters.

    :var name: The name of the conversion provided. This must be a string in 
      the form '<input_type> to <output_type>'.
    '''

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def name(self):
        pass

    @abc.abstractmethod
    def convert(self, data):
        '''
        return a string with the 

        :arg data: Contents of file in input format.
        :type data: String

        :returns: Contents of file in output format.
        :rtype: String
        '''
        pass
