class Captain():
    def __init__(self):
         self.name = "captain"

    def __str__(self):
        return "captain"

    def __repr__(self):
        return "captain"
    
    def action(self, player, target):
        
        if target.coins == 0:
            print("Player has 0 coins, failed to steal")
            return False
        if target.coins == 1:
            player.coins += 1
            target.coins -=1
            print("Sucess, You stole 1 coin")
            return True
        if target.coins >=2:
            player.coins += 2
            target.coins -= 2
            print("Sucess, you stole 2 coins")
            return True