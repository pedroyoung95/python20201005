class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()
        # super()는 다중 상속 시 가장 맨 앞 부모클래스의 메소드와 필드(프로퍼티)만 상속 받게 됨
        # 다중 상속시에는 부모클래스로부터 직접 상속 받는 것이 좋음
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()