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

# TODO(skyler) Consider making Config class a NamedTuple.
class Config(object):
    '''
    Store configuration parameters and translate them into Resu classes.
    '''

    def __init__(self):
        self.parser_format = 'yaml'
        self.data_files = ('resu.yml', )
        self.transforms = ()
        self.template_engine = resu.template_engines.Jinja2Engine()
        self.template = resu.templates.Default()
        self.output_file = 'resu.html'

    def set_command_line_options(self, options):
        '''
        Load parsed command line options.

        :arg options: Options specified on the command line.
        :type options: dict

        :returns: None
        :rtype: None
        '''
        for key, value in options.iteritems():
            if key in self.__dict__:
                self.__dict__[key] = value

    def get_parser(self):
        '''
        Get a :class:`Parser` that can handle the format specified in the
        configuration.

        :returns: A Parser
        :rtype: :class:`Parser`
        '''
        return resu.parsers.Parser.get_parser(self.parser_format)()

    def get_data_files(self):
        '''
        Get a list of data files based on config.

        :returns: Paths to data files specified.
        :rtype: List of strings.
        '''
        return self.data_files

    def get_transform(self):
        '''
        Get a function composed of transforms specified in the configuration.

        :returns: Composition of all transforms specified.
        :rtype: Function.
        '''
        return resu.transforms.Transform.get_composite_transform(self.transforms)

    def get_template(self):
        '''
        Get template from configuration.

        :returns: A template.
        :rtype: :class:`Template`
        '''
        return self.template

    def get_template_engine(self):
        '''
        Get template engine from configuration.

        :returns: A template engine
        :rtype: :class:`TemplateEngine`.
        '''
        return self.template_engine

    def get_output_file(self):
        '''
        Get output file from configuration.

        :returns: The path to the intended output file.
        :rtype: String.
        '''
        return self.output_file
