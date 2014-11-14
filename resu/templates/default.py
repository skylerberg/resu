import resu
from resu.templates import Template
from resu.loaders import PackageData, PackageDataSource

class Default(Template):
    '''
    Default template.

    :var file_type: ``'default'``
    :var file_type: ``'html'``
    :var language: ``'jinja2'``
    '''

    name = 'default'
    file_type = 'html'
    language = 'jinja2'
    source = PackageDataSource('resu', 'examples/templates/default.html')

    def get(self):
        '''
        :returns: The contents of the default template.
        :rtype: String.
        '''
        return PackageData().load(Default.source)
