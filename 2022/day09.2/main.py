from curses.ascii import isupper
from pathlib import Path
import string

import re
from typing import List


map = []

class Knot:
    def __init__(self, pos_x, pos_y, label = 0) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.label = "H" if label == 0 else str(label)
        
    def get_label(self):
        return self.label

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y
            
    def set(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        
    def get(self):
        return self.pos_x, self.pos_y

    def check(self, other):
        delta_x = self.pos_x - other.pos_x
        delta_y = self.pos_y - other.pos_y

        result = abs(delta_x) > 1 or abs(delta_y) > 1
        return result
    
    def delta(self, other):
        delta_x = self.pos_x - other.pos_x
        delta_y = self.pos_y - other.pos_y    
        return delta_x, delta_y
    
    def __str__(self):
        return f"({self.pos_x}, {self.pos_y})"
    

class Rope:
    def __init__(self) -> None:
        self.knots = [Knot(0,0, i) for i in range(0, 10)]
                    
    def move(self, delta_x, delta_y):
        
        index = 0
        
        current_knot = self.knots[index]
        current_knot.move(delta_x, delta_y)
        
        size = len(self.knots)
        
        while index < size - 1:
            next_knot = self.knots[index+1]
            print(f">>>=== {current_knot.label}:{current_knot} - {next_knot.label} {next_knot}")
            if current_knot.check(next_knot):
                delta_x , delta_y = current_knot.delta(next_knot)
                if abs(delta_x) > 1 and abs(delta_y) > 1:
                    d_x = int(delta_x/abs(delta_x))
                    d_y = int(delta_y/abs(delta_y))
                    print(f">>> MOVE {next_knot} {d_x} {d_y}")
                    next_knot.move(d_x, d_y)
                    
                elif abs(delta_x) > 1:
                    d_x = int(delta_x/abs(delta_x))
                    d_y = delta_y
                    print(f">>> MOVE {next_knot} {d_x} {d_y}")
                    next_knot.move(d_x, d_y)
                elif abs(delta_y) > 1:
                    d_x = delta_x
                    d_y = int(delta_y/abs(delta_y))
                    print(f">>> MOVE {next_knot} {d_x} {d_y}")
                    next_knot.move(d_x, d_y)
            current_knot = next_knot
            index +=1
            

    def tail(self):
        return self.knots[-1]
    def head(self):
        return self.knots[0]
    
def show_map(rope: Rope):
    return
    map = [['.' for i in range(0, 40)] for i in range(0, 40)]
    
    middle = int(len(map)/2)
    
    map[middle][middle] = "X"
    
    for knot in rope.knots:
        pos_x = knot.pos_x
        pos_y = knot.pos_y

        map[-pos_y + middle][pos_x + middle] = knot.get_label()

    for line in map:
        print("".join(line))

def main(path):
    
    rope = Rope()
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
      
                if move == "U":
                    rope.move(0, 1)
                elif move == "D":
                    rope.move(0, -1)
                elif move == "L":
                    rope.move(-1, 0)
                elif move == "R":
                    rope.move(1, 0)

                tail = rope.tail()
                head = rope.head()
                tail_pos = (tail.pos_x, tail.pos_y)
                if not tail_pos in maps:
                    maps.append(tail_pos)
                
                show_map(rope)
                
                index +=1

            show_map(rope)

    print(f"Total {len(maps)}")

dir = "sample"
path = Path(__file__).parent / f"{dir}/input.dat"

main(path)   

# exit(0)

dir = "data"
path = Path(__file__).parent / f"{dir}/input.dat"

main(path)