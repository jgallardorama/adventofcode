from curses.ascii import isupper
from pathlib import Path
import string

import re
from typing import List


regex = r"move (?P<size>[0-9]*) from (?P<source>[0-9]*) to (?P<target>[0-9]*)"

def process_line(line: str):
    return "", 1
    pass

class Clock:
    def __init__(self) -> None:
        self.cycle = 1
        self.reg_x = 1
        self.next_x = 0
        self.op_time = 0
        
    
    def addx(self, value):
        self.next_x = self.reg_x + value
        self.op_time = 2
    
    def noop(self):
        self.next_x = self.reg_x
        self.op_time = 1

    def exec_cycle(self):
        result = self.cycle, self.reg_x
        self.op_time -= 1
        self.cycle += 1
        if self.op_time == 0:
            self.reg_x = self.next_x
            
        return result
            
    def idle(self):
        return self.op_time == 0
        
        

def main(path):
    
    clock = Clock()
    with open(path,"r") as file:

        sum = 0
        while True:
            line = file.readline()            
            if not line:
                break
            
            command_line = line.rstrip("\n")
            
            parts = command_line.split(" ")
            print(f"COMMAND: {command_line}")
            command = parts[0]
            if command == "addx":
                value = int(parts[1])
                clock.addx(value)
                pass
            elif command == "noop":
                clock.noop()
            
            
            while not clock.idle():
                cycle, x = clock.exec_cycle()     
                print(f"CYCLE {cycle}, {x}, {cycle * x}")       
                if cycle in  [20, 60, 100, 140, 180, 220]:
                    
                    sum += cycle * x

        print(f"SUM {sum}")
dir = "data"
path = Path(__file__).parent / f"{dir}/input.dat"

main(path)            