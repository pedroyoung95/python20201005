# 중복X, 순서X
my_set = {1,2,3,3,3}
print(my_set) # 중복되는 부분은 무시되고 나머지만 set에 들어감

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

 #교집합(두 set 모두에 들어가있는 요소 리턴)
print(java & python)
print(java.intersection(python))

#합집합(두 set를 합침)
print(java | python)
print(java.union(python))

#차집합(한 집합에서 다른 집합을 뺌)
print(java - python)
print(java.difference(python))

#값 추가
python.add("김태호")
print(python)

#값 제거
java.remove("김태호")
print(java)

