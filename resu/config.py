'''
This file contains default values and functions for dealing with configuration.

Default values are assigned through from one of the following sources. If one
source does not provide the value, then the next is looked up.

1. Command line arguments.
2. Configuration in data files.
3. Built in default values.

This class will eventually replace the defaults.py file.
'''

import resu
import resu.template_engines
import resu.parsers

# Default values
PARSER_FORMAT = 'yaml'
DATA_FILES = ('resu.yml', )
TRANSFORMS = ()
TEMPLATE_ENGINE = resu.template_engines.Jinja2Engine()
OUTPUT_FILE = 'resu.html'

class Config(object):
    '''Store configuration parameters and translate them into Resu classes.'''

    def __init__(self):
        self.command_line_options = {}
        self.user_data_options = {}

    def set_command_line_options(self, options):
        self.command_line_options = options

    def set_user_data_options(self, options):
        self.user_data_options = options

    def get_parser(self):
        '''Get a Parser object from the configuration.'''
        format = PARSER_FORMAT
        if 'parser' in self.command_line_options:
            format = self.command_line_options['parser']
        return resu.Parser.get_parser(format)()

    def get_data_files(self):
        '''Return a list of data files based on config.'''
        if 'data_files' in self.command_line_options:
            return self.command_line_options['data_files']
        return DATA_FILES

    def get_transform(self):
        '''Get a function composed of all transforms specified in the
        configuration.'''
        transforms = TRANSFORMS
        if 'transforms' in self.user_data_options:
            transforms = self.user_data_options['transforms']
        return resu.Transform.get_composite_transform(transforms)

    # TODO(skyler) Make this function actually look at config
    def get_template(self):
        '''Get template from configuration.'''
        return resu.get_template()

    # TODO(skyler) Make this function actually look at config
    def get_template_engine(self):
        '''Get template engine from configuration.'''
        return TEMPLATE_ENGINE

    def get_output_file(self):
        '''Get output file from configuration.'''
        if 'output_file' in self.command_line_options:
            return self.command_line_options['output_file']
        if 'output_file' in self.user_data_options:
            return self.user_data_options['output_file']
        return OUTPUT_FILE
