'''
Entry point into pyres and subcommands.

pyres.cli is responsible for providing the entry point for executables as well
as
'''
import sys

from docopt import docopt

from pyres import init, __version__

PYRES_DOC = \
'''Usage:
    pyres [options]
    pyres [options] <command> [<args>]...

Options:
    -h --help       Show this message.
    -v --version    Show PyRes version number and exit.

Commands:
    help            Display documentation for a command.
    init            Create a new pyres project.
    build           Build a document from a pyres project.
'''

HELP_DOC = \
''' Usage: pyres help [<command>]
'''

INIT_DOC = \
'''Usage: pyres init [options]

Options:
    -h --help       Show this message.
    -d <path> --directory <path>
                    Directory to create new project in.
                    [default: .]
'''

BUILD_DOC = \
'''Usage: pyres build [options]

Options:
    -h --help       Show this message.
    -i <file> --input-file <file>
                    Path to input file.
                    [default: resume.yml]
    -o <file> --output-file <file>
                    Path to output file.
                    [default: resume.pdf]
    -c <file> --config-file <file>
                    Path to configuration file.
                    [default: config.yml]
    -s <path> --sections-dir <path>
                    Directory containing sections.
                    [default: section]
    -t <path> --transforms-dir <path>
                    Directory containing transforms.
                    [default: transforms]
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
        arguments = docopt(PYRES_DOC, argv=args, options_first=True, help=False)
    except SystemExit:
        out.write(PYRES_DOC)
        exit(1)
    if arguments['--help']:
        out.write(PYRES_DOC)
        exit(0)
    if arguments['--version']:
        out.write(__version__ + '\n')
        exit(0)
    command = arguments['<command>']
    if command in COMMANDS:
        COMMANDS[command](arguments['<args>'])
    else:
        out.write(PYRES_DOC)
        exit(1)

def help_command():
    '''Display documentation for a command'''
    pass

def init_command(args=None, out=sys.stdout):
    '''
    Create a new pyres project
    '''
    if not args:
        args = []
    try:
        arguments = docopt(INIT_DOC, argv=['init'] + args, help=False)
    except SystemExit:
        out.write(INIT_DOC)
        exit(1)
    if arguments['--help']:
        out.write(INIT_DOC)
        exit(0)
    init(directory=arguments['--directory'])


def build_command():
    '''Build a document from a pyres project'''
    pass

COMMANDS = {
    'help': help_command,
    'init': init_command,
    'build': build_command
}
