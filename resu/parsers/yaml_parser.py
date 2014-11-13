import yaml

from resu.parsers import Parser

class YamlParser(Parser):
    '''
    Parser for YAML files.

    :var format: ``'yaml'``
    '''

    format = "yaml"

    def load(self, data):
        '''
        Deserialize YAML data.

        :arg data: Serialized data in the YAML format.
        :type data: str

        :returns: Deserialized data.
        :rtype: Object.
        '''
        return yaml.load(data)
