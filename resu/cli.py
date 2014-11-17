'''
Entry point into resu and subcommands. resu.cli is responsible for providing
the entry point for executables as well as handling parsing arguments.
'''
import sys
import os
import importlib

import docopt

import resu
from resu.templates import Template
from resu.parsers import Parser, YamlParser
from resu.loaders import Loader
from resu.template_engines import TemplateEngine

CLI_DOC = \
    '''Usage:
    resu [options] [<file>]

Options:
    -h --help               Show this message.
    -v --version            Show resu version number and exit.
    -l --list-features      Show all supported features.
    -g --generate           Generate the default resu.yml file.
    -p --parser <name>      Use specified parser for user provided data files.
    -t --template <name>    Use specified template.
    -o --output-file <file> Path to output file.
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
    if arguments['--help']:
        out.write(CLI_DOC)
        exit(0)
    if arguments['--version']:
        out.write(resu.__version__ + '\n')
        exit(0)
    if arguments['--extensions']:
        _load_extensions(arguments['--extensions'].split(','))
    if arguments['--list-features']:
        _print_capabilities(out)
        exit(0)
    kwargs = {}
    if arguments['<file>']:
        kwargs['data_source'] = arguments['<file>']
    if arguments['--output-file']:
        kwargs['output_file'] = arguments['--output-file']
    if arguments['--parser']:
        kwargs['parser'] = arguments['--parser']
    if arguments['--template']:
        kwargs['template'] = arguments['--template']
    if arguments['--generate']:
        resu.generate(**kwargs)
    else:
        resu.build(**kwargs)


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
    capabilities['input types'] = resu.available(Loader)
    parser = YamlParser()
    out.write(parser.dump(capabilities))
