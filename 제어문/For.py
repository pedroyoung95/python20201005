for waiting_no in range(1, 6):
    print("대기번호 : {}".format(waiting_no))
starbucks = ["아이언맨", "토르", "캡틴"]
for customer in starbucks:
    print("{}님, 커피가 준비되었습니다.".format(customer) )

#한 줄 for
students = [1,2,3,4,5]
students = [i+100 for i in students]
print(students)

students = ["Iron man", "Thor", "Captine"]
students = [len(i) for i in students]
print(students)

students = ["Iron man", "Thor", "Captine"]
students = [i.upper() for i in students]
print(students)