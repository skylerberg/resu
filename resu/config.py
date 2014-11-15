import resu
import resu.template_engines
import resu.parsers
import resu.loaders

class Config(object):
    '''
    Store configuration parameters and translate them into Resu classes.
    '''

    def __init__(self):
        self.parser = 'yaml'
        self.data_source = 'resu.yml'
        self.transforms = ()
        self.template = 'default'
        self.output_file = 'resu.html'

    def update(self, options):
        '''
        Replace existing configuration options.

        :arg options: New configuration options.
        :type options: dict

        :returns: None
        :rtype: None
        '''
        for key, value in options.iteritems():
            if key in self.__dict__:
                self.__dict__[key] = value

    def get_parser(self):
        '''
        Get a parser that can parse the format specified in the configuration.

        :returns: Parser class for configured format.
        :rtype: Subclass of :class:`Parser`.
        '''
        for parser in resu.parsers.Parser.__subclasses__():
            if self.parser == parser.format:
                return parser()

    def get_template_engine(self):
        '''
        Get template engine from configuration.

        :returns: A template engine
        :rtype: :class:`TemplateEngine`.
        '''
        template = resu.get_template(self.template)
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

    def get_loader(self):
        return resu.loaders.FileLoader()
