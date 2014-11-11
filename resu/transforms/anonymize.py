from resu.transforms import Transform

class Anonymize(Transform):
    '''
    Transform sensitive feilds into anonymous defaults.
    '''

    def apply(self, data, **kwargs):
        '''
        Currently, this function is just a toy to test out transforms.

        :arg data: All user supplied data.
        :type data: dict
        :arg kwargs: Unused
        :type kwargs: dict

        :returns: A dict without personal identification information.
        :rtype: Dictionary.
        '''
        data['resume']['personal']['name'] = 'Jane Doe'
        return data
