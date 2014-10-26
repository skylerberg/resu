'''
An abstract class representating a templating engine that only provides the
provides only the features needed by Resu.
'''

import abc

class TemplateEngine(object):
    '''Abstract base class for template engines.

    Support for a templating engine should be added to Resu by implementing this
    class.
    '''

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def render(self, template, **kwargs):
        '''Return rendered template with data passed in as kwargs.'''
        raise NotImplementedError
