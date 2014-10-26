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

def _copy_data_dir(target_dir, data_dir):
    '''Copy a directory from package data.

    Completely copies a directory and all files and subdirectories from the
    package data.

    target_dir: Directory to copy files into.
    data_dir: Directory to to copy data from inside of the package.

    Raises MissingPackageDataError if data_dir does not correspond to a
    directory inside the resu package.

    Returns a list of warnings for each conflicting file found.
    '''
    if not pkg_resources.resource_exists('resu', data_dir):
        raise MissingPackageDataError(
            '{data_dir} does not exist.'.format(data_dir=data_dir))
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    warnings = []
    for resource_name in pkg_resources.resource_listdir('resu', data_dir):
        resource_path = data_dir + '/' + resource_name
        if pkg_resources.resource_isdir('resu', resource_path):
            warnings += _copy_data_dir(
                os.path.join(target_dir, resource_name),
                resource_path)
        else:
            try:
                _copy_data_file(target_dir, data_dir, resource_name)
            except FileExistsError as exc:
                warnings.append(str(exc))
    return warnings

def get_template(template='default.html'):
    '''Return a template as a string.'''
    template_location = TEMPLATES_DIR + '/' + template
    if not pkg_resources.resource_exists('resu', template_location):
        raise MissingPackageDataError(
            '{template} does not exist.'.format(template=template_location))
    return pkg_resources.resource_string('resu', template_location)

# TODO(skyler) Replace this function with something more general
def generate_default():
    '''Copy default resu.yml file into local directory.'''
    _copy_data_file('.', DATA_DIR, 'resu.yml')