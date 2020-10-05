url = "http://daum.com"
my_str = url.replace("http://","")
my_password = my_str[:my_str.index(".")]
firstpart = my_password[:3]
secondpart = len(my_password)
thirthpart = my_password.count("e")
print(firstpart + str(secondpart) + str(thirthpart) + "!")

