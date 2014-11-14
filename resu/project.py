'''This module stores the main commands for working with projects.'''

import resu

def build(config):
    '''Create a new resume from configuration files.'''
    # Set up config and read data
    loader = config.get_loader()
    data = loader.load(config.get_data_source())
    parser = config.get_parser()
    data = parser.load(data)

    # Get a composite transform based on config
    data = config.get_transform()(data)

    template = config.get_template().get()
    template_engine = config.get_template_engine()
    output_file = config.get_output_file()
    with open(output_file, 'w') as out:
        out.write(template_engine.render(template, config=data))

def generate(config):
    print config.get_template().get_example()
