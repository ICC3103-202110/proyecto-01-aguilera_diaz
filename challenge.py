from action import Player
import random
class Challenge():
    def __init__(self):
         self.name = "challenge"

    def __str__(self):
        return "challenge"

    def __repr__(self):
        return "challenge"    

    def action(self, player, totplayers, actcard, deck):
        counter = 0
        for index, j in enumerate(totplayers):
            if j != player and counter == 0:
                print()
                chall = input(f"{j}: Do you want to challenge player {player.name}? (Y/N) ")
                if chall == "Y":
                    counter = 1
                    for i in range(len(player.cards)):
                        if actcard == str(player.cards[i]):
                            print(f"Player {player.name} has the card, {j.name} you lost the challenge")
                            for index, card in enumerate(j.cards):
                                print(f"{index}. {card}")
                            print()
                            i = int(input(f"What card you want to throw? {j.name} "))
                            j.cards.pop(i)
                            listcardplayer = list(player.cards)
                            newcard = []
                            for p in range(1):
                                index = random.randint(0, (len(deck) - 1))
                                card = deck.pop(index)
                                newcard.append(card)
                            print(f"{player.name} You took these card from the deck")
                            print(newcard)
                            newplayercards = []
                            newplayercards.append(listcardplayer[0])
                            newplayercards.append(listcardplayer[1])
                            newplayercards.append(newcard[0])
                            
                            
                            for i in range(len(newplayercards)-1):
                                if actcard == str(newplayercards[i]):
                                    newplayercards.pop(i)
                                    player.cards = list(newplayercards)
                                    chall = "OK"
                                    return "win challenge"
                                    
                                else:
                                    continue
                            
                        
                    if chall == "OK": #condition to differ if the player already lost the card
                        break
                    print(f"Player {player.name} does not have the card, {j.name} wins the challenge")
                    for index, card in enumerate(player.cards):
                        print(f"{index}. {card}")
                    print()
                    i = int(input(f"What card you want to throw? {player.name} "))
                    player.cards.pop(i)
                    return "lost challenge"
        
                else:
                    continue
        print()
        return True