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
parser = argparse.ArgumentParser(description = "The pythfinder CLI - interact with local or remote pathfinder character sheets.")

actions = parser.add_subparsers(title = "action", required = True, metavar = "action", description = "the type of action to take with the character sheet")

parser_new = actions.add_parser("new", help = "create a new character sheet")
parser_get = actions.add_parser("get", help = "retrieve various pieces of data from the character sheet")
parser_create = actions.add_parser("create", help = "create a new item in a collection, or a new character sheet")
parser_update = actions.add_parser("update", help = "update a specific item, collection of items, or fields of the character sheet")
parser_delete = actions.add_parser("delete", help = "delete one or more items in a collection")
parser_copy = actions.add_parser("copy", help = "copy an existing character sheet to a new location")

# All CRUD actions except for delete get the collection argument 
# (delete gets a slightly modified collection argument that does not 
# include "character")
for action in [parser_get, parser_create, parser_update]:
    action.add_argument("collection", metavar = "collection",
                        help = "the collection of elements to interact with",
                        choices = [
                            "character",
                            "feat",
                            "trait",
                            "special",
                            "class",
                            "ability",
                            "throw",
                            "equipment",
                            "skill",
                            "spell",
                            "attack",
                            "armor"
                        ])

# delete's special collection arg
parser_delete.add_argument("collection", metavar = "collection",
                           help = "the collection of elements to interact with",
                           choices = [
                               "character",
                               "feat",
                               "trait",
                               "special",
                               "class",
                               "ability",
                               "throw",
                               "equipment",
                               "skill",
                               "spell",
                               "attack",
                               "armor"
                           ])

# Get, update, and delete can have filters
for action in [parser_get, parser_update, parser_delete]:
    action.add_argument("filter", metavar = "filter", help = "optional filters to apply; can also provide a single UUID string to specify an item directly", nargs = "?", default = "{}")

for action in [parser_create, parser_update]:
    action.add_argument("values", metavar = "values", help = "new values in JSON format")

parser_new.add_argument("values", metavar = "values", help = "new values in JSON format (optional)", nargs = "?", default = "{}")

for _, action in actions.choices.items():
    action.add_argument("target", metavar = "target", help = "the target character sheet; file path, scp URL, or pythfinder.io URL")

if __name__ == "__main__":
    # Parse args
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(0)
    args = parser.parse_args()

    ensure_pythfinder_dir()

    print(args)
