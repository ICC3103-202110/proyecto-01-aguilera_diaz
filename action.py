

class Action():
    coinsneeded = 0 #coins needed for doing the action
    blocks = [] 
    hastarget = False

class Income(Action):
    def play(self, player, target = None):
        player.coins += 1
        return True