#!/bin/python3
#
# pf.py - pythfinder CLI

import argparse
import json
import sys

from pythfinder import Character
from pathlib import Path

# pythfinder directory path, in $home
pythfinder_dir = Path("{}/.pythfinder".format(Path.home()))

# Ensure that the pythfinder directory exists
def ensure_pythfinder_dir():
    Path(pythfinder_dir).mkdir(exist_ok=True)

# Get various pieces of character information
def get(args):
    print("you called 'get' with the target: {}".format(args.target))

# Argument parsing
parser = argparse.ArgumentParser(description = "The pythfinder CLI")

subparsers = parser.add_subparsers(title = "actions")

parser_get = subparsers.add_parser("get",
                                   help = "list various pieces of the character sheet")

parser_get.add_argument("target", metavar = "target",
                        help = "the element of the character sheet to 'get'",
                        choices = ["character", "equipment"])

parser_get.set_defaults(func = get)
parser_save = subparsers.add_parser("save",
                                    help = "save the character sheet in source to dest")

parser_save.add_argument("source", metavar = "source")
parser_save.add_argument("destination", metavar = "destination")

if __name__ == "__main__":
    # Parse args
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(0)
    args = parser.parse_args()

    ensure_pythfinder_dir()

    args.func(args)
