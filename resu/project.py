'''project.py

This module stores the main commands for working with projects.
'''

import resu.transforms
import resu.parsers
from resu.exceptions import DataMergeError

def _merge_dicts(dicts):
    '''Recursively combine a list of dictionaries.

    If a subset of the dictionaries contain the same key and the associated
    value is a dictionary in all dictionaries in this subset, then the key will
    map to the merged values.

    If a subset of the dictionaries contain the same key and the associated
    value is a list in all dictionaries in this subset, then the lists will be
    concatenated in the order the dictionaries where provided.

    If a subset of the dictionaries contain the same key and the associated
    value in any dictionary contains any data type other than lists or
    dictionies or there are both list and dictionary values, then a
    DataMergeError is raised.

    warning: This function copies the data in each dictionary, this could be
    quite costly. This function is a prime candidate for optimization.
    '''
    out = {}
    for dictionary in dicts:
        for key, value in dictionary.iteritems():
            if key not in out:
                out[key] = value
            else:
                if isinstance(out[key], dict) and isinstance(value, dict):
                    out[key] = _merge_dicts([out[key], value])
                elif isinstance(out[key], list) and isinstance(value, list):
                    out[key] += value
                else:
                    raise DataMergeError(
                        "Cannot combine {first} and {second}".format(
                            first=type(out[key]), second=type(value)))
    return out

def _combine_data_files(files, parser):
    '''Read a list of files containing dictionaries and combine their content.
    '''
    dicts = []
    for data_file_path in files:
        with open(data_file_path) as data_file:
            dicts.append(parser.load(data_file.read()))
    return _merge_dicts(dicts)

def _apply_transforms(transforms, data):
    '''Apply all transforms specified in the config file.'''
    composite_transform = resu.Transform.get_composite_transform(transforms)
    return composite_transform(data)

def build(
        data_files=resu.defaults.DATA_FILES,
        output_file=resu.defaults.OUTPUT_FILE,
        parser=resu.defaults.DATA_PARSER,
        template_engine=resu.defaults.TEMPLATE_ENGINE):
    '''Create a new resume from configuration files.'''
    data = _combine_data_files(data_files, parser)
    settings = data.get('config', {})
    data = _apply_transforms(settings.get('transforms', []), data)
    template = resu.get_template()
    with open(output_file, 'w') as out:
        out.write(template_engine.render(template, config=data))
