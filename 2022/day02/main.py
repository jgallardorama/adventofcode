

from pathlib import Path

def calc_score(line):
    
    # A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.
    # The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.
    scores = {
        "A X": 1 + 3,
        "A Y": 2 + 6,
        "A Z": 3 + 0,
        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 1 + 6,
        "C Y": 2 + 0,
        "C Z": 3 + 3,
    }
    
    
    result = scores[line[0:3]]
    return result


def calc_score_2(line):
    
    # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
    # A=1 B=2 C=3
    # A for Rock, B for Paper, and C for Scissors.
    scores = {
        "A X": 0 + 3,
        "A Y": 3 + 1,
        "A Z": 6 + 2,
        "B X": 0 + 1,
        "B Y": 3 + 2,
        "B Z": 6 + 3,
        "C X": 0 + 2,
        "C Y": 3 + 3,
        "C Z": 6 + 1,
    }
    
    
    result = scores[line[0:3]]
    return result


def main():
    path = Path(__file__).parent / "input.dat"

    elfs = []

    score = 0
    score_2 = 0

    with open(path,"r") as file:

        while True:
            line = file.readline()
            if not line:
                break
            
            score += calc_score(line)
            score_2 += calc_score_2(line)
            

    print(score)
    print(score_2)
    
main()