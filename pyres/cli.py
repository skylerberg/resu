'''Usage: pyres [options] <command> [<args>]...

Options:
    -h --help   Show this screen.
    -l --list   Show a list of available commands

Commands:
    help        Display documentation for a command
    init        Create a new pyres project
    build       Build a document from a pyres project
    '''

import sys

from docopt import docopt

def pyres(args=sys.argv[1:], out=sys.stdout):
    '''Main entry point into pyres'''
    try:
        arguments = docopt(__doc__, argv=args, options_first=True)
    except SystemExit:
        out.write(__doc__)
        exit(1)
    command = arguments['<command>']
    if command in COMMANDS:
        print COMMANDS[command]
        COMMANDS[command](arguments['<args>'])
    else:
        out.write(__doc__)
        exit(1)

def display_help(*args, **kwargs):
    '''Display documentation for a command'''
    pass

def init(*args, **kwargs):
    '''Create a new pyres project'''
    pass

def build(*args, **kwargs):
    '''Build a document from a pyres project'''
    pass

COMMANDS = {
        'help': display_help,
        'init': init,
        'build': build
        }
