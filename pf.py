#!/bin/python3
#
# pf.py - pythfinder CLI

import argparse
import json
import sys
import re
import requests

from pythfinder import Character
from pathlib import Path

# pythfinder directory path, in $home
PYTHFINDER_DIR = Path("{}/.pythfinder".format(Path.home()))

# Ensure that the pythfinder directory exists
def ensure_pythfinder_dir():
    Path(PYTHFINDER_DIR).mkdir(exist_ok=True)

# Ensure that the given path is a valid file
def parse_file_path(path):
    return Path(path).is_file()

"""
Given a string, determines if it's a valid link to a pythfinder 
character sheet; if it is, returns the UUID of the character, if not, 
returns None.
"""
def parse_pythfinder_url(url):
    # lowercase url
    url = url.lower()
    pythfinder_url_regex = r"(https?://)?(www.)?(pythfinder.io/)([a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[a-f0-9]{4}-[a-f0-9]{12})"

    parsed = re.search(pythfinder_url_regex, url)
    if parsed:
        return parsed.group(4)
    else:
        return None

# Given a uuid string, build the API link for the base character
def build_pythfinder_url(uuid):
    # until api is set up, this will remain localhost
    return "http://localhost:5000/api/v0/characters/{}".format(uuid)

"""
Given a target, returns the type of target within. If not a valid 
target, returns "None"
"""
def parse_target(target):
    uuid = parse_pythfinder_url(target)
    valid_file = parse_file_path(target)
    if uuid:
        return "pythfinder.io"
    if valid_file:
        return "file"
    else:
        return None

# Get various pieces of character information
def get(args):
    target_type = parse_target(args.target)
    print(target_type)

# Argument parsing
parser = argparse.ArgumentParser(description = "The pythfinder CLI")

subparsers = parser.add_subparsers(title = "actions")

parser_get = subparsers.add_parser("get",
                                   help = "list various pieces of the character sheet")

parser_get.add_argument("element", metavar = "element",
                        help = "the element of the character sheet to 'get'",
                        choices = ["character", "equipment"])
parser_get.add_argument("target", metavar = "target",
                        help = "the target character sheet to interact with")

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
