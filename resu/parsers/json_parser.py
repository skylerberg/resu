import json

from resu.parser import Parser

class JsonParser(Parser):
    '''
    Parser for JSON files.

    :var format: ``'json'``
    :type format: String.
    '''

    format = "json"

    def load(self, data):
        '''
        Deserialize JSON data.

        :arg data: Serialized data in the JSON format.
        :type data: str

        :returns: Deserialized data.
        :rtype: Object.
        '''
        return json.load(data)
