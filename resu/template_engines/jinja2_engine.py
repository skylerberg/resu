import jinja2

from resu.template_engines import TemplateEngine


class Jinja2Engine(TemplateEngine):
    '''
    :class:`resu.TemplateEngine` for Jinja2.

    :var name: ``'jinja2'``
    '''

    name = 'jinja2'

    def render(self, template, **kwargs):
        '''
        :arg template: A template.
        :arg kwargs: Context for the template.
        :type template: String
        :type kwargs: Dictionary

        :returns: Template rendered with Jinja2.
        :rtype: String
        '''
        jinja_template = jinja2.Template(template)
        return jinja_template.render(**kwargs)
