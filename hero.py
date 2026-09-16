import random 

class Hero:
    """The hero blueprint will be implemented later in the project."""
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.attack_power = 45
        self.armor = 5

    def attack(self):
        passedCritCheck = random.randint(1, 6) == 6
        if passedCritCheck:
            attack = random.randint(1,self.attack_power) * 1.25
            print("Attack was critical")
        x = random.randint(0, self.attack_power)
        if x == 0:
            print("Attack Missed")
        return x


    def take_damage(self, damage):
        damage =  max(0, damage - self.armor)
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} take {damage} damage. Health: {self.health}")

    def is_alive(self):
        return self.health > 0