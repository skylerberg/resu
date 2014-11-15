'''
This module stores the main commands for working with projects.
'''

import resu
from resu.loaders import load

def build(config):
    '''
    Create a new resume from configuration files.
    '''
    # Get and process data
    parser = config.get_parser()
    data = parser.load(load(config.data_source))

    template = load(resu.get_template(config.template).template_source)
    template_engine = config.get_template_engine()
    with open(config.output_file, 'w') as out:
        out.write(template_engine.render(template, config=data))

def generate(config):
    with open('resu.yml', 'w') as out:
        out.write(load(resu.get_template(config.template).example_source))
