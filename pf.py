#!/bin/python3
#
# pf.py - pythfinder CLI

import argparse
import json
import sys

from pythfinder import Character
from pathlib import Path

if __name__ == "__main__":
    """
    Ensure that the pythfinder directory exists
    """
    pythfinder_dir = Path("{}/.pythfinder".format(Path.home()))
    Path(pythfinder_dir).mkdir(exist_ok=True)
