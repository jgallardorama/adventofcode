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

def load_moves(path, stacks: List[List[str]]):
    result = 0

    with open(path,"r") as file:

        while True:
            line = file.readline()            
            if not line:
                break
            match = re.search(regex, line)
            if match:
                size = int(match.group("size"))
                source = int(match.group("source"))
                target = int(match.group("target"))

                for index in range(0, size):
                    item = stacks[source-1].pop()
                    stacks[target-1].append(item)


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