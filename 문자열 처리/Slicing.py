jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) #0~2직전까지의 글자 가져옴
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[0:6])
print("뒤 7자리 : " + jumin[7:]) #끝까지 slice 함
print("뒤 7자리 (뒤에부터) : " + jumin[-7:])
#뒤부터 셀 때는 index 번호가 -1부터 시작
#똑같이 :(콜론) 뒤 숫자 직전까지만 포함