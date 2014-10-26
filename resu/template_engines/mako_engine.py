import mako

from resu.templating import TemplateEngine

class MakoEngine(TemplateEngine):

    def render(self, template, **kwargs):
        mako_template = mako.template.Template(template)
        return mako_template.render(**kwargs)
