import mako

from resu.template_engines import TemplateEngine

class MakoEngine(TemplateEngine):
    '''
    :class:`resu.TemplateEngine` for Mako.

    :var name: ``'mako'``
    '''

    name  = 'mako'

    def render(self, template, **kwargs):
        '''
        :arg template: A template.
        :type template: String
        :arg kwargs: Context for the template.
        :type kwargs: Dictionary

        :returns: Template rendered with Mako.
        :rtype: String
        '''
        mako_template = mako.template.Template(template)
        return mako_template.render(**kwargs)
