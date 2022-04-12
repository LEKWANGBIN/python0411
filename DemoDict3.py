# DemoDict3.py
#얕은복사
a = [1,2,3]
b = a 
a[0] = 38
print(a)
print(b)
print(id(a),id(b))

#깊은복사
a = [100,200,300]
b = a[:]
a[0] = 101
print(a)
print(b)
print(id(a),id(b))

print(1<2)
print(1 !=2)
print(1==2)
print(True and True and True)
print(True and True and False)
print(True or False or False)
print(5/2)
print(5//2)
print(5%2)
print(4%2)