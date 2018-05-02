from character import Character

class Goblin(Character):
    def __init__(self):
        self.health = 6
        self.power = 2
        self.attack_string = 'The goblin does %d damage to you.'
        self.print_status_string = 'The goblin has %d health and %d power.' 
        self.win_string = 'You are dead.'
