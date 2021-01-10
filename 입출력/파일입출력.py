#파일 열기 : open(param1, param2, param3) 메소드(파일을 사용하기 위해선 open으로 꼭 열어야 사용 가능)
#param1 : 파일명 / param2 : 파일로 하려는 활동 / param3 : 인코딩
#파일명은 필수 입력 파라미터, 나머지는 선택
#파일로 할 수 있는 활동 : "r"(read) / "w"(write) / "a"(append, 내용 추가) / "x"(create)
score_file = open("score.txt", "w", encoding="utf8") 
#파일이름, write, 인코딩 utf 8
print("수학 : 0", file=score_file) #write용도의 파일을 print()메소드의 파라미터로 파일을 지정하게 되면 그 파일에 write하게 됨
print("영어 : 50", file=score_file)
score_file.close() #사용한 파일은 close()메소드로 꼭 닫기

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# #print(score_file.read()) #read()메소드의 파라미터가 없으면 모든 내용 읽음
# print(score_file.readline()) #readline() : 한 줄 읽고 커서를 다음 줄로 이동. 맨 처음 커서는 맨 첫 줄 이전.
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
# #파일이 몇 줄인지 모를 때 -> while 무한 반복으로 읽고, 더이상 읽을 내용이 없을 때 break
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="") #print는 기본적으로 줄바꿈으로 인해 readline한 거 외에 추가로 한 줄 더 띄움. 
# end값으로 빈 스트링 할당(출력문의 끝을 결정)하면 줄바꿈이 한 번만 일어나게 함
# score_file.close()

# lines = score_file.readlines() #모든 라인을 가져와서 list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()

#바로 for 반복해도 한 줄씩 나옴
for line in score_file:
    print(line, end="")
score_file.close()