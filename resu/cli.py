'''
Entry point into resu and subcommands.

resu.cli is responsible for providing the entry point for executables as well
as
'''
import sys

from docopt import docopt

from resu import init, __version__

RESU_DOC = \
'''Usage:
    resu [options]
    resu [options] <command> [<args>]...

Options:
    -h --help       Show this message.
    -v --version    Show resu version number and exit.

Commands:
    help            Display documentation for a command.
    init            Create a new resu project.
    build           Build a document from a resu project.
'''

HELP_DOC = \
''' Usage: resu help [<command>]
'''

INIT_DOC = \
'''Usage: resu init [options]

Options:
    -h --help       Show this message.
    -d <path> --directory <path>
                    Directory to create new project in.
                    [default: .]
'''

BUILD_DOC = \
'''Usage: resu build [options]

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
'''

def resu_command(args=sys.argv[1:], out=sys.stdout):
    '''
    Dispatch control to a longer.

    args
        Resu arguments. Defaults to system arguments.

    out
        Output file, or StringIO. Defaults to standard out.
    '''
    try:
        arguments = docopt(RESU_DOC, argv=args, options_first=True, help=False)
    except SystemExit:
        out.write(RESU_DOC)
        exit(1)
    if arguments['--help']:
        out.write(RESU_DOC)
        exit(0)
    if arguments['--version']:
        out.write(__version__ + '\n')
        exit(0)
    command = arguments['<command>']
    if command in COMMANDS:
        COMMANDS[command](arguments['<args>'])
    else:
        out.write(RESU_DOC)
        exit(1)

def help_command():
    '''Display documentation for a command'''
    pass

def init_command(args=None, out=sys.stdout):
    '''
    Create a new resu project
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
    '''Build a document from a resu project'''
    pass

COMMANDS = {
    'help': help_command,
    'init': init_command,
    'build': build_command
}
