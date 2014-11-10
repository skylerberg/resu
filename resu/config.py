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
import resu.templates

# Default values
PARSER_FORMAT = 'yaml'
DATA_FILES = ('resu.yml', )
TRANSFORMS = ()
TEMPLATE_ENGINE = resu.template_engines.Jinja2Engine()
TEMPLATE = resu.templates.Default()
OUTPUT_FILE = 'resu.html'

class Config(object):
    '''
    Store configuration parameters and translate them into Resu classes.
    '''

    def __init__(self):
        self.command_line_options = {}
        self.user_data_options = {}

    def set_command_line_options(self, options):
        '''
        Load parsed command line options.

        :arg options: Options specified on the command line.
        :type options: dict

        :returns: None
        :rtype: None
        '''
        self.command_line_options = options

    def set_user_data_options(self, options):
        '''
        Load parsed options provided in user data files.

        :arg options: Options specified in the user data files.
        :type options: dict

        :returns: None
        :rtype: None
        '''
        self.user_data_options = options

    def get_parser(self):
        '''
        Get a :class:`Parser` that can handle the format specified in the
        configuration.

        :returns: A Parser
        :rtype: :class:`Parser`
        '''
        format = PARSER_FORMAT
        if 'parser' in self.command_line_options:
            format = self.command_line_options['parser']
        return resu.Parser.get_parser(format)()

    def get_data_files(self):
        '''
        Get a list of data files based on config.

        :returns: Paths to data files specified.
        :rtype: List of strings.
        '''
        if 'data_files' in self.command_line_options:
            return self.command_line_options['data_files']
        return DATA_FILES

    def get_transform(self):
        '''
        Get a function composed of transforms specified in the configuration.

        :returns: Composition of all transforms specified.
        :rtype: Function.
        '''
        transforms = TRANSFORMS
        if 'transforms' in self.user_data_options:
            transforms = self.user_data_options['transforms']
        return resu.Transform.get_composite_transform(transforms)

    # TODO(skyler) Make this function actually look at config
    def get_template(self):
        '''
        Get template from configuration.

        :returns: A template.
        :rtype: :class:`Template`
        '''
        return TEMPLATE

    # TODO(skyler) Make this function actually look at config
    def get_template_engine(self):
        '''
        Get template engine from configuration.

        :returns: A template engine
        :rtype: :class:`TemplateEngine`.
        '''
        return TEMPLATE_ENGINE

    def get_output_file(self):
        '''
        Get output file from configuration.

        :returns: The path to the intended output file.
        :rtype: String.
        '''
        if 'output_file' in self.command_line_options:
            return self.command_line_options['output_file']
        if 'output_file' in self.user_data_options:
            return self.user_data_options['output_file']
        return OUTPUT_FILE
