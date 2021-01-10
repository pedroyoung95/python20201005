menu = {"커피", "우유", "주스"}
print(menu)
print(menu, type(menu)) #type() : 파라미터의 타입을 리턴

#형변환
menu = list(menu)
print(menu, type(menu))
menu = tuple(menu)
print(menu, type(menu))
menu = set(menu)
print(menu, type(menu))