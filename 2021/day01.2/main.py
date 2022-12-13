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

        previous = None
        counter = 0
        while True:
            line = file.readline()            
            if not line:
                break
            
            if previous:
                item = int(line)
                if item > previous:
                    counter += 1
                    
            previous = int(line)
                
            
        print(f"{counter}")

dir = "sample"
path = Path(__file__).parent / f"{dir}/input.dat"

main(path)            