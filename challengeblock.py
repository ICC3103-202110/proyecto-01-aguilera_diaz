from action import Player
import random
class Challengeblock():
    def __init__(self):
         self.name = "challengeblock"

    def __str__(self):
        return "challengeblock"

    def __repr__(self):
        return "challengeblock"    

    def action(self, player, totplayers, actcard, deck):
        counter = 0
        for index, j in enumerate(totplayers):
            if j != player and counter == 0:
                print()
                chall = input(f"{j}: Do you want to counterattack player {player.name}? (Y/N) ")
                if chall == "Y":
                    counter = 1
                    for i in range(len(player.cards)):
                        if actcard == str(player.cards[i]):
                            print(f"Player {player.name} has the card, {j.name} you lost the challenge")
                            print()
                            chall = "OK"
                            return "has the card"
            
                    if chall == "OK":
                        break

                    print(f"Player {player.name} does not have the card, {j.name} wins the counterattack")
                    return "not have card"
                else:
                    continue
        
        print()
        return True

