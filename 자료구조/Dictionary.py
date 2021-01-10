cabinet = {
    3 : "유재석",
    100 : "김태호"
    }
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
# print(cabinet[5]) 없는 index 키를 사용하면 에러 발생 및 프로그램 종료
print(cabinet.get(5)) #get()메소드로 없는 키의 값을 구하려고 하면 None 출력, 프로그램은 계속 가동
print(cabinet.get(5, "사용가능")) #두 번째 파라미터로, 값이 없을 경우의 출력되는 기본값 입력
print("hi")

print(3 in cabinet)
print(5 in cabinet)

cabinet = {
    "a-3" : "유재석",
    "b-100" : "김태호"
}
print(cabinet["a-3"])
cabinet["c-20"] = "조세호"
cabinet["a-3"] = "김종국"
print(cabinet)
del cabinet["a-3"]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
print(cabinet)