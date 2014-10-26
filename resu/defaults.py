'''A collection of default values.'''

import resu.template_engines
import resu.parsers

TEMPLATE_ENGINE = resu.template_engines.Jinja2Engine()
DATA_PARSER = resu.parsers.YamlParser()
OUTPUT_FILE = 'resu.html'
DATA_FILES = ('resu.yml')
