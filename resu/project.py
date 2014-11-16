'''
This module stores the main commands for working with projects.
'''

import resu
from resu.parsers import Parser
from resu.templates import Template
from resu.template_engines import TemplateEngine
from resu.loaders import Loader
from resu.sources import FileSource

def build(
        data_source='resu.yml',
        parser='yaml',
        template='default',
        output_file='resu.html'):
    '''
    Create a new resume from configuration files.

    :arg data_source: A string indicating where to find the resume data.
    :arg parser: The format of the resume data must be parsed from.
    :arg template: Name of the template for the resume.
    :arg output_file: Path to the file to write the resume to.
    :type data_source: String
    :type parser: String
    :type template: String
    :type output_file: String

    :returns: None
    '''
    data_source = FileSource(data_source)
    data = parse(parser, load(data_source))
    with open(output_file, 'w') as out:
        out.write(render_template(template, data))

def generate(template='default', output_file='resu.yml'):
    '''
    Generate an example resume for a template.

    :arg template: The name of the template to generate an example for.
    :arg output_file: Path to the file to save the example resume to.
    :type template: String
    :type output_file: String

    :returns: None
    '''
    with open(output_file, 'w') as out:
        out.write(load(resu.find(Template, template).example_source))


def load(source):
    '''
    Read data from ``source``.

    :arg source: The source of the data.
    :type source: namedtuple

    :returns: Deserialized data
    :rtype: Dictionary
    '''
    return resu.find(Loader, type(source), id_attr='source_type')().load(source)

def parse(format_, data):
    '''
    Parse data

    :arg language: The serialization format to parse.
    :arg data: Data to deserialize.
    :type langauge: String
    :type data: String

    :returns: Deserialized data
    :rtype: Dictionary
    '''
    return resu.find(Parser, format_)().load(data)

def render_template(name, data):
    '''
    Render a template with provided data.

    :arg name: Name of the template to render.
    :arg data: Data to pass into the template.
    :type name: String
    :type data: Dictionary

    :returns: The template with data provided as its context.
    :rtype: String
    '''
    template = resu.find(Template, name)
    template_content = load(template.template_source)
    template_engine = resu.find(TemplateEngine, template.language)()
    return template_engine.render(template_content, config=data)
