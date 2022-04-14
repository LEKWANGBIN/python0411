#DemoStr.py
print(dir(str))

strA = "python is very powerful"
print(len(strA))
print(strA.capitalize)
print(strA.endswith("ful"))
print(strA.count("p"))
print(strA.count("p",7))

print("mbc2580".isalnum())
print("mbc:2580".isalnum())
print("2580".isnumeric())

names= ["전우치","홍길동","이순신"]
for name in names:
    print("안녕하세요 {0}님 더운 여름입니다.".format(name))
    print("="*40)

u = "<<<  spam and ham  >>>"
result= u.strip("<> ")
print(u)
print(result)
result2 = result.replace("spam","spam egg")
print(result2)
lst = result2.split()
print(lst)
print("---하나로 합치기---")
print(":)".join(lst))