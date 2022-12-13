from curses.ascii import isupper
from pathlib import Path
import string

import re
from typing import List


regex = r"move (?P<size>[0-9]*) from (?P<source>[0-9]*) to (?P<target>[0-9]*)"

def process_line(line: str):
    return "", 1
    pass



def load(path):
    map = None
    with open(path,"r") as file:
        row = 0
        while True:
            line = file.readline()            
            if not line:
                break
            
            line = line.rstrip("\n")
            
            if map == None:
                size = len(line)
                map = [[0 for x in range(size)] for y in range(size)]
            
            column = 0
            for c in line:
                map[row][column] = int(c)
                
                column += 1
            
            row +=1
    return map

class MatrixIterator:
    def __init__(self, size, dir) -> None:
        self.size = size
        self.dir = dir
        

    def calc_pos(self, i, j):
        res_i = i
        res_j = j

        if self.dir == 1:
            res_i = j
            res_j = i
        elif self.dir == 2:
            res_i = i
            res_j = (self.size -1) - j
        elif self.dir == 3:
            res_i = (self.size -1) - j
            res_j = i
            
        return res_i, res_j

def calc(map, dir, count_map):
    result = 0
    size = len(map)
    
    result = 0
    
    miter = MatrixIterator(size, dir)
    
    
    for i in range(0, size):
        last = -1
        for j in range(0, size):
            d_i , d_j = miter.calc_pos(i, j)
            val = map[d_i][d_j]
            if last < val:
                last = val
                repe = "REPE"
                if count_map[d_i][d_j] == 0:
                    result += 1
                    count_map[d_i][d_j] = 1
                    repe = "+1"
                    
                print(f"{d_i} {d_j} -> {val} {repe}")
            elif last == val:
                print(f"SKIP {d_i} {d_j} -> {val}")                

    return result

def main_8(path):
    map = load(path)
    total = 0
    size = len(map)
    count_map = [[0 for x in range(size)] for y in range(size)]

    for dir in [0,1,2,3]:
        result = calc(map, dir, count_map)
        print(f"==== {dir}, {result}")
        total += result
        
    print(count_map) 
    
    for line in count_map:
        print("".join(str(e) for e in line))   
    
    print(f"total {total}")

def calc_view(map, i, j, size, dir):
    result = 0

    val_ref = map[i][j]

    delta_i = -1
    delta_j = 0

    if dir == 1:
        delta_i = 1
        delta_j = 0
    elif dir == 2:
        delta_i = 0
        delta_j = -1
    elif dir == 3:
        delta_i = 0
        delta_j = +1

    ix = i
    jx = j
    print(f">> {ix}:{jx} {val_ref}")

    while True:
        ix += delta_i
        jx += delta_j
    
        if ix < 0 or ix >= size or jx < 0 or jx >= size:
            break
    
        val = map[ix][jx]
        print(f"  {ix}:{jx} {val}")
        result+=1
        if val_ref <= val:
            break
    return result



def main(path):
    map = load(path)
    size = len(map)
    max = 0
    for i in range(1, size-1):
        last = -1
        for j in range(1, size-1):
            print(f"======== {i}:{j} =============")
            up = calc_view(map, i, j, size, 0)
            down = calc_view(map, i, j, size, 1)
            right = calc_view(map, i, j, size, 2)
            left = calc_view(map, i, j, size, 3)
            
            print(f"=== RES {i} {j} {up} {down} {right} {left}")
            res = up * down * right * left
            
            if res > max:
                max = res
                
    print(f"max {max}")
            
dir = "data"
path = Path(__file__).parent / f"{dir}/input.dat"

main(path)