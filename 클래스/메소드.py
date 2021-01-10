class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}]".format(self.name, location, self.damage))