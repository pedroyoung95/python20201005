print("a", "b")

#방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은  %c로 시작해요." % "A")
# %s는 다른 타입도 다 받을 수 있음
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

#방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))


#방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))
#format() method에서 변수 선언 후, {}안 변수 명을 기입

#방법 4(v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
#문장 앞 f는 format method를 적용함을 의미