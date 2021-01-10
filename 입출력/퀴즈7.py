# for weak_no in range(1, 51):
#     with open("{}주차.txt".format(weak_no), "w", encoding="utf8") as weakly_file:
#         weakly_file.write("- {} 주차 주간보고 - \n부서 : \n이름 : \n업무 요약 : ".format(weak_no))

for weak_no in range(1, 6):
    with open("{}주차.txt".format(weak_no), "w", encoding="utf8") as weakly_file:
        weakly_file.write("- {} 주차 주간보고 - \n부서 : \n이름 : \n업무 요약 : ".format(weak_no))