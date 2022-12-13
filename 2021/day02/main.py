from curses.ascii import isupper
from pathlib import Path
import string

import re
from typing import List


regex = r"move (?P<size>[0-9]*) from (?P<source>[0-9]*) to (?P<target>[0-9]*)"



def main(path):
    with open(path,"r") as file:
        position = 0
        depth = 0
        aim = 0
        while True:
            line = file.readline()            
            if not line:
                break
            
            command, number = line.split(" ")
            
            if command == "forward":
                position += int(number)
                depth += int(number) * aim
            if command == "up":
                aim -= int(number)
            if command == "down":
                aim += int(number)
                
            
            

        print(f"pos: {position} depth: {depth} = {position * depth}")

dir = "sample"
path = Path(__file__).parent / f"{dir}/input.dat"

main(path)


dir = "data"
path = Path(__file__).parent / f"{dir}/input.dat"

main(path)          