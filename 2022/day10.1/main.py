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
        self.cycle = 0
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
        return self.op_time == 0 or self.cycle >= 240
        
    def get_cycle(self):
        return self.cycle

def main(path):
    
    clock = Clock()
    
    crt = [["." for i in range(0,40)] for j in range(0, 6)]
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
            
            
            while not clock.idle() and clock.get_cycle() < 240:
                cycle, x = clock.exec_cycle()
                
                cycle_row = int(cycle / 40)
                cycle_pos = cycle % 40
                cycle_min = cycle_pos - 1
                cycle_max = cycle_pos + 1
                
                result = "."
                if cycle_min <= x and x <= cycle_max:
                    result="#"
                
                print(f"CYCLE {cycle}, {x}, {result}")  
                crt[cycle_row][cycle_pos]= result

            

        for crt_line in crt:
            print("".join(crt_line))
dir = "data"
path = Path(__file__).parent / f"{dir}/input.dat"

main(path)            