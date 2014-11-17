'''
This module stores the main commands for working with projects.

This module should not be directly imported, all public members of this module
are made available in :module:`resu`.
'''

import resu
from resu.parsers import Parser
from resu.templates import Template
from resu.template_engines import TemplateEngine
from resu.loaders import Loader, FileLoader
from resu.sources import FileSource

def build(
        data_source='resu.yml',
        parser='yaml',
        template='default',
        output_file='resu.html'):
    '''
    Use user data to create a document from a template. The user's data is read
    from the source provided, parsed into a dictionary, and used to render a
    template. The rendered template is then written to the specified location.

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
    output = render_template(template, data)
    FileLoader().write(FileSource(output_file), output, force=True)

def generate(template='default', output_file='resu.yml'):
    '''
    Write the example input for a template to the specified location. The data
    written by this command can be used by :func:`build` to generate a
    document.

    :arg template: The name of the template to generate an example for.
    :arg output_file: Path to the file to save the example resume to.
    :type template: String
    :type output_file: String

    :returns: None
    '''
    source = FileSource(output_file)
    content = load(resu.find(Template, template).example_source)
    FileLoader().write(source, content)

def load(source):
    '''
    Read data from ``source``.

    :arg source: The source of the data.
    :type source: namedtuple

    :returns: Deserialized data
    :rtype: Dictionary
    '''
    return resu.find(Loader, type(source), id_attr='source_type')().read(source)

def parse(format_, data):
    '''
    Parses data serialized as a string into a Python dictionary.

    :arg language: The serialization format to parse.
    :arg data: Data to deserialize.
    :type langauge: String
    :type data: String

    :returns: Deserialized data
    :rtype: Dictionary
    '''
    return resu.find(Parser, format_)().load(data)

def render_template(name, context):
    '''
    Render a template with provided context.

    :arg name: Name of the template to render.
    :arg context: Context to pass to the template.
    :type name: String
    :type data: Dictionary

    :returns: The template with data provided as its context.
    :rtype: String
    '''
    template = resu.find(Template, name)
    template_content = load(template.template_source)
    template_engine = resu.find(TemplateEngine, template.language)()
    return template_engine.render(template_content, config=context)
