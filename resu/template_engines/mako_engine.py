import mako

from resu.template_engines import TemplateEngine

class MakoEngine(TemplateEngine):
    '''
    :class:`resu.TemplateEngine` for Mako.
    '''

    def render(self, template, **kwargs):
        '''
        :arg template: A template.
        :type template: str
        :arg kwargs: Conext for the template.
        :type kwargs: dict

        :returns: Template rendered with Mako.
        :rtype: String.
        '''
        mako_template = mako.template.Template(template)
        return mako_template.render(**kwargs)
