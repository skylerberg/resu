from resu.transform import Transform

class Anonymize(Transform):
    '''Transform sensitive feilds into anonymous defaults.'''

    def apply(self, data):
        '''Currently, this function is just a toy to test out transforms.'''
        data['resume']['personal']['name'] = 'Jane Doe'
        return data
