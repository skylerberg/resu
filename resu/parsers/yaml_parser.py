import yaml

from resu.parser import Parser

class YamlParser(Parser):

    format = "yaml"

    def load(self, data):
        return yaml.load(data)
