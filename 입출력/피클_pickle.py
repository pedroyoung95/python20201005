#pickle이란? 프로그램 상에서 사용하고 있는 데이터를 파일 형태로 저장해주는 것
import pickle
# profile_file = open("profile.pickle", "wb") #pickle를 사용하려면 꼭 binary로 명시해야 함. 인코딩은 필요 없음
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를 profile_file이라는 파일에 저장
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) #file에 있는 정보를 profile이라는 변수에 볼러오기
print(profile)
profile_file.close()