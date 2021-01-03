#!/bin/python3
#
# pf.py - pythfinder CLI

import argparse
import json
import sys

from pythfinder import Character
from pathlib import Path

pythfinder_dir = Path("{}/.pythfinder".format(Path.home()))

"""
Ensure that the pythfinder directory exists
"""
def ensure_pythfinder_dir():
    Path(pythfinder_dir).mkdir(exist_ok=True)

if __name__ == "__main__":
    ensure_pythfinder_dir()
