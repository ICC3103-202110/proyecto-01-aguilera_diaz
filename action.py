import random

class Player():
    def __init__(self, name):
        self.name = name
        self.coins = 2
        self.influences = 2
        self.cards = []
    
    def __str__(self):
        return f"{self.name}: coins: {self.coins}"


class Foreign_Aid():
    def __init__(self):
         self.name = "foreign aid"
    def __str__(self):
        return "foreign aid"

    def __repr__(self):
        return "foreign aid"

    def play(self, player):
        
        player.coins += 2
        print("You gained 2 coins")
        print(player)

class Coup():
    def __init__(self):
         self.name = "coup"
    def __str__(self):
        return "coup"

    def __repr__(self):
        return "coup"

    def play(self, player, target):
        if player.coins < 7:
            print("Not enough coins")
            return False
        
        player.coins -= 7
        print("You payed 7 coins")
        print(player)
        print()
        print(f"These are your cards {target.name}")
        for index, card in enumerate(target.cards):
            print(f"{index}. {card}")
        print()
        i = int(input(f"What card you want to throw? {target.name} "))
        target.cards.pop(i)
        print(f"These is your deck now {target.name}, {target.cards} ")
    
        return True

        