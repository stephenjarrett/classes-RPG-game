"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
from hero import Hero
from goblin import Goblin
from character import Character

def main():
    hero = Hero()
    goblin = Goblin()

    while hero.alive() and goblin.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r. Enter 1, 2 or 3." % user_input)

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)


main()
