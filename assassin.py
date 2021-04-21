class Assassin():
    def __init__(self):
         self.name = "assassin"

    def __str__(self):
        return "assassin"

    def __repr__(self):
        return "assassin"    

    def action(self, player, target):
        if player.coins < 3:
            print("Not enough coins")
            return False
        
        player.coins -= 3
        print("You payed 3 coins")
        print(player)  
        for index, card in enumerate(target.cards):
            print(f"{index}. {card}")
        print()
        i = int(input(f"What card you want to throw? {target.name} "))
        target.cards.pop(i)
        print(f"These is your deck now {target.name}, {target.cards} ")
        target.influence = len(target.cards)
        return True