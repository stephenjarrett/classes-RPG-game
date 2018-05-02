from character import Character

class Hero(Character):
    def __init__(self):
        self.health = 10
        self.power = 5
        self.attack_string = 'You do %d damage to the goblin.'
        self.print_status_string = 'You have %d health and %d power.'
        self.win_string = 'The goblin is dead.'
    
    

