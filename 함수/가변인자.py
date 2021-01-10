# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end="") #end키워드에 빈 스트링을 담으면 줄바꿈 하지 않고 빈칸으로 문장을 끝마침
#     print(lang1, lang2, lang3, lang4, lang5) #이전 print문이 end로 인해 빈 칸으로 끝났으므로, 출력 시 줄 바꿈 없이 다음 출력문이 나옴

#파라미터의 개수가 정해지지 않은 경우, '*parameterName'형태로 *을 붙여서 작성하면 args를 개수 제한 없이 받을 수 있음
#여러 개의 args를 tuple로 받을 수 있게 함
def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end="") 
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")