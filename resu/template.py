import abc

class Template(object):
    '''
    Abstract base class for templates.

    This class provides a method for getting the content of a tempalte as well
    as some metadata for that template.

    :var file_type: The file type the template produces.
    :type file_type: str
    :var language: The templating language used in the template.
    :type language: str
    '''

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def file_type(self):
        raise NotImplementedError

    @abc.abstractproperty
    def language(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self):
        '''
        :returns: The contents of the template.
        :rtype: String.
        '''
        raise NotImplementedError