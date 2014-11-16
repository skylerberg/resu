import json

from resu.parsers import Parser

class JsonParser(Parser):
    '''
    Parser for JSON files.

    :var name: ``'json'``
    '''

    name = "json"

    def load(self, data):
        '''
        Deserialize JSON data.

        :arg data: Serialized data in the JSON format.
        :type data: String

        :returns: Deserialized data.
        :rtype: Object
        '''
        return json.load(data)
