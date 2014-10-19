'''
Entry point into resu and subcommands.

resu.cli is responsible for providing the entry point for executables as well
as handling parsing arguments and providing defaults.
'''
import sys

import docopt

import resu

CLI_DOC = \
'''Usage:
    resu [options] [<files>]...

Options:
    -h --help           Show this message.
    -v --version        Show resu version number and exit.
    -g --generate       Generate the default resu.yml file.
    -o --output-file <file>
                        Path to output file.
                        [default: resu.html]
'''

def run(args=sys.argv[1:], out=sys.stdout):
    '''
    Dispatch control to a longer.

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
        resu.generate_default()
    else:
        if not arguments['<files>']:
            arguments['<files>'] = ['resu.yml']
        resu.build(
            data_files=arguments['<files>'],
            output_file=arguments['--output-file'])
