import jinja2

from resu.templating import TemplateEngine

class Jinja2Engine(TemplateEngine):

    def render(self, template, **kwargs):
        jinja_template = jinja2.Template(template)
        return jinja_template.render(**kwargs)
