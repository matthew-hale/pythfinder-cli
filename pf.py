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

# Argument parsing
pythfinder_parser = argparse.ArgumentParser(description = "The pythfinder CLI")

pythfinder_parser.add_argument("action", metavar = "action",
                               help = "the action to be taken on the character sheet",
                               choices = ["get"])

pythfinder_parser.add_argument("target", metavar = "target",
                               help = "the character sheet you intend to interact with")

if __name__ == "__main__":
    ensure_pythfinder_dir()
    if len(sys.argv) < 2:
        pythfinder_parser.print_help()
        sys.exit(0)
    args = pythfinder_parser.parse_args()
    print("{} {}".format(args.action, args.target))
