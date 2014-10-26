import mako

from resu.template_engine import TemplateEngine

class MakoEngine(TemplateEngine):

    def render(self, template, **kwargs):
        mako_template = mako.template.Template(template)
        return mako_template.render(**kwargs)
