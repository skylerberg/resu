import resu
from resu.templates import Template
from resu.loaders import PackageDataLoader, PackageDataSource

class DefaultTemplate(Template):
    '''
    Default template.

    :var file_type: ``'default'``
    :var file_type: ``'html'``
    :var language: ``'jinja2'``
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
        return PackageDataLoader().load(DefaultTemplate.example_source)
