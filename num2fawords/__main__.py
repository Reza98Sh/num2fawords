"""Provide a command-line interface to use cardinal_words and ordinal_words."""

from argparse import ArgumentParser

from num2fawords import cardinal_words, ordinal_words


parser = ArgumentParser()
parser.add_argument(
    'number', help='the number that is going to be converted to words'
)
parser.add_argument(
    '--ordinal', '-o',
    help='convert to ordinal from', action='store_true',
)
parser.add_argument(
    '--cardinal', '-c',
    help='convert to cardinal form', action='store_true',
)
args = parser.parse_args()
if args.cardinal:
    if args.ordinal:
        print(cardinal_words(args.number))
        print(ordinal_words(args.number))
    else:
        print(cardinal_words(args.number))
else:
    print(ordinal_words(args.number))