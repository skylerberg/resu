'''
This module stores the main commands for working with projects.
'''

import resu
from resu.loaders import load
from resu.parsers import get_parser
from resu.template_engines import get_template_engine

def build(config):
    '''
    Create a new resume from configuration files.
    '''
    # Get and process data
    parser = get_parser(config.parser)
    data = parser.load(load(config.data_source))

    template = resu.get_template(config.template)
    template_engine = get_template_engine(template.language)
    with open(config.output_file, 'w') as out:
        out.write(template_engine.render(load(template.template_source), config=data))

def generate(config):
    with open('resu.yml', 'w') as out:
        out.write(load(resu.get_template(config.template).example_source))
