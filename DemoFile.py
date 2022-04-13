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