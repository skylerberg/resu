from collections import namedtuple

from resu.sources import PackageDataSource

class Template(namedtuple('Template', [
        'name', 'file_type', 'language', 'template_source', 'example_source'])):

    instances = []

    def __init__(self, **kwargs):
        Template.instances.append(self)

Template(name='default', file_type='html', language='jinja2',
        template_source=PackageDataSource('resu', 'examples/templates/default.html'),
        example_source=PackageDataSource('resu', 'examples/resu.yml'))
