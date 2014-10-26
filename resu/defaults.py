'''A collection of default values.'''

import resu.template_engines
import resu.parsers

TEMPLATE_ENGINE = resu.template_engines.Jinja2Engine()
DATA_PARSER = resu.parsers.YamlParser()
