class Unit:
    # self는 객체 자신을 지칭하는 키워드, 자기 자신의 요소(ex>필드)에 접근하기 위해 사용
    # self가 붙은 파라미터는 그 이름의 객체의 변수가 되게 만듦(self가 안 붙은 건 파라미터)
    #Python에서는 self키워드를 붙여서 필드로 선언해서 값을 할당하는 것
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

#__init__() : 파이선에서의 클래스 생성자
#self를 제외한 동일한 개수의 인수를 보내줘야 함

#멤버 변수 : 클래스가 가지는 변수('self.변수명'의 형태의 것들) -> 자바의 클래스의 '필드'와 유사
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {}, 공격력 : {}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True #Python에서는 클래스의 객체에다가 새로운 속성을 외부에서 부여할 수 있음
#cloking 변수가 없었는데 외부에서 인위적으로 객체의 변수를 만들고, True라는 값을 할당함

if wraith2.clocking == True: 
    print("{}는 현재 클로킹 상태입니다.".format(wraith2.name))
