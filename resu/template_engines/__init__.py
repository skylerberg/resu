from resu.template_engines.template_engine import TemplateEngine
try:
    from resu.template_engines.jinja2_engine import Jinja2Engine
except ImportError:
    pass
try:
    from resu.template_engines.mako_engine import MakoEngine
except ImportError:
    pass
