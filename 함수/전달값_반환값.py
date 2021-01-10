def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account()

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {} 원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {} 원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {} 원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    if balance >= money + commission:
        print("출금이 완료되었습니다. 수수료는 {} 원이며, 잔액은 {} 원 입니다.".format(commission, balance - money -commission))
        return commission, balance - money - commission #리턴값이 여러 개면 tuple로 나옴
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {} 원 입니다.".format(balance))
        return balance

balance = 0
balance = deposit(balance, 1000)
print(balance)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
#commission, balance = withdraw_night(balance, 500) #리턴값 두 개가 첫 번째 변수 부터 차례로 할당됨
#print("수수료 {} 원이며, 잔액은 {} 원입니다.".format(commission, balance))
commission, balance = withdraw_night(balance, 500)
withdraw_night(balance, 400)