'''
Entry point into pyres and subcommands.
'''
import sys

from docopt import docopt

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
    -h --help       Show this message.
    -d --directory  Directory to create new project in.
                    Default is the current directory.
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

def pyres(args=sys.argv[1:], out=sys.stdout):
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
        print COMMANDS[command]
        COMMANDS[command](arguments['<args>'])
    else:
        out.write(PYRES_DOC)
        exit(1)

def display_help(*args, **kwargs):
    '''Display documentation for a command'''
    pass

def init(*args, **kwargs):
    '''
    Create a new pyres project
    '''
    pass

def build(*args, **kwargs):
    '''Build a document from a pyres project'''
    pass

COMMANDS = {
        'help': display_help,
        'init': init,
        'build': build
        }
