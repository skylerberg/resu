'''
Entry point into resu and subcommands. resu.cli is responsible for providing
the entry point for executables as well as handling parsing arguments.
'''
import sys
import os
import importlib

import docopt

import resu
from resu.io import Provider, File
from resu.templates import Template
from resu.parsers import Parser, YamlParser
from resu.template_engines import TemplateEngine
from resu.converters import Converter

CLI_DOC = \
    '''Usage:
    resu [options] [<file>]
    resu [options]

Options:
    -h --help               Show this message.
    -v --version            Show resu version number and exit.
    -l --list-features      Show all supported features.
    -g --generate           Generate the default resu.yml file.
    -p --parser <name>      Use specified parser for user provided data files.
    -t --template <name>    Use specified template.
    -o --output-file <file> Path to output file.
    -f --format <file_type> File type to produce.
    -e --extensions <names> Comma separated list of extensions to import.
'''


def run(args=sys.argv[1:], out=sys.stdout):
    '''
    Handle command line options and run Resu.

    :arg args: Resu arguments.
    :arg out: Output file, or StringIO. Defaults to standard out.

    :returns: None
    '''
    try:
        arguments = docopt.docopt(
            CLI_DOC,
            argv=args,
            options_first=True,
            help=False)
    except SystemExit:
        out.write(CLI_DOC)
        exit(1)

    if arguments['--extensions']:
        _load_extensions(arguments['--extensions'].split(','))

    generate_kwargs = {}
    build_kwargs = {}
    if arguments['--output-file']:
        generate_kwargs['output_provider'] = File(arguments['--output-file'])
        build_kwargs['output_provider'] = File(arguments['--output-file'])
    if arguments['--format']:
        build_kwargs['output_format'] = arguments['--format']
        generate_kwargs['output_format'] = arguments['--format']
    if arguments['--template']:
        generate_kwargs['template_name'] = arguments['--template']
        build_kwargs['template_name'] = arguments['--template']
    if arguments['<file>']:
        build_kwargs['input_provider'] = File(arguments['<file>'])
    if arguments['--parser']:
        build_kwargs['input_format'] = arguments['--parser']

    if arguments['--help']:
        out.write(CLI_DOC)
    elif arguments['--version']:
        out.write(resu.__version__ + '\n')
    elif arguments['--list-features']:
        _print_capabilities(out)
    elif arguments['--generate']:
        resu.get_example(**generate_kwargs)  # pylint: disable=star-args
    else:
        resu.build(**build_kwargs)  # pylint: disable=star-args


def _load_extensions(extensions):
    '''
    Load each extension as a python module from either installed packages or
    from the current working directory.
    '''
    sys.path.append(os.getcwd())
    for extension in extensions:
        importlib.import_module(extension)


def _print_capabilities(out=sys.stdout):
    '''
    Prints out a YAML representation of the available features.
    '''
    capabilities = {}
    capabilities['parsers'] = resu.available(Parser)
    capabilities['templates'] = resu.available(Template)
    capabilities['template engines'] = resu.available(TemplateEngine)
    capabilities['IO providers'] = resu.available(Provider)
    capabilities['Converters'] = resu.available(Converter)
    parser = YamlParser()
    out.write(parser.dump(capabilities))
