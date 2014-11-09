import json

from resu.parser import Parser

class JsonParser(Parser):

    format = "json"

    def load(self, data):
        return json.load(data)
