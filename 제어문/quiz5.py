from random import*

cnt = 0
for i in range(1,51):
    time = randrange(5, 51)
    if time > 15:
        check = ""
        print("[{0}] {1}번째 손님 (소요시간  : {2}분)".format(check, i, time))
    else:
        check = "O"
        cnt+=1
        print("[{0}] {1}번째 손님 (소요시간  : {2}분)".format(check, i, time))
print("\r")
print("총 탑승 승객 : {} 분".format(cnt))