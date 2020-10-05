python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
#isupper() -> 대문자인지 확인
#variableName[index number].method() 
#몇번째 글자에 대해서만 method 적용
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
#동일 글자가 여러 개 있을 경우, 맨 앞 글자의 번호를 가져옴
index = python.index("n", index + 1)
#index("a", index + n)
#a의 index번호+n번째부터 그 뒤에 있는 a의 index번호 찾기
print(index)

print(python.find("Java"))
# print(python.index("Java"))
#find() : 찾는 글자가 없으면 -1출력하고 계속 실행
#index() : 찾는 글자가 없으면 오류, 실행 종료
print("hi")

print(python.count("n"))
#.count("a") : a가 총 몇 번 나오는지
