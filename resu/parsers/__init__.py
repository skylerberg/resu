'''
Resu expects IO to yield serialized data in need of parsing. To smooth out the
differences between parsers, Resu provides parsers with a uniform interface.
For example, PyYAML provides a ``dump`` function while Python's built in json
module provides a ``dumps`` function. Resu wraps both of these so that other
functions can call ``dump`` without knowing what parser is being used.
'''
from resu.parsers.parser import Parser
try:
    from resu.parsers.yaml_parser import YamlParser
except ImportError:
    pass
from resu.parsers.json_parser import JsonParser
