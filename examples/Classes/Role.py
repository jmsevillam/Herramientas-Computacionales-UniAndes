# This code was written during the course
# "Herramientas computacionales" at Uniandes
# Mauricio Sevilla. email: j.sevillam@uniandes.edu.co

import random as rn
# This code is a role game
class Character:
    #creator
    def __init__(self,name,race,power,level,location):
        #save the variables
        self.name=name
        self.race=race
        self.power=power
        self.level=level
        self.loc=location
    def Move(self):
        #Moves randomly
        location=['N','S','E','W']
        self.loc=location[rn.randint(0, 3)]
    def fight(self):
        #if it fights, half probability to win and half to lose
        r=rn.random()
        if r>0.5:
            print('Win')
        else:
            print('lose')
#I create myself
me=Character('Yo','Human',10,1,'N')
#ask for location
print(me.loc)
me.Move() #moves
print(me.loc)
#Ask for fight result
me.fight()
