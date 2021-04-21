import random
from action import Player, Foreign_Aid, Coup
from challenge import Challenge
from counterattack import Counterattack
from duke import Duke
from countess import Countess
from assassin import Assassin
from captain import Captain
from ambassador import Ambassador
class Game():
    def __init__(self):
        self.players = []
        self.cards = []
    
    def initialice_names(self):
        cant = int(input("amount of players? (3-4) "))
        for i in range(cant):
            name_player = input(f"Write your name {i}: ")
            player = Player(name_player)
            self.players.append(player)
    
    def initialice_cards(self):
        for i in range(3):
            duke = Duke()
            assassin = Assassin()
            ambassador = Ambassador()
            countess = Countess()
            captain = Captain()
            self.cards.append(duke)
            self.cards.append(assassin)
            self.cards.append(ambassador)
            self.cards.append(countess)
            self.cards.append(captain)
        random.shuffle(self.cards)

    def give_cards(self):
        for player in self.players*2:
            index = random.randint(0, (len(self.cards) - 1))
            card = self.cards.pop(index)
            player.cards.append(card)
            
        for player in self.players:
            print(f"{player.name}: {player.cards}")
            input("next turn (press enter)")
    
    def play_cards(self, player):
            print("0: duke")
            print("1: assassin")
            print("2: captain")
            print("3: ambassador")
            card = int(input("What card you want to play? "))
    
            if card == 0: 
                actcard = "duke"
                duke = Duke()
                listcardsplayer = list(player.cards)
                deck = self.cards
                challengep1 = Challenge()
                challengep1.action(player, self.players, actcard, deck)
                if range(len(listcardsplayer)) == range(len(player.cards)): #condition to see if player has the same cards before the challenge
                    answer = duke.action(player)
                else:
                    print(f"{player.name} you lost your turn")
                    player.influence = len(player.cards)
                    if player.influence == 0:
                        self.players.remove(player)
                    answer = True
            if card == 1:
                actcard = "assassin"
                assassin = Assassin()
                listcardsplayer = list(player.cards)
                deck = self.cards

                challengep1 = Challenge()
                challenge = challengep1.action(player, self.players, actcard, deck)
                
                if challenge == "lost challenge":
                    print(f"{player.name} you lost your turn")
                    player.influence = len(player.cards)
                    if player.influence == 0:
                        self.players.remove(player)
                    answer = True
                
                counterattackp1 = Counterattack()
                cha = counterattackp1.action(player, self.players, actcard, deck)

                if cha == "has the card":
                    print(f"{player.name} you lost your turn, they blocked your foreign aid")
                    answer = True
                else:
                    print("Sucess, they didn´t block you")
                    if range(len(listcardsplayer)) == range(len(player.cards)):
                        print("In what player do you want to use the card assassin: ")
                        opcions = []
                        for index, j in enumerate(self.players):
                            if j != player:
                                print(f"{index}. {j}")
                                opcions.append(index)
                        print()
                        player_index = int(input("What player you want to assassin? "))
                        targassassin = self.players[player_index]
                        assassin = Assassin()
                        answer = assassin.action(player, targassassin)
                    else:
                        print(f"{player.name} you lost your turn")
                        player.influence = len(player.cards)
                        if player.influence == 0:
                            self.players.remove(player)
                        answer = True
            
            if card == 2:
                actcard = "captain"
                captain = Captain()
                listcardsplayer = list(player.cards)
                deck = self.cards

                challengep1 = Challenge()
                challenge = challengep1.action(player, self.players, actcard, deck)

                if challenge == "lost challenge":
                    print(f"{player.name} you lost your turn")
                    player.influence = len(player.cards)
                    if player.influence == 0:
                        self.players.remove(player)
                    answer = True

                counterattackp1 = Counterattack()
                cha = counterattackp1.action(player, self.players, actcard, deck) 

                if cha == "has the card":
                    print(f"{player.name} you lost your turn, they blocked your foreign aid")
                    answer = True
                else:
                    print("Sucess, they didn´t block ")
                    if range(len(listcardsplayer)) == range(len(player.cards)):
                        print("To what player do you want to use the card: ")
                        opcions = []
                        for index, j in enumerate(self.players):
                            if j != player:
                                print(f"{index}. {j}")
                                opcions.append(index)
                        print()
                        player_index = int(input("What player you want to steal? "))
                        targcaptain = self.players[player_index]
                        captain = Captain()
                        answer = captain.action(player, targcaptain)
                    else:
                        print(f"{player.name} you lost your turn")
                        player.influence = len(player.cards)
                        if player.influence == 0:
                            self.players.remove(player)
                        answer = True
            if card == 3:
                actcard = "ambassador"
                ambassador = Ambassador()
                listcardsplayer = list(player.cards)
                deck = self.cards
                challengep1 = Challenge()
                challengep1.action(player, self.players, actcard, deck)
                if range(len(listcardsplayer)) == range(len(player.cards)):
                    answer = ambassador.action(player, deck)
                else:
                    print(f"{player.name} you lost your turn")
                    player.influence = len(player.cards)
                    if player.influence == 0:
                        self.players.remove(player)
                    answer = True
            return answer
    def play(self):
        self.initialice_names()
        self.initialice_cards()
        self.give_cards()
        playing = 0
        while playing == 0:
            for p in self.players:
                answer = False
                while not answer: 
                    print()
                    print("1. Play Card")
                    print("2. Income")
                    print("3. Foreign Aid")
                    print("4. Coup")
                    print("5. See your cards")
                    print("8. Quit Game")
                    print()
                    action = int(input(f"What action do you want to do {p.name}?: "))
                    if action == 1:
                        answer = self.play_cards(p)
                    elif action == 2:
                        p.coins += 2
                        print()
                        print("You gained 2 coins")
                        print(f"{p.name}: coins: {p.coins}")
                        print()
                        answer = True
                    elif action == 3:
                        print()
                        actcard = "foreign aid"
                        listcardsplayer = list(p.cards)
                        deck = self.cards
                        counterattackp1 = Counterattack()
                        cha = counterattackp1.action(p, self.players, actcard, deck)
                        
                        if cha == "has the card":
                            print(f"{p.name} you lost your turn, they blocked your foreign aid")
                            answer = True
                        else:
                            FA = Foreign_Aid()
                            FA.play(p)
                            print()
                            answer = True
                    
                    elif action == 4:
                        print()
                        coup = Coup()
                        print("In what player do you want to use the card: ")
                        opcions = []
                        for index, j in enumerate(self.players):
                            if j != p:
                                print(f"{index}. {j}")
                                opcions.append(index)
                        print()
                        player_index = int(input("What player you want to coup? "))
                        targetcoup = self.players[player_index]
                        coupp1 = coup.play(p, targetcoup)
                        print()
                        if coupp1 == True:
                            answer = True
                        else:
                            answer = False
                    elif action == 5:
                        print(p.cards)
                    elif action == 8:
                        playing = 1
                        break
                    if len(self.players) == 1:
                        print(f"The winner is {p.name}")
                        playing = 1
                        break

game = Game()
game.play()
    
