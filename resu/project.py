'''
This module stores the main commands for working with projects.

This module should not be directly imported, all public members of this module
are made available in :module:`resu`.
'''

import resu
import resu.io
from resu.parsers import Parser
from resu.templates import Template
from resu.template_engines import TemplateEngine
from resu.converters import Converter


def build(
        input_provider=None,
        output_provider=None,
        input_format='yaml',
        output_format='pdf',
        template_name='default'):
    '''
    Use user data to create a document from a template. The user's data is read
    from the source provided, parsed into a dictionary, and used to render a
    template. The rendered template is then written to the specified location.

    :arg input_provider: A string indicating where to find the resume data. If
      left as ``None``, defaults to ``resu.io.File('resu.yml')``.
    :arg output_provider: Path to the file to write the resume to. If left as
      ``None``, defaults to ``resu.io.File('resu.' + output_format)``.
    :arg input_format: The format of the resume data must be parsed from.
    :arg template: Name of the template for the resume.
    :type input_provider: :class:`resu.io.Provider` or None
    :type output_provider: :class:`resu.io.Provider` or None
    :type input_format: String
    :type template: String

    :returns: None
    '''
    if input_provider is None:
        input_provider = resu.io.File('resu.yml')
    if output_provider is None:
        output_provider = resu.io.File('resu.' + output_format)

    parser = resu.find(Parser, input_format)()
    data = parser.load(input_provider.read())
    output = render_template(template_name, data)

    template = resu.find(Template, template_name)
    if template.file_type != output_format:
        converter = _get_converter(template.file_type, output_format)()
        output = converter.convert(output)

    output_provider.write(output, force=True)


def get_example(
        output_provider=resu.io.File('resu.yml'),
        output_format='yml',
        template_name='default'):
    '''
    Write the example input for a template to the specified location. The data
    written by this command can be used by :func:`build` to generate a
    document.

    :arg output_provider: Path to the file to save the example resume to.
    :arg output_format: The file type to produce. Currently, this is not
      implemented.
    :arg template: The name of the template to generate an example for.
    :type output_provider: :class:`resu.io.Provider`
    :type output_format: String
    :type template: String

    :returns: None
    '''
    template = resu.find(Template, template_name)
    output_provider.write(template.example.read())


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


def _get_converter(input_type, output_type):
    for converter_format in resu.available(Converter):
        in_type, _, out_type = converter_format.split(' ')
        if in_type == input_type and out_type == output_type:
            return resu.find(Converter, converter_format)
