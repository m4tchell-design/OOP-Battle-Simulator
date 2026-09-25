import random


from enemy import Enemy


class Goblin(Enemy):
    """A basic enemy found in the arena."""

    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15,)

    def attack(self):
        """Return a random amount of damage."""
        print(f"{self.name} attacks")
        return random.randint(1, self.attack_power)
        

    def take_damage(self, damage):
        """Reduce health without allowing it to fall below zero."""
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        """Return True while the enemy has health remaining."""
        return self.health > 0
