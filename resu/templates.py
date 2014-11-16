from collections import namedtuple

from resu.sources import PackageDataSource

class Template(namedtuple('Template', [
        'name',
        'file_type',
        'language',
        'template_source',
        'example_source'])):
    '''
    :var name: Name of the template. Required.
    :var file_type: File type the template renders to. Required.
    :var language: Templating language used in the template. Required.
    :var template_source: Location of the template. Required.
    :var example_source: Location of example input for the template. Optional.
    '''

    instances = []

    def __init__(self, **kwargs):
        Template.instances.append(self)

Template(name='default', 
         file_type='html',
         language='jinja2',
         template_source=PackageDataSource('resu', 'examples/templates/default.html'),
         example_source=PackageDataSource('resu', 'examples/resu.yml'))
