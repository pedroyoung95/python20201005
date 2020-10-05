from random import *

print(random()) #0.0이상 1.0미만의 임의의 값 생성
print(random()*10)
print(int(random()*10)) #int 타입을 붙이면 정수로 만듦
print(int(random()*10)+1)

print("--------")

print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)

print("--------")

print(randrange(1, 46)) #1~46미만의 임의의 값 생성
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))

print(randint(1, 45)) #1~45이하의 임의의 값 생성