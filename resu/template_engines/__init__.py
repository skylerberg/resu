from resu.template_engines.template_engine import TemplateEngine
try:
    from resu.template_engines.jinja2_engine import Jinja2Engine
except ImportError:
    pass
try:
    from resu.template_engines.mako_engine import MakoEngine
except ImportError:
    pass

def get_template_engine(language):
    '''
    Get template engine from configuration.

    :returns: A template engine
    :rtype: :class:`TemplateEngine`.
    '''
    for template_engine in TemplateEngine.__subclasses__():
        if language == template_engine.language:
            return template_engine()
