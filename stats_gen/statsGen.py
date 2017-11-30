from random import *

reroll = True
while (reroll):
    results = []
    results_str = []
    for i in range(6):
        dice = []
        for die in range(4):
            dice.append(randint(1, 6))
        dice.remove(min(dice))
        results.append(sum(dice))
        results_str.append( str(dice) + " " + str(sum(dice)) )
        
    num_high = 0
    for res in results:
        if res >= 15:
            num_high += 1
    if (num_high >= 2):
        reroll = False
    if (not reroll):
        for result in results_str:
            print(result)

raw_input("exit?")
