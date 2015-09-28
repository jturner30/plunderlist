"""Plunderlist
Usage:
    cli.py add <title>

Options:
    -h --help   Show this screen
"""

from docopt import docopt


def main():
    args = docopt(__doc__)
    title = args['<title>']
    print title


if __name__ == '__main__':
    main()
