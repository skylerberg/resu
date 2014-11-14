'''
Functions for working with the built in examples for configuration and
templates.
'''

import os

import pkg_resources

from resu.exceptions import FileExistsError, MissingPackageDataError

DATA_DIR = 'examples'
TEMPLATES_DIR = 'examples/templates'

def _copy_data_file(target_dir, data_dir, data_file):
    '''Copy a file from package data

    target_dir: Directory to copy files into.
    data_dir: Directory to to copy data from inside of the package.
    data_file: File to copy from data_dir.

    Raises FileExistsError if a file with the same name as data_file already
    exists in target_dir.
    '''
    data_file_location = data_dir + '/' + data_file
    if not pkg_resources.resource_exists('resu', data_file_location):
        raise MissingPackageDataError(
            '{data_file} does not exist.'.format(data_file=data_file_location))
    default_file = pkg_resources.resource_string('resu', data_file_location)
    data_file_path = os.path.join(target_dir, data_file)
    if os.path.exists(data_file_path):
        raise FileExistsError(
            '{file} already exists.'.format(file=data_file_path))
    with open(data_file_path, 'w') as new_file:
        new_file.write(default_file)

# TODO(skyler) Replace this function with something more general
def generate_default():
    '''Copy default resu.yml file into local directory.'''
    _copy_data_file('.', DATA_DIR, 'resu.yml')
