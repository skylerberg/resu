import resu
from resu.templates import Template
from resu.loaders import PackageDataLoader, PackageDataSource

class DefaultTemplate(Template):
    '''
    Default template.

    :var file_type: ``'default'``
    :var file_type: ``'html'``
    :var language: ``'jinja2'``
    :var template_source: The location of the default resume template file.
    :var example_source: The location of the default resume input file.
    '''

    name = 'default'
    file_type = 'html'
    language = 'jinja2'
    template_source = PackageDataSource('resu', 'examples/templates/default.html')
    example_source = PackageDataSource('resu', 'examples/resu.yml')

    def get(self):
        '''
        :returns: The contents of the default template.
        :rtype: String.
        '''
        return PackageDataLoader().load(DefaultTemplate.template_source)

    def get_example(self):
        '''
        :returns: The contents of the default ``resu.yml`` file.
        :rtype: String.
        '''
        return PackageDataLoader().load(DefaultTemplate.example_source)
