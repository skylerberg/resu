'''This module stores the main commands for working with projects.'''

import resu
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
    dictionaries or there are both list and dictionary values, then a
    DataMergeError is raised.

    Warning: This function copies the data in each dictionary, this could be
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

def build(**kwargs):
    '''Create a new resume from configuration files.'''
    # Set up config and read data
    config = resu.Config()
    config.set_command_line_options(kwargs)
    parser = config.get_parser()
    data = _combine_data_files(config.get_data_files(), parser)
    config.set_user_data_options(data.get('config', {}))

    # Get a composite transform based on config
    data = config.get_transform()(data)

    template = config.get_template()
    template_engine = config.get_template_engine()
    output_file = config.get_output_file()
    with open(output_file, 'w') as out:
        out.write(template_engine.render(template, config=data))
