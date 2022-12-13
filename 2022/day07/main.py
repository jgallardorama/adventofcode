from curses.ascii import isupper
from pathlib import Path
import string

import re
from typing import List


regex = r"move (?P<size>[0-9]*) from (?P<source>[0-9]*) to (?P<target>[0-9]*)"

class Node:
    def __init__(self, name: str, parent = None, size:int = -1) -> None:
        self.children = {}
        self.name=name
        self.size = size
        self.parent = parent
        
    def child(self, name, size=-1):        
        if name in self.children:
            result = self.children[name]
        else:
            result = Node(name, self, size)
            self.children[name] = result
        return result
    
    def get_total_size(self):
        if self.size < 0:
            result = sum(child.get_total_size() for _, child in self.children.items())
        else:
            result = self.size
        return result
    
    def __str__(self):        
        result = f"{self.name} : {self.size}"
        return result
    
    def get_fullname(self):
        result = self.name
        if self.parent:
            result = self.parent.get_fullname() + "/" + result
        else:
            result = "/"
        return result
    

def process_line(current_node: Node, line: str):
    next_node = current_node
    segments = line.rstrip("\n").split(" ")
    if segments[0] == "$":
        if segments[1] == "cd":
            arg = segments[2]
            if arg == "..":
                next_node = current_node.parent
            elif arg == "/":
                pass
            else:
                next_node = current_node.child(arg)
        elif segments[1] == "ls":
            pass
    elif segments[0] == "dir":
        dirname = segments[1]
        ## add directory
        current_node.child(dirname)        
    else:
        filename = segments[1]
        ## add file
        size = int(segments[0])
        current_node.child(filename, size)
            
    return next_node

def calc_nodes(node: Node):
    fullname = node.get_fullname()
    # print(f"Calc Node {fullname}")
    result = []
    
    sum = 0
    for key, child in node.children.items():
        child_result = calc_nodes(child) 
        result.extend(child_result)
        
    result.append(node)

    print(f"{fullname} {node.get_total_size()}")
        
    return result

def build_node(file, node):
    file.write("$ ls\n")
    for _, child in node.children.items():
        if child.size == -1:
            file.write(f"dir {child.name}\n")
        else:
            file.write(f"{child.size} {child.name}\n")
            
    for _, child in node.children.items():
        if child.size == -1:
            file.write(f"$ cd {child.name}\n")
            build_node(file, child)
    
    file.write("$ cd ..\n")

def main(path):
    with open(path,"r") as file:
        root_node = Node("/")
        current_node = root_node
        while True:
            line = file.readline()            
            if not line:
                break
            
            current_node = process_line(current_node, line)
            print(current_node)

    
    list_nodes = calc_nodes(root_node)
    
    print(f"ROOT {root_node.get_total_size()}")
    
    sorted(list_nodes, key=Node.get_total_size)
    result = 0

    total_disk_space = 7*10**7
    desired_free_disk_space = 3*10**7

    free_space = total_disk_space - root_node.get_total_size()
    needed_for_update = desired_free_disk_space - free_space
    
    print(f"needed_for_update {needed_for_update}")

    dirs = []
    for node in list_nodes:
        size = node.get_total_size()
        if size > needed_for_update:
            print(f">> {node.get_fullname()} {size}")            
            dirs.append(size)
            
    sorted_dirs = sorted(dirs)
    print(f"RESULT = {sorted_dirs[0]}")

    with open("output.txt","w") as file:
        build_node(file, root_node)
        
    
        
dir = "sample"
path = Path(__file__).parent / f"{dir}/input.dat"

main(path)

dir = "data"
path = Path(__file__).parent / f"{dir}/input.dat"

main(path)