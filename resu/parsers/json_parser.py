import json

from resu.parser import DataParser

class JsonParser(DataParser):

    format = "json"

    def load(self, data):
        return json.load(data)
