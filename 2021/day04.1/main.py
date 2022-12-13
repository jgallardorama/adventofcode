import copy
from curses.ascii import isupper
from pathlib import Path
import string

import re
from typing import List, Optional


regex = r"move (?P<size>[0-9]*) from (?P<source>[0-9]*) to (?P<target>[0-9]*)"

def process_line(line: str):
    return "", 1
    pass

def load_numbers(file):
    line: str = file.readline()
    
    numbers = [ int(number) for number in line.rstrip("\n").split(",") ]
    return numbers

class Board:
    def __init__(self) -> None:
        self.row_index = 0
        self.numbers = {}
        self.row_counters = [0 for _ in range(0, 5)]
        self.column_counters = [0 for _ in range(0, 5)]

    def add_row(self, row):
        
        for index, value in enumerate(row):
            self.numbers[value] = (self.row_index, index, False)

        self.row_index += 1
        
    def mark(self, number):
        res_row = -1
        res_column = -1
        if number in self.numbers:
            cell_pos = self.numbers[number]
            x, y, _ = cell_pos
            self.numbers[number] = x, y, True
            self.row_counters[x] +=1
            self.column_counters[y] +=1
            
            if self.row_counters[x] == 5:
                res_row = x
            if self.column_counters[y] == 5:
                res_column = y
            
        return res_row, res_column
            
    def get_line(self, x, y):
        line = [0 for _ in range(0,5)]
        
        for key, value in self.numbers.items():
            c_x, c_y, _ = value
            if x==c_x:
                line[c_y] = key
            elif y==c_y:
                line[c_x] = key
                
        return line
    
    def sum_unmarket(self):
        result = 0
        for key, value in self.numbers.items():
            _, _, marked = value
            if not marked:
                result += key
                
        return result


def load_boards(file):

    boards = []    
    current_board = None
    while True:
        line: Optional[str] = file.readline()
        if line and line != "\n":
            if not current_board:
                current_board = Board()
                
            row = re.split(' +',line.rstrip("\n").lstrip(" ").rstrip(" "))
            row_numbers = [int(number) for number in row]
            current_board.add_row(row_numbers)
        else:
            if current_board:
                boards.append(current_board)
                current_board = None

        if not line:
            break

    return boards
    

def main(path):
    with open(path,"r") as file:

        numbers = load_numbers(file)
        
        boards = load_boards(file)
        
        all_boards = [board for board in boards]
        
        for number in numbers:
            board: Board
            for board in boards:
                row, column = board.mark(number)
                                
                if row>=0 or column>=0:
                    if board in all_boards:
                        all_boards.remove(board)
                        if len(all_boards) == 0:
                            
                    # line = board.get_line(row, column)
                    
                            res1 = board.sum_unmarket()
                            res2 = number
                            
                            print(f"RESULT: {res1} {res2} {res1 * res2}")
                    
                            return
        

dir = "data"
path = Path(__file__).parent / f"{dir}/input.dat"

main(path)            