from curses.ascii import isupper
from pathlib import Path
import string

import re
from typing import List


regex = r"Monkey (?P<id>.*):\n  Starting items: (?P<items>.*)\n  Operation: new = old (?P<op>.*) (?P<op_val>.*)\n  Test: divisible by (?P<test>.*)\n    If true: throw to monkey (?P<if_true>.*)\n    If false: throw to monkey (?P<if_false>.*)"

def process_line(line: str):
    return "", 1
    pass

class Monkey():
    def __init__(self, id, items, op, op_val, test, if_true, if_false) -> None:
        self.id = id
        self.items = items
        self.op = op
        self.op_val = op_val
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.counter = 0
        pass
    
    def calc_worry_level(self, item, op, op_val):
        result = item
        
        if op_val == "old":
            op_val = item
        else:
            op_val = int(op_val)
            
        
        if op == "*":
            result = item * op_val
        elif op == "+":
            result = item + op_val        
        return result
    
    
    def inspect(self):
        result = []
        next_items = []
        print(f"Monkey {self.id}")
        for item in self.items:
            print(f"  Monkey inspects an item with a worry level of {item}.")
            worry_level = self.calc_worry_level(item, self.op, self.op_val)
            print(f"    Worry level is {self.op} by {self.op_val} to {worry_level}.")
            
            next_worry_level = int(worry_level / 3)
            print(f"    Monkey gets bored with item. Worry level is divided by 3 to {next_worry_level}.")
            
            test_result = next_worry_level % self.test
            if test_result == 0:
                next_monkey = self.if_true
            else:
                next_monkey = self.if_false

            if next_monkey != self.id:
                result.append((next_worry_level, next_monkey))
            else:
                next_items.append(next_worry_level)
                
            print(f"    Item with worry level {next_worry_level} is thrown to monkey {next_monkey}.")
            
            self.counter += 1
                
        self.items = next_items
        
        return result
        
    def add_item(self, item):
        self.items.append(item)
        
    def print_status(self):
        items_str = ', '.join(map(str, self.items))
        print(f"Monkey {self.id}: {self.counter}: {items_str}")

    def __str__(self):
        result = f"id {self.id}\n" + \
        f"items: {self.items}\n" + \
        f"op: {self.op}\n" + \
        f"op_val: {self.op_val}\n" + \
        f"test: {self.test}\n" + \
        f"if_true: {self.if_true}\n" + \
        f"if_false: {self.if_false}\n"         
        return result

def read_paragraph(file):
    result = ""
    
    while True:
        line = file.readline()
        if not line or line == "\n":
            break
        result +=line

    return result, line == ''

def load_monkeys(path):
    result = []
    with open(path,"r") as file:
        while True:
            monkey_lines, EOF = read_paragraph(file)
            if monkey_lines:
                match = re.search(regex, monkey_lines)
                if match:
                    id = match.group("id")
                    items = match.group("items")
                    op = match.group("op")
                    op_val = match.group("op_val")
                    test = int(match.group("test"))
                    if_true = int(match.group("if_true"))
                    if_false = int(match.group("if_false"))
                    
                    items_vals = [int(item) for item in items.split(",")]
                    monkey = Monkey(id, items_vals, op, op_val, test, if_true, if_false)
                    result.append(monkey)

            if EOF:
                break

    return result

def round(monkeys):
    for monkey in monkeys:
        thrown_items = monkey.inspect()
        for item in thrown_items:
            worry_level, monkey_id = item
            monkeys[monkey_id].add_item(worry_level)

def main(path):
    monkeys = load_monkeys(path)
    
    for monkey in monkeys:
        print(monkey)
    
    for round_ix in range(0, 20):
        round(monkeys)
        
        print(f"Round {round_ix + 1}")
        monkey: Monkey
        for monkey in monkeys:
            monkey.print_status()
            
        pass
    
    print("===== SORTED =====")
    sorted_monkeys = sorted(monkeys, key=lambda x: x.counter, reverse=True)
    for monkey in sorted_monkeys:
        monkey.print_status()

dir = "data"
path = Path(__file__).parent / f"{dir}/input.dat"

main(path)            