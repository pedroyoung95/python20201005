def profile(name, age, main_lang):
    print(name, age, main_lang)

#키워드를 통해 순서 상관 없이 args를 원하는 파라미터에 할당 가능
profile(name = "유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")

