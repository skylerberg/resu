from resu.parsers.parser import Parser
try:
    from resu.parsers.yaml_parser import YamlParser
except ImportError:
    pass
from resu.parsers.json_parser import JsonParser

def get_parser(parser_format):
    '''
    Get a parser that can parse the format specified in the configuration.

    :returns: Parser class for configured format.
    :rtype: Subclass of :class:`Parser`.
    '''
    for parser in Parser.__subclasses__():
        if parser_format == parser.name:
            return parser()
