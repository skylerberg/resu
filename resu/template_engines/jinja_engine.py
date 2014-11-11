import jinja2

from resu.template_engines import TemplateEngine

class Jinja2Engine(TemplateEngine):
    '''
    :class:`resu.TemplateEngine` for Jinja2.
    '''

    def render(self, template, **kwargs):
        '''
        :arg template: A template.
        :type template: str
        :arg kwargs: Conext for the template.
        :type kwargs: dict

        :returns: Template rendered with Jinja2.
        :rtype: String.
        '''
        jinja_template = jinja2.Template(template)
        return jinja_template.render(**kwargs)
