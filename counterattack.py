from action import Player
from challenge import Challenge
from challengeblock import Challengeblock
import random

class Counterattack():
    def __init__(self):
         self.name = "counterattack"

    def __str__(self):
        return "counterattack"

    def __repr__(self):
        return "counterattack"    

    def action(self, player, totplayers, actcard, deck):
        counter = 0
        for index, j in enumerate(totplayers):
            if j != player and counter == 0:
                print()
                cattack = input(f"{j}: Do you want to counterattack player {player.name}? (Y/N) ")
                if cattack == "Y":
                    counter = 1
                    if actcard == "foreign aid":
                        actcardp2 = "duke"
                        challengep2 = Challengeblock()
                        cha = challengep2.action(j, totplayers, actcardp2, deck)
                        return cha
                    
                    elif actcard == "assassin":
                        actcardp2 = "countess"
                        challengep2 = Challengeblock()
                        cha = challengep2.action(j, totplayers, actcardp2, deck)
                        return cha

                    elif actcard == "captain":
                        actcardp2 = "captain"
                        challengep2 = Challengeblock()
                        cha = challengep2.action(j, totplayers, actcardp2, deck)
                        return cha
                

                else:
                    continue
        
        print()
        return True