from random import *


results = []
results_str = []

#pick which two stats should be over 15:
over1 = randint(1,6)
over2 = randint(1,5)
if over1 <= over2:
    over2 += 1

for i in range(6):
    #for the ones guaranteed over 15, roll according to proper distribution
    if i+1==over1 or i+1==over2:
        roll = randint(1,20)
        if roll <= 10:
            results.append(15)
            results_str.append("15")
        elif roll <= 16:
            results.append(16)
            results_str.append("16")
        elif roll <= 19:
            results.append(17)
            results_str.append("17")
        else:
            results.append(18)
            results_str.append("18")
    else:
        dice = []
        for die in range(4):
            dice.append(randint(1, 6))
        dice.remove(min(dice))
        results.append(sum(dice))
        results_str.append( str(dice) + " " + str(sum(dice)) )
        

for result in results_str:
    print(result)

raw_input("exit?")
