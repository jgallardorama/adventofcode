from curses.ascii import isupper
from pathlib import Path
import string

import re
from typing import List

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2

regex = r"move (?P<size>[0-9]*) from (?P<source>[0-9]*) to (?P<target>[0-9]*)"


def load_stacks(path) -> List[List[str]]:
    stacks: List[List[str]] = [[], [], [], [], [], [], [], [], [], [], [], []]
    result = 0

    with open(path,"r") as file:

        while True:
            line = file.readline()            
            if not line:
                break

            index = 0
            while True:
                position = index * 4 + 1
                if position > len(line):
                    break
                
                item = line[position]
                if item != " ":
                    stacks[index].insert(0, item)
                    
                index+=1    
    return stacks   

def print_stacks(stacks: List[List[str]]):
    for stack in stacks:
        if stack:
            print(stack)

def load_moves(path, stacks: List[List[str]]):
    result = 0

    print_stacks(stacks)
    with open(path,"r") as file:

        while True:
            line = file.readline()            
            if not line:
                break
            match = re.search(regex, line)
            if match:
                size = int(match.group("size"))
                source_idx = int(match.group("source"))
                target_idx = int(match.group("target"))
                
                print(f"=== {line}")
                
                source = stacks[source_idx-1]
                target = stacks[target_idx-1]

                items = source[-size:]
                source =source[0:-size]
                target += items
                
                stacks[source_idx-1] = source
                stacks[target_idx-1] = target
                
                print_stacks(stacks)


def main():
    dir = "data"
    path = Path(__file__).parent / f"{dir}/input.dat"

    stacks: List[List[str]] = load_stacks(path)
    print(stacks)
    
    path = Path(__file__).parent / f"{dir}/moves.dat"
    
    load_moves(path, stacks)
    print(stacks)
    
    key = ""
    for stack in stacks:
        if stack:
            key += (stack[-1])
    
    print(key)
    
main()