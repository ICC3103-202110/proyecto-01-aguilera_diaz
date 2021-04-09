import random

class Player():
    def __init__(self, cards, name):
        self.name = name
        self.coins = 2
        self.__cards = []
    
    def __str__(self):
        return f"{self.name}: monedas: {self.coins}"
   
class Duke():
    def __init__(self):
         self.name = "duke"

    def __str__(self):
        return "duke"

    def __repr__(self):
        return "duke"    

    def accion(self, player):
        player.coins += 3
        print("You added 3 coins")
        print(player)   
cards = []
while True:
    for i in range(1):
        duke = Duke()
        cards.append(duke)
    print(cards)
    break