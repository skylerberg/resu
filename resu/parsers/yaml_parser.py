import yaml

from resu.parser import DataParser

class YamlParser(DataParser):

    format = "yaml"

    def load(self, data):
        return yaml.load(data)
