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

