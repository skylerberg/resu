import abc

class TemplateEngine(object):
    '''
    Abstract base class for template engines.

    Support for a templating engine should be added to Resu by implementing this
    class.

    :var name: The templating language that the engine can parse.
    '''

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def name(self):
        pass

    @abc.abstractmethod
    def render(self, template, **kwargs):
        '''
        :arg template: A template.
        :type template: str
        :arg kwargs: Context for the template.
        :type kwargs: dict

        :returns: Rendered template.
        :rtype: String.
        '''
        pass
