# DemoDict.py 
a = (1,2,3)
b = list(a)
print(b)
b.append(4)
print(b)

#딕셔너리 연습
color = {"apple":"red", "banana":"yellow"}
print(type(color))
print(color["apple"])
#입력
color["cherry"] = "red"
#수정
color["apple"] = "blue"
#삭제
del color["cherry"]
#반복구문(~.items(), ~.values(), ~.keys() )
for item in color.items():
    print(item)

for k,v in color.items():
    print(k,v)

#모바일 장비관리
device = {"아이폰":5, "아이패드":10, "윈도우":20}
print(device["아이폰"])

device["맥북"] = 15 

device["아이폰"] = 6 

for item in device.items():
    print(item)