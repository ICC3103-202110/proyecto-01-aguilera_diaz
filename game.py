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
