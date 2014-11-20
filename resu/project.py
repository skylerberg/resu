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
        input_provider=io.File('resu.yml'),
        output_provider=io.File('resu.html'),
        parser='yaml',
        template='default'):
    '''
    Use user data to create a document from a template. The user's data is read
    from the source provided, parsed into a dictionary, and used to render a
    template. The rendered template is then written to the specified location.

    :arg input_provider: A string indicating where to find the resume data.
    :arg output_provider: Path to the file to write the resume to.
    :arg parser: The format of the resume data must be parsed from.
    :arg template: Name of the template for the resume.
    :type input_provider: :class:`io.Provider`
    :type output_proiver: :class:`io.Provider`
    :type parser: String
    :type template: String

    :returns: None
    '''
    data = parse(parser, input_provider.read())
    output = render_template(template, data)
    output_provider.write(output, force=True)


def get_example(output_provider=io.File('resu.yml'), template='default'):
    '''
    Write the example input for a template to the specified location. The data
    written by this command can be used by :func:`build` to generate a
    document.

    :arg output_provider: Path to the file to save the example resume to.
    :arg template: The name of the template to generate an example for.
    :type output_provider: :class:`io.Provider`
    :type template: String

    :returns: None
    '''
    output_provider.write(resu.find(Template, template).example.read())


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
    template_content = template.source.read()
    template_engine = resu.find(TemplateEngine, template.language)()
    return template_engine.render(template_content, config=context)
