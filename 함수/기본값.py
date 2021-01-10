def profile(name, age, main_lang):
    print("이름 : {}\t나이 : {}\t주 사용 언어: {}" \
        .format(name, age, main_lang)) #코드를 여러 줄로 분할 할 시, 역슬래쉬로 이어줘야 함

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

def profile2(name, age=17, main_lang="파이썬"):
    print("이름 : {}\t나이 : {}\t주 사용 언어: {}" \
        .format(name, age, main_lang))
profile2("박명수") #args를 따로 받지 않으면 기본args가 적용됨
#기본args가 설정되어 있지 않으면 반드시 args를 전부 설정해줘야 함

    

