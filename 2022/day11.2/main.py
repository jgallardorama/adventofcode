from curses.ascii import isupper
import math
from pathlib import Path
import string

import re
from typing import List


regex = r"Monkey (?P<id>.*):\n  Starting items: (?P<items>.*)\n  Operation: new = old (?P<op>.*) (?P<op_val>.*)\n  Test: divisible by (?P<test>.*)\n    If true: throw to monkey (?P<if_true>.*)\n    If false: throw to monkey (?P<if_false>.*)"

def log_print(message):
    # print(message)
    pass

class Item():
    def __init__(self, value) -> None:
        self._value = value
    
    def add(self, val, mod):
        self._value = (self._value + val) % mod
    

    def mul(self, val, mod):
        self._value = (self._value * val) % mod
        
    def get_value(self):
        return self._value
    
    def calc(self, op, op_val, mod):        
        if op_val == "old":
            op_val = self.get_value()
        else:
            op_val = int(op_val)
            
        if op == "*":
            self.mul(op_val, mod)
        elif op == "+":
            self.add(op_val, mod)
            
    def check(self, mod):
        return self._value % mod == 0




class Monkey():
    def __init__(self, id, items, op:str, op_val:str, test_mod: int, if_true:int, if_false: int) -> None:
        self.id = id
        self.items = items
        self.op = op
        self.op_val = op_val
        self.test_mod = test_mod
        self.if_true = if_true
        self.if_false = if_false
        self.counter = 0
        pass
    
    def inspect(self, mod: int):
        result = []
        next_items = []
        log_print(f"Monkey {self.id}")
        item:Item
        for item in self.items:
            log_print(f"  Monkey inspects an item with a worry level of {item}.")
            item.calc(self.op, self.op_val, mod)
            log_print(f"    Worry level is {self.op} by {self.op_val} to {item.get_value()}.")
                        
            test_result = item.check(self.test_mod)
            if test_result:
                next_monkey = self.if_true
            else:
                next_monkey = self.if_false

            if next_monkey != self.id:
                result.append((item, next_monkey))
            else:
                next_items.append(item)
                
            log_print(f"    Item with worry level {item.get_value()} is thrown to monkey {next_monkey}.")
            
            self.counter += 1

        self.items = next_items
        
        return result
        
    def add_item(self, item):
        self.items.append(item)
        
    def print_status(self):
        # items_str = ', '.join(map(str, self.items))
        print(f"Monkey {self.id}: {self.counter}")

    def __str__(self):
        result = f"id {self.id}\n" + \
        f"items: {self.items}\n" + \
        f"op: {self.op}\n" + \
        f"op_val: {self.op_val}\n" + \
        f"test: {self.test_mod}\n" + \
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
                    
                    items_vals = [Item(int(item)) for item in items.split(",")]
                    monkey = Monkey(id, items_vals, op, op_val, test, if_true, if_false)
                    result.append(monkey)

            if EOF:
                break

    return result

def round(monkeys):
    
    mod = math.prod([monkey.test_mod for monkey in monkeys])
    
    for monkey in monkeys:
        thrown_items = monkey.inspect(mod)
        for item in thrown_items:
            worry_level, monkey_id = item
            monkeys[monkey_id].add_item(worry_level)

def main(path):
    monkeys = load_monkeys(path)
    
    for monkey in monkeys:
        print(monkey)
    
    for round_ix in range(0, 10000):
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