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
DATA_PARSER_FORMAT = 'yaml'

class Config(object):
    '''Store configuration parameters and translate them into Resu classes.'''

    def __init__(self):
        self.command_line_options = {}

    def set_command_line_options(self, options):
        self.command_line_options = options

    def get_parser(self):
        '''Get a Parser object from the configuration.'''
        format = DATA_PARSER_FORMAT
        if 'parser' in self.command_line_options:
            format = self.command_line_options['parser']
        return resu.Parser.get_parser(format)()
