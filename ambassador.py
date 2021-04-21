import random

class Ambassador():
    def __init__(self):
         self.name = "ambassador"

    def __str__(self):
        return "ambassador"

    def __repr__(self):
        return "ambassador"
    
    def action(self, player, deck):
        
        print("These are your cards ")
        print(player.cards)
        listcardplayer = list(player.cards)
        
        
        newcards = []
        newplayercards = []
        for p in range(2):
            index = random.randint(0, (len(deck) - 1))
            card = deck.pop(index)
            newcards.append(card)
        print("You took these 2 cards from the deck ")
        print(newcards)
        
        newplayercards.append(listcardplayer[0])
        newplayercards.append(listcardplayer[1])
        newplayercards.append(newcards[0])
        newplayercards.append(newcards[1])
        print()
        for i in range(len(newplayercards)):
            print(f"{i}: {newplayercards[i]}")
        newi = int(input(("Choose your first card: ")))
        newi2 = int(input("Choose your second card: "))

        listcardplayer.pop()
        listcardplayer.pop()
        listcardplayer.append(newplayercards[newi])
        listcardplayer.append(newplayercards[newi2])
        player.cards = list(listcardplayer)
        print(f"These is your new deck {player.name}, {player.cards}")
        return True
