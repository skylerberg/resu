'''
This module stores the main commands for working with projects.
'''

import resu
from resu.parsers import get_parser
from resu.template import Template
from resu.loaders import Loader

def build(
        data_source='resu.yml',
        parser='yaml',
        template='default',
        output_file='resu.html'):
    '''
    Create a new resume from configuration files.

    :arg data_source: A string indicating where to find the resume data.
    :type data_source: String
    :arg parser: The format of the resume data must be parsed from.
    :type parser: String
    :arg template: Name of the template for the resume.
    :type template: String
    :arg output_file: Path to the file to write the resume to.
    :type output_file: String

    :returns: None
    '''
    # Get and process data
    parser = get_parser(parser)
    data = parser.load(resu.load(data_source))

    with open(output_file, 'w') as out:
        out.write(resu.render_template(template, data))

def generate(template='default', output_file='resu.yml'):
    '''
    Generate an example resume for a template.

    :arg template: The name of the template to generate an example for.
    :type template: String
    :arg output_file: Path to the file to save the example resume to.
    :type output_file: String

    :returns: None
    '''
    with open(output_file, 'w') as out:
        out.write(resu.load(resu.find(Template, template).example_source))


def load(source):
    '''
    Read data from ``source``.

    :arg source: The source of the data.
    :type source: namedtuple

    :returns: Deserialized data.
    :rtype: Dictionary
    '''
    return resu.find(Loader, type(source), id_attr='source_type')().load(source)
