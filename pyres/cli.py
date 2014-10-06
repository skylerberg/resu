'''
Entry point into pyres and subcommands.

pyres.cli is responsible for providing the entry point for executables as well
as
'''
import sys

from docopt import docopt

from pyres import init

PYRES_DOC = \
'''Usage: pyres [options] <command> [<args>]...

Options:
    -h --help   Show this message.
    -l --list   Show a list of available commands.

Commands:
    help        Display documentation for a command.
    init        Create a new pyres project.
    build       Build a document from a pyres project.
'''

HELP_DOC = \
''' Usage: pyres help [<command>]
'''

INIT_DOC = \
'''Usage: pyres init [options]

Options:
    -h --help   Show this message.
    -d <path> --directory <path>
                Directory to create new project in.
                [default: .]
'''

BUILD_DOC = \
'''Usage: pyres build [options]

Options:
    -h --help           Show this message.
    -i --input-file     Path to input file.
                        Defaults to resume.yml.
    -o --output-file    Path to output file.
                        Defaults to resume.pdf.
    -c --config-file    Path to configuration file.
                        Defaults to config.yml.
    -t --transforms-dir Directory containing transforms.
                        Defaults to transforms.
    -s --sections-dir   Directory containing sections.
                        Defaults to sections.
'''

def pyres_command(args=sys.argv[1:], out=sys.stdout):
    '''
    Dispatch control to a longer.

    args
        Pyres arguments. Defaults to system arguments.

    out
        Output file, or StringIO. Defaults to standard out.
    '''
    try:
        arguments = docopt(PYRES_DOC, argv=args, options_first=True)
    except SystemExit:
        out.write(PYRES_DOC)
        exit(1)
    command = arguments['<command>']
    if command in COMMANDS:
        COMMANDS[command](arguments['<args>'])
    else:
        out.write(PYRES_DOC)
        exit(1)

def help_command(*args, **kwargs):
    '''Display documentation for a command'''
    pass

def init_command(args=[], out=sys.stdout):
    '''
    Create a new pyres project
    '''
    try:
        arguments = docopt(INIT_DOC, argv= ['init'] + args, help=False)
    except SystemExit:
        out.write(INIT_DOC)
        exit(1)
    if arguments['--help']:
        out.write(INIT_DOC)
        exit(0)
    init(directory=arguments['--directory'])


def build_command(*args, **kwargs):
    '''Build a document from a pyres project'''
    pass

COMMANDS = {
        'help': help_command,
        'init': init_command,
        'build': build_command
        }
