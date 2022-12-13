from curses.ascii import isupper
from pathlib import Path
import string


def main():
    path = Path(__file__).parent / "input.dat"

    elfs = []
    result = 0

    with open(path,"r") as file:

        while True:
            line = file.readline()            
            if not line:
                break
            
            size = len(line[0:-1])
            half = int(size/2)
            container1 = line[0:half]
            container2 = line[half:size]
            
            intersect = set(container1).intersection(set(container2))
            
            item = list(intersect)[0]
            
            delta = 0
            if isupper(item):
                delta = 26
            
            value = ord(str.lower(item)) - (ord("a") - 1) + delta

            print(f"{container1}:{container2} = {item} {value}")
            
            result += value
            
    print(result)
main()