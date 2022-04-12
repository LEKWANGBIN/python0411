# function2.py 
#전역변수
x = 1 
def func(a):
    return x+a 

#호출
print(func(1))

def func2(a):
    x = 2 
    return x+a 

#호출
print(func2(1))

#불변형식
a = 1.2
print(id(a))
a = 2.3
print(id(a))
print("---가변형식---")
lst=[1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))

#불변형식인데 함수 내부에서 읽기 + 쓰기
g=1
def testScope(a):
    global g
    g = 2
    return g+a

#호출
print(testScope(1))
print("전역변수 g: ", g)
