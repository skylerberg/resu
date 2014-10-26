import yaml

from resu.parser import DataParser

class YamlParser(DataParser):

    def load(self, data):
        return yaml.load(data)
