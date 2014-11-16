from collections import namedtuple

import resu
from resu.sources import PackageDataSource
from resu.template_engines import TemplateEngine

class Template(namedtuple('Template', [
        'name', 'file_type', 'language', 'template_source', 'example_source'])):

    instances = []

    def __init__(self, **kwargs):
        Template.instances.append(self)

Template(name='default', file_type='html', language='jinja2',
        template_source=PackageDataSource('resu', 'examples/templates/default.html'),
        example_source=PackageDataSource('resu', 'examples/resu.yml'))


def render_template(name, data):
    '''
    Render a template with provided data.

    :arg name: Name of the template to render.
    :type name: String
    :arg data: Data to pass into the template.
    :type data: Dictionary

    :returns: The template with data provided as its context.
    :rtype: String
    '''
    template = resu.find(Template, name)
    template_content = resu.load(template.template_source)
    return resu.find(TemplateEngine, template.language)().render(template_content, config=data)
