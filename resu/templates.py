'''
This module stores the :class:`resu.templates.Template` class and instantiates
all templates included in Resu by default.

To add a template to Resu, one need only instantiate an instance of
:class:`resu.templates.Template` class. The instance will automatically be
made available to the rest of Resu.
'''
from collections import namedtuple

import resu.io


class Template(
        namedtuple('Template', 'name source example file_type language')):
    '''
    This modified namedtuple, contains metadata associated with a template.
    Most importantly, this includes the templates name and where to find the
    template. Other attributes are optional and default to sensible values,
    however, setting the location of an example of the input the
    :class:`resu.templates.Template` expects is highly recommended.

    :var instances: Stores a list of all instances of
      :class:`resu.templates.Template` that have been instantiated.
    '''

    instances = []

    def __new__(cls,
                name,
                source,
                example=None,
                file_type='html',
                language='jinja2'):
        '''
        This method is used to set default values for a namedtuple.

        :arg name: Name of the template. Required.
        :arg source: Location of the template. Required.
        :arg example: Location of example input for the template.
          Defaults to ``None``.
        :arg file_type: File type the template renders to.
          Defaults to ``'html'``.
        :arg language: Templating language used in the template.
          Defaults to ``'jinja2'``.
        :type name: String
        :type source: :class:`resu.io.Provider`
        :type example: :class:`resu.io.Provider`
        :type file_type: String
        :type language: String
        '''
        return super(Template, cls).__new__(cls,
                                            name,
                                            source,
                                            example,
                                            file_type,
                                            language)

    def __init__(self, **kwargs):
        Template.instances.append(self)


Template(name='default',
         source=resu.io.PackageData('resu', 'examples/templates/default.html'),
         example=resu.io.PackageData('resu', 'examples/resu.yml'))
