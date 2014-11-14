import abc

class Template(object):
    '''
    Abstract base class for templates.

    This class provides a method for getting the content of a template as well
    as some metadata for that template.

    :var name: The name of the template.
    :var file_type: The file type the template produces.
    :var language: The templating language used in the template.
    :var template_source: The source that the template can be loaded from.
    :var example_source: Source of example input for the template.
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

    @abc.abstractproperty
    def template_source(self):
        pass

    @abc.abstractproperty
    def example_source(self):
        pass

    @abc.abstractmethod
    def get(self):
        '''
        :returns: The contents of the template.
        :rtype: String.
        '''
        pass

    @abc.abstractmethod
    def get_example(self):
        '''
        :returns: The contents of the example input for the template.
        :rtype: String.
        '''
        pass
