from curses.ascii import isupper
from pathlib import Path
import string

import re
from typing import List


regex = r"move (?P<size>[0-9]*) from (?P<source>[0-9]*) to (?P<target>[0-9]*)"

def process_line(line: str):
    return "", 1
    pass

groups = []

def main(path):
    with open(path,"r") as file:

        counter = 0
        while True:
            line = file.readline()            
            if not line:
                break
            
            item = int(line)
            groups.append([])
            for group in groups:
                group.append(item)
            
            if len(groups[0]) == 4:
                first = sum(groups[0][0:3])
                second = sum(groups[1])
                if first < second:
                    counter+=1

                del groups[0]

            
        print(f"{counter}")

dir = "data"
path = Path(__file__).parent / f"{dir}/input.dat"

main(path)            