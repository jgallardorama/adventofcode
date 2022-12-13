from curses.ascii import isupper
from pathlib import Path
import string

import re
from typing import List


regex = r"move (?P<size>[0-9]*) from (?P<source>[0-9]*) to (?P<target>[0-9]*)"

def process_line(line: str):
    return "", 1
    pass

def to_dec(bool_stream):
    result = 0
    while True:
        
        result += bool_stream[0]        
        del bool_stream[0]
        if len(bool_stream) == 0:
            break
        else:
            result *=2
                    
    return result
    

def main(path):
    with open(path,"r") as file:

        counters = [0,0,0,0,0,0,0,0,0,0,0,0]
        total = 0
        size_word = 0
        while True:
            line = file.readline()            
            if not line:
                break
            
            if size_word == 0:
                size_word = len(line)-1
            
            pos = 0
            for item in line:
                if item == "1":
                    counters[pos] += 1
                pos +=1
                
            total+=1

        print(counters)
        print(f"Total {total}")

        result = [1 if counter> total/2 else 0 for counter in counters]
        print(to_dec(result[0:size_word]))


dir = "sample"
path = Path(__file__).parent / f"{dir}/input.dat"

main(path)


dir = "data"
path = Path(__file__).parent / f"{dir}/input.dat"

main(path)          