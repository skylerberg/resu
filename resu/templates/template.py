import abc

class Template(object):
    '''
    Abstract base class for templates.

    This class provides a method for getting the content of a tempalte as well
    as some metadata for that template.

    :var name: The name of the template.
    :var file_type: The file type the template produces.
    :var language: The templating language used in the template.
    '''

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def name(self):
        pass

    @abc.abstractproperty
    def file_type(self):
        pass

    @abc.abstractproperty
    def language(self):
        pass

    @abc.abstractmethod
    def get(self):
        '''
        :returns: The contents of the template.
        :rtype: String.
        '''
        pass