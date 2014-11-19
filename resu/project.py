'''
This module stores the main commands for working with projects.

This module should not be directly imported, all public members of this module
are made available in :module:`resu`.
'''

import resu
from resu import io
from resu.parsers import Parser
from resu.templates import Template
from resu.template_engines import TemplateEngine


def build(
        data_source=io.File('resu.yml'),
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
    data = parse(parser, data_source.read())
    output = render_template(template, data)
    io.File(output_file).write(output, force=True)


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
    content = resu.find(Template, template).example_source.read()
    io.File(output_file).write(content)


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
    template_content = template.template_source.read()
    template_engine = resu.find(TemplateEngine, template.language)()
    return template_engine.render(template_content, config=context)
