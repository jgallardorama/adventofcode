from curses.ascii import isupper
from pathlib import Path
import string

import re
from typing import List


regex = r"move (?P<size>[0-9]*) from (?P<source>[0-9]*) to (?P<target>[0-9]*)"

def begin_stream(line: str):
    result = 0
    print(line)
    index = 0
    marker = []
    for item in line:
        print(f"{index} {item} {marker}")
        
        if item in marker:
            pos = marker.index(item)
            marker = marker[pos+1:len(marker)]
        
        size = len(marker)
        if size == 4:
            result = index
            break
        else:
            if size > 3:
                marker = marker[1:3]
    
            marker.append(item)
        
        index += 1

    
    return marker, result


def main(path):
    with open(path,"r") as file:

        while True:
            line = file.readline()            
            if not line:
                break
            
            marker, result = begin_stream(line)
            print(marker, result)
            
dir = "data"
path = Path(__file__).parent / f"{dir}/input.dat"

main(path)            