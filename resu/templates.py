from collections import namedtuple

from resu import io


class Template(
        namedtuple('Template',
                   'name template_source example_source file_type language')):
    '''
    :var name: Name of the template. Required.
    :var template_source: Location of the template. Required.
    :var example_source: Location of example input for the template.
      Defaults to ``None``.
    :var file_type: File type the template renders to.
      Defaults to ``'html'``.
    :var language: Templating language used in the template.
      Defaults to ``'jinja2'``.
    '''

    instances = []

    def __new__(cls,
                name,
                template_source,
                example_source=None,
                file_type='html',
                language='jinja2'):
        # add default values
        return super(Template, cls).__new__(cls,
                                            name,
                                            template_source,
                                            example_source,
                                            file_type,
                                            language)

    def __init__(self, **kwargs):
        Template.instances.append(self)


Template(name='default',
         template_source=io.PackageData('resu', 'examples/templates/default.html'),
         example_source=io.PackageData('resu', 'examples/resu.yml'))
