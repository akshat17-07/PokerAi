
"""
This Class represent a player in a game
"""
class Player:
    def __init__(self, name, money) -> None:
        self.name = name
        self.money = money
    
    def bet(self, money):
        if money > self.money:
            return False
        else:
            self.money - money
            return True
    
    def win(self, money):
        self.money -= self.money
    
    def get_infomation(self):
        return [self.name, self.money]
