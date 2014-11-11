import resu
from resu.templates import Template

class Default(Template):
    '''
    Default template.

    :var file_type: ``html``
    :type file_type: str
    :var language: ``jinja2``
    :type language: str
    '''

    file_type = 'html'

    language = 'jinja2'

    def get(self):
        '''
        :returns: The contents of the default template.
        :rtype: String.
        '''
        return resu.get_template()
