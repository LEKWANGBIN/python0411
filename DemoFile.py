# DemoFile.py
#문자열을 결합 연산
url = "http://www.credu.com/?page=" + str(1) 
print(url)
#정렬방식 지정
for x in range(1,6):
    print(x,"*",x,"=",x*x)


print("---약간 수정---")

for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3))

print("---약간 수정---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).zfill(5))

#서식문자 지정
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(15000000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
