'''
This module stores the main commands for working with projects.
'''

import resu
from resu.loaders import load
from resu.parsers import get_parser
from resu.template import Template

def build(
        parser='yaml',
        data_source='resu.yml',
        template='default',
        output_file='resu.html'):
    '''
    Create a new resume from configuration files.
    '''
    # Get and process data
    parser = get_parser(parser)
    data = parser.load(load(data_source))

    with open(output_file, 'w') as out:
        out.write(resu.render_template(template, data))

def generate(template='default', output_file='resu.yml'):
    with open(output_file, 'w') as out:
        out.write(load(resu.find(Template, template).example_source))
