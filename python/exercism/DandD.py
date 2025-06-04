import math
import random

class Character:
    def __generate_score():
        die = [1, 2, 3, 4, 5, 6]
        return sum(sorted((random.choice(die) for i in range(4)), reverse=True)[:3])
# 
    def __init__(self):
        self.strength = self.__generate_score()
        self.dexterity = self.__generate_score()
        self.constitution = self.__generate_score()
        self.intelligence = self.__generate_score()
        self.wisdom = self.__generate_score()
        self.charisma = self.__generate_score()


def modifier(value):
    
    return math.floor((value - 10) / 2)


# print(modifier(9))



die = [1, 2, 3, 4, 5, 6]

roles = sum(sorted((random.choice(range(1, 7)) for i in range(4)), reverse=True)[:3])

for i in range(1, 20):
    print(random.randint(1, 6))

