import sys
print("Python", "Java", "JavaScript", sep=" vs ") #sep(=seperate) : comma로 '구분된' 출력물 사이에 넣을 것을 지정
print("Python", "Java", "JavaScript", sep=",", end="?") #end : 출력물의 마지막 끝나는 부분을 지정(줄바꿈 안 일어남)
print("무엇이 더 재밌을까요?")
print("Python", "Java", file=sys.stdout) #stdout(=standard-out) : 표준출력
print("Python", "Java", file=sys.stderr) #stderr(=standard-error) : 표준에러로 출력, 에러 처리 가능

scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subject, score in scores.items(): #items() : dictionary의 키와 값을 쌍으로 리턴(tuple형태로 리턴)
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    #ljsut(int), rjust(int) : 파라미터 값의 칸 만큼 공간을 확보하며 각각 왼쪽/오른쪽 정렬

for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) #zfill(int) : 파라미터 값 만큼의 자리수로 만들고, 빈 자리수는 0(zero)로 채움

answer = input("아무 값이나 입력하세요 : ") #input(string) : 파라미터 값이 출력되면서 옆에 콘솔에 입력가능한 커서 활성화 
print(type(answer)) #input으로 입력된 값은 항상 문자열로 저장
print("입력하신 값은 " + answer + "입니다.") 