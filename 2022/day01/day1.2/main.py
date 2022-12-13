

from pathlib import Path


path = Path(__file__).parent / "data.lst"

elfs = []

with open(path,"r") as file:

    current_elf_index = 0 
    current_elf_calories = 0
    max_elf_calories= 0
    while True:
        line = file.readline()    
        if line:
            if line != '\n':
                current_elf_calories += int(line)
            else:
                elfs.append(current_elf_calories)

                print(f"{current_elf_index} = {current_elf_calories}")
                current_elf_calories = 0
                current_elf_index += 1
        else:
            break
        
    elfs.sort(reverse = True)
    
    for index in range(0,3):
        print(elfs[index])

    result = sum(elfs[0:3])
    print (result)
