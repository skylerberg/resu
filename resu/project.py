'''
This module stores the main commands for working with projects.
'''

def build(config):
    '''
    Create a new resume from configuration files.
    '''
    # Get and process data
    source = config.get_data_source()
    loader = config.get_loader()
    parser = config.get_parser()
    transform = config.get_transform()
    data = transform(parser.load(loader.load(source)))

    template = config.get_template().get()
    template_engine = config.get_template_engine()
    output_file = config.get_output_file()
    with open(output_file, 'w') as out:
        out.write(template_engine.render(template, config=data))

def generate(config):
    with open('resu.yml', 'w') as out:
        out.write(config.get_template().get_example())
