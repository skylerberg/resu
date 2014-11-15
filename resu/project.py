'''
This module stores the main commands for working with projects.
'''

import resu
from resu.loaders import load
from resu.parsers import get_parser
from resu.template_engines import get_template_engine

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

    template = resu.get_template(template)
    template_engine = get_template_engine(template.language)
    with open(output_file, 'w') as out:
        out.write(template_engine.render(load(template.template_source), config=data))

def generate(template='default', output_file='resu.yml'):
    with open(output_file, 'w') as out:
        out.write(load(resu.get_template(template).example_source))
