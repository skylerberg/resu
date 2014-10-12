'''
Entry point into resu and subcommands.

resu.cli is responsible for providing the entry point for executables as well
as handling parsing arguments and providing defaults.
'''
import sys

from docopt import docopt

from resu import init, build, __version__

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
'''Usage: resu build [options] [<files>]...

Options:
    -h --help       Show this message.
    -o <file> --output-file <file>
                    Path to output file.
                    [default: resume.pdf]
    -s <path> --sections-dir <path>
                    Directory containing sections.
                    [default: sections]
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
    if command in COMMAND_FUNCTIONS:
        COMMAND_FUNCTIONS[command](arguments['<args>'])
    else:
        out.write(RESU_DOC)
        exit(1)

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


def build_command(args=None, out=sys.stdout):
    '''Build a document from a resu project'''
    if not args:
        args = []
    try:
        arguments = docopt(BUILD_DOC, argv=['build'] + args, help=False)
    except SystemExit:
        out.write(BUILD_DOC)
        exit(1)
    if arguments['--help']:
        out.write(BUILD_DOC)
        exit(0)
    if not arguments['<files>']:
        arguments['<files>'] = ['config.yml', 'resume.yml']
    build(
        output_file=arguments['--output-file'],
        sections_dir=arguments['--sections-dir'],
        files=arguments['<files>'])

def help_command(args=None, out=sys.stdout):
    '''Display documentation for a command'''
    if not args:
        args = []
    try:
        arguments = docopt(HELP_DOC, argv=['help'] + args)
    except SystemExit:
        out.write(HELP_DOC)
        exit(1)
    command = arguments.get('<command>', None)
    if not command:
        out.write(RESU_DOC)
    else:
        try:
            out.write(COMMAND_DOCS[command])
        except KeyError as exc:
            out.write("Invalid command: {command}".format(command=exc))
    exit(0)

COMMAND_FUNCTIONS = {
    'help': help_command,
    'init': init_command,
    'build': build_command
}

COMMAND_DOCS = {
    'help': HELP_DOC,
    'init': INIT_DOC,
    'build': BUILD_DOC
}
