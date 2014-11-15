from collections import namedtuple

from resu.loaders import PackageDataSource

class Template(namedtuple('Template', [
        'name', 'file_type', 'language', 'template_source', 'example_source'])):
    pass

def get_template(name):
    return Template(
        name='default',
        file_type='html',
        language='jinja2',
        template_source=PackageDataSource(
            'resu',
            'examples/templates/default.html'),
        example_source=PackageDataSource('resu', 'examples/resu.yml'))
