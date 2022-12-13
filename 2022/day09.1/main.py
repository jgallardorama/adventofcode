from curses.ascii import isupper
from pathlib import Path
import string

import re
from typing import List


regex = r"move (?P<size>[0-9]*) from (?P<source>[0-9]*) to (?P<target>[0-9]*)"

def process_line(line: str):
    return "", 1
    pass


map = []

class Rope:
    def __init__(self) -> None:
        self.head_x = 0
        self.head_y = 0
        self.tail_x = 0
        self.tail_y = 0
                    
    def move(self, delta_x, delta_y):
        last_x = self.head_x
        last_y = self.head_y
        
        self.head_x += delta_x
        self.head_y += delta_y
        self.calc_tail(last_x, last_y)
        
    def calc_tail(self, last_x, last_y):
        delta_x = self.head_x - self.tail_x
        delta_y = self.head_y - self.tail_y

        if abs(delta_x) > 1 or abs(delta_y) > 1:
            self.tail_x = last_x
            self.tail_y = last_y
        

    def tail(self):
        return self.tail_x, self.tail_y
    def head(self):
        return self.head_x, self.head_y


def main(path):
    
    sim = Rope()
    maps = []
    
    with open(path,"r") as file:
        index = 0
        while True:
            line = file.readline()            
            if not line:
                break
            
            parts = line.split(" ")
            
            move = parts[0]
            steps = int(parts[1])
            
            delta = 0, 0
            for step in range(0, steps):
                if index == 5:
                    print("Break")                
                if move == "U":
                    sim.move(0, 1)
                elif move == "D":
                    sim.move(0, -1)
                elif move == "L":
                    sim.move(-1, 0)
                elif move == "R":
                    sim.move(1, 0)

                tail_pos = sim.tail()
                head_pos = sim.head()
                if not tail_pos in maps:
                    maps.append(tail_pos)
                
                print(f"{index} {move} {steps} - {head_pos} {tail_pos}")
                index +=1


    print(f"Total {len(maps)}")

dir = "sample"
path = Path(__file__).parent / f"{dir}/input.dat"

main(path)   

# exit(0)         

dir = "data"
path = Path(__file__).parent / f"{dir}/input.dat"

main(path)