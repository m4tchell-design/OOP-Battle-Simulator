import random
from goblin import Goblin
from boss import Boss
from hero import Hero

ARENA_NAME = "The Iron Lung"

def battle(hero, enemy):
    while hero.is_alive() and enemy.is_alive():
        if hero.is_alive():
            hero_damage = hero.attack()
            enemy.take_damage(hero_damage)
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)
    if hero.is_alive():
        print(f"{hero.name} won the battle")
    else:
        print(f"{enemy.name} won the battle")


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    boss = Boss("Gorlock")
    print(f"{boss.name} enters the arena with {boss.health} health.")

    goblin = Goblin("Dobby")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    goblinTwo = Goblin("Gobby")
    print(f"{goblinTwo.name} enters the arena with {goblinTwo.health} health.")

    print("But no hero has answered the call... yet.")

    hero = Hero("Carv")
    print(f"{hero.name} has entered the arena with {hero.health} health")

    battle(hero, boss)

if __name__ == "__main__":
    main()
