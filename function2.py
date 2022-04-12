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
