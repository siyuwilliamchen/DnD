import numpy as np 
import random

def d20(adv = False, disadv = False):
    primaryRoll = random.randint(1,20)
    secondRoll = random.randint(1,20)
    advRoll = np.max(primaryRoll, secondRoll)
    disadvRoll = np.min(primaryRoll, secondRoll)
    if adv and disadv:
        return primaryRoll
    elif adv:
        return advRoll
    elif disadv:
        return disadvRoll
    else:
        return primaryRoll

def d(n, count = 1):
    result = 0
    for i in range(0,n):
        result += random.randint(1, n)
    return result

    