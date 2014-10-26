import json

from resu.parser import DataParser

class JsonParser(DataParser):

    def load(self, data):
        return json.load(data)
