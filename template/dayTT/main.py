from curses.ascii import isupper
from pathlib import Path
import string

import re
from typing import List


regex = r"move (?P<size>[0-9]*) from (?P<source>[0-9]*) to (?P<target>[0-9]*)"

def process_line(line: str):
    return "", 1
    pass


def main(path):
    with open(path,"r") as file:

        while True:
            line = file.readline()            
            if not line:
                break
            
            marker, result = process_line(line)
            print(marker, result)

dir = "data"
path = Path(__file__).parent / f"{dir}/input.dat"

main(path)            