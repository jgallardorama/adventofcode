from curses.ascii import isupper
from pathlib import Path

from typing import List

def begin_stream(line: str, size_begin_marker = 4):
    result = 0
    print(line)
    index = 0
    
    marker = []
    for item in line:
        print(f"{index} {item} {marker}")
        
        if item in marker:
            pos = marker.index(item)
            marker = marker[pos+1:len(marker)]
        
        marker.append(item)
        size = len(marker)
        if size == size_begin_marker:
            result = index + 1
            break
        else:
            if size >= size_begin_marker:
                marker = marker[1:size_begin_marker]
    
            
        
        index += 1

    
    return marker, result


def main(path):
    with open(path,"r") as file:

        while True:
            line = file.readline()            
            if not line:
                break
            
            marker, result = begin_stream(line, size_begin_marker= 14)
            print(marker, result)
            
dir = "data"
path = Path(__file__).parent / f"{dir}/input.dat"

main(path)            