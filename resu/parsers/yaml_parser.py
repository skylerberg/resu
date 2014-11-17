import yaml

from resu.parsers import Parser

class YamlParser(Parser):
    '''
    Parser for YAML files.

    :var name: ``'yaml'``
    '''

    name = "yaml"

    def load(self, data):
        '''
        Deserialize YAML data.

        :arg data: Serialized data in the YAML format.
        :type data: String

        :returns: Deserialized data.
        :rtype: Object
        '''
        return yaml.load(data)

    def dump(self, data):
        '''
        :arg data: Data to serialize
        :type data: Object

        :returns: Data serialized as YAML.
        :rtype: String
        '''
        return yaml.dump(data)
