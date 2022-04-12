# function3.py
#기본값을 명시
def times(a=10,b=20):
    return a*b 

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드 인자방식으로 전달
def connectURI(server, port):
    strURL = "http://" + server + ":" + port 
    return strURL

#호출
print(connectURI("credu.com", "80"))
print(connectURI(port="80", server="credu.com"))

#가변인자(갯수가 정해지지 않은 가변적인 경우)
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result 

#호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))
#정의되지않은 인자 처리(필수, 옵션:dict)
def userURLBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL 

#호출
print(userURLBuilder("credu.com", "80", id="kim", passwd="1234"))
print(userURLBuilder("credu.com", "80", id="kim", passwd="1234", 
    name="mike"))

#람다함수(이름이 없다)
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print((lambda x:x*x)(3))
print(globals())