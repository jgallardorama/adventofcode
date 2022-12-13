from curses.ascii import isupper
from pathlib import Path
import string

import re

regex = r"(?P<a_minior>[0-9]*)-(?P<a_major>[0-9]*),(?P<b_minior>[0-9]*)-(?P<b_major>[0-9]*)"

def overlap(a_minior, a_major, b_minior, b_major):
    result = (a_minior <= b_minior and b_minior <= a_major) or (a_minior <= b_major and b_major <= a_major)
    return result

def check_sections(a_minior, a_major, b_minior, b_major):
    result = overlap(a_minior, a_major, b_minior, b_major) or overlap(b_minior, b_major, a_minior, a_major)
    return result

def main():
    path = Path(__file__).parent / "input.dat"

    trucks = []
    result = 0

    with open(path,"r") as file:

        while True:
            line = file.readline()            
            if not line:
                break

            match = re.search(regex, line)
            if match:
                a_minior = int(match.group("a_minior"))
                a_major = int(match.group("a_major"))
                b_minior = int(match.group("b_minior"))
                b_major = int(match.group("b_major"))
                
                print(f"{line} = {a_minior}, {a_major}, {b_minior}, {b_major}")
                if check_sections(a_minior, a_major, b_minior, b_major):
                    print("MATCH")
                    result +=1
                    
    print(result)
    
    
main()