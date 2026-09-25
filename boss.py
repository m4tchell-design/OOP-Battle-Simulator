from enemy import Enemy


class Boss(Enemy):
    """A stronger enemy with a powered-up attack."""

    def __init__(self, name):
        super().__init__(name, health=300, attack_power=45)

    def attack(self):
        damage = super().attack()
        bonus_damage = 15
        print(f"{self.name} unleashes a crushing blow!")
        return damage + bonus_damage

    def take_damage(self, damage):
        damage = damage * 1.5
        super().take_damage(damage)
        print(f"{self.name} suffured {damage} damage. Health: {self.health}")
        