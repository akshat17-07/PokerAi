"""
This Class represent a player in a game
"""
class Player:
    def __init__(self, name, money, type) -> None:
        self.name = name
        self.money = money
        self.status = 0
        self.type = type
    
    def bet(self, money):
        if money > self.money:
            return False
        else:
            self.money - money
            return True
    
    def win(self, money):
        self.money += self.money
    
    def get_infomation(self):
        return [self.name, self.money]
    
    def change_status(self, status):
        """
        fold = 0
        in_game = 1
        the game would keep track of rasies and blinds
        """
        self.status = status
    
    def get_status(self):
        return self.status

    def get_type(self):
        """
        0: human
        1: AI
        """
        return self.type