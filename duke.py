class Duke():
    def __init__(self):
         self.name = "duke"

    def __str__(self):
        return "duke"

    def __repr__(self):
        return "duke"    

    def action(self, player):
        player.coins += 3
        print("You gained 3 coins")
        print(player)  
        return True