import resu
import resu.template_engines
import resu.parsers
import resu.templates

class Config(object):
    '''
    Store configuration parameters and translate them into Resu classes.
    '''

    def __init__(self):
        self.parser = 'yaml'
        self.data_files = ('resu.yml', )
        self.transforms = ()
        self.template = 'default'
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
        Return a parser for a configured format.

        :returns: Parser class for configured format.
        :rtype: Subclass of :class:`Parser`.
        '''
        for parser in resu.parsers.Parser.__subclasses__():
            if self.parser == parser.format:
                return parser()

    def get_data_files(self):
        '''
        Get a list of data files based on config.

        :returns: Paths to data files specified.
        :rtype: List of strings.
        '''
        return self.data_files

    def get_transform(self):
        '''
        Running the composite function returned by this function is the
        equivalent of running each transform in the same order supplied.

        :returns: A function composed of the application of each transform given.
        :rtype: Function.
        '''
        transform_lookup = {}
        for transform in resu.transforms.Transform.__subclasses__():
            transform_lookup[transform.name] = transform()
        composite = _identity
        for transform_name in self.transforms:
            transform = transform_lookup[transform_name]
            composite = _compose(transform.apply, composite)
        return composite


    def get_template(self):
        '''
        Get template from configuration.

        :returns: A template.
        :rtype: :class:`Template`
        '''
        for template in resu.templates.Template.__subclasses__():
            if self.template == template.name:
                return template()

    def get_template_engine(self):
        '''
        Get template engine from configuration.

        :returns: A template engine
        :rtype: :class:`TemplateEngine`.
        '''
        template = self.get_template()
        for template_engine in resu.template_engines.TemplateEngine.__subclasses__():
            if template.language == template_engine.language:
                return template_engine()

    def get_output_file(self):
        '''
        Get output file from configuration.

        :returns: The path to the intended output file.
        :rtype: String.
        '''
        return self.output_file

def _identity(data):
    '''
    The single argument identity function.
    '''
    return data

def _compose(f, g):
    '''
    Return the composition of two functions taking a single argument.
    '''
    return lambda data: f(g(data))
