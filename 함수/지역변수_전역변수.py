gun = 10 #지역 변수 상태로, 함수 내 gun이라는 변수와 다른 변수임

def checkpoint(soldiers):
    global gun #global키워드를 통해 전역 변수가 되어서, 함수 밖 변수를 함수 안에서 사용 가능하게 함
    gun = gun - soldiers #원래는 함수 내의 지역변수 gun이나 함수 밖 gun이 전역변수가 되어서 이 변수는 함수 밖 gun변수와 동일함
    print("[함수 내] 남은 총 : {}".format(gun))

#전역 변수를 많이 사용하게 되면 프로그램 관리가 어려워짐
#실제로는 함수 내에서 계산된 결과값을 리턴해서 기존 변수에 다시 담는 방식으로 처리함
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {}".format(gun))
    return gun 

print("전체 총 : {}".format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun, 2) #함수에서 계산된 결과값을 기존 변수에 다시 넣어서 변경된 결과값이 반영되게 함
print("남은 총 : {}".format(gun))