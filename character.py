class Character(object):
    def __init__(self):
        self.health = 10
        self.power = 5
        self.attack_string = ''
        self.print_status_string = ''
        self.win_string = ''

    def alive(self):
        return self.health > 0
    
    def attack(self, enemy):
        enemy.health -= self.power
        print(self.attack_string % self.power)
        if enemy.health <= 0:
            print(self.win_string)

    def print_status(self):
        print(self.print_status_string % (self.health, self.power))

