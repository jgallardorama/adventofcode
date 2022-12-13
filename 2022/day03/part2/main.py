from curses.ascii import isupper
from pathlib import Path
import string


def get_priority(item):
    delta = 0
    if isupper(item):
        delta = 26
    
    value = ord(str.lower(item)) - (ord("a") - 1) + delta    
    
    return value

def main():
    path = Path(__file__).parent / "input.dat"

    trucks = []
    result = 0

    with open(path,"r") as file:

        while True:
            line = file.readline()            
            if not line:
                break
            
            trucks.append(str.rstrip(line))
            
    group_index = 0
    while True:
        
        if group_index * 3 >= len(trucks):
            break

        truck1 = trucks[group_index*3 + 0]
        truck2 = trucks[group_index*3 + 1]
        truck3 = trucks[group_index*3 + 2]
        
        intersect = set(truck1).intersection(set(truck2)).intersection(set(truck3))
            
        item = list(intersect)[0]

        priority = get_priority(item)
        print(f"{truck1}:{truck2}:{truck3} = {item} {priority}")
        
        result += priority
        
        group_index+=1
            
    print(result)
main()