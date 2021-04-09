
class Player():
    def __init__(self, cards, name):
        self.name = name
        self.coins = 2
        self.__cards = []
    
    def __str__(self):
        return f"{self.name}: monedas: {self.coins}"
   
        
