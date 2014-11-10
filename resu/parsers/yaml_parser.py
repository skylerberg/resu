import yaml

from resu.parser import Parser

class YamlParser(Parser):
    '''
    Parser for YAML files.

    :var format: ``'yaml'``
    :type format: str
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
