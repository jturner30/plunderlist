"""Plunderlist
Usage:
    cli.py <command> [OPTIONS]

Options:
    -h --help   Show this screen
"""

from docopt import docopt
import plunderlist


def dispatch_command(command, args):
    if command == 'ls':
        plunderlist.print_task_list()


def main():
    args = docopt(__doc__)
    command = args.pop('<command>')
    dispatch_command(command, args)

    
if __name__ == '__main__':
    main()
