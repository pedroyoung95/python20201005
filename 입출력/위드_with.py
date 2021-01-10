# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))
# #open으로 특정 파일을 열고, as 뒤에 있는 변수에 담은 상태에서 특정 활동을 수행
# #with을 통해서 파일을 열면 자동으로 파일을 close함(java의 autoclose와 유사)

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있다")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())