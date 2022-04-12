#DemoLoop.py
value = 5
while value > 0:
    print(value)
    value -= 1
print("전체 코드 실행 종료")

#반복구문을 원하는 만큼
for i in range(5):
    print(i)

lst = ["apple", 100, 3.14]
for item in lst:
    print(item, type(item))

d={"apple":100, "kiwi":200}
for k,v in d.items():
    print(k,v)

#구구단 출력
for i in [2,3,4,5,6]:
    print("--{0}단---".format(i))
    for j in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(i,j,i*j)) 

lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break 
    print("Item:{0}".format(i))
print("---continue---")
for i in lst:
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))

#수열함수
result = list(range(10))
print(result) 
years = list(range(2000,2023))
print(years)

#리스트컴프리헨션
lst = list(range(1,11))
result = [i**2 for i in lst if i > 5]
print(result)

tp = ("apple", "banana", "kiwi")
print([len(i) for i in tp])

#필터링
lst = [10,25,30]
iterL = filter(None, lst)
for item in iterL:
    print(item)

print("---필터링을 하면---")
#함수 정의
def getBiggerThan20(i):
    return i>20

#호출
iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

