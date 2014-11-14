'''
Entry point into resu and subcommands.

resu.cli is responsible for providing the entry point for executables as well
as handling parsing arguments.
'''
import sys

import docopt

import resu

CLI_DOC = \
'''Usage:
    resu [options] [<file>]

Options:
    -h --help               Show this message.
    -v --version            Show resu version number and exit.
    -g --generate           Generate the default resu.yml file.
    -p --parser <name>      Use specified parser for user provided data files.
    -t --template <name>    Use specified template.
    -o --output-file <file> Path to output file.
'''

def run(args=sys.argv[1:], out=sys.stdout):
    '''
    Handle command line options and run Resu.

    args
        Resu arguments. Defaults to system arguments.

    out
        Output file, or StringIO. Defaults to standard out.
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
    elif arguments['--version']:
        out.write(resu.__version__ + '\n')
    elif arguments['--generate']:
        resu.example.generate_default()
    else:
        kwargs = {}
        if arguments['<file>']:
            kwargs['data_source'] = arguments['<file>']
        if arguments['--output-file']:
            kwargs['output_file'] = arguments['--output-file']
        if arguments['--parser']:
            kwargs['parser'] = arguments['--parser']
        if arguments['--template']:
            kwargs['template'] = arguments['--template']
        resu.build(**kwargs)
