class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        # 부모 클래스명을 자식 클래스의 파라미터로 넣음
        # 부모 클래스의 변수를 사용하려면 parentClass.__init__(self,...)으로 부모클래스의 __init__메소드를 호출
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어벳", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)