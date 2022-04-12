# function1.py 
#함수를 정의
def setValue(i):
    #함수 내부의 지역변수에 초기화
    x = i 
    print("내부에서 출력:", x)

#함수를 호출
retValue = setValue(5)
print(retValue)

#함수를 정의
def swap(x,y):
    return y,x 

#호출
print(swap(2,3))

#디버깅 연습함수 정의
def intersect(prelist,postlist):
    #함수 내부의 지역 함수를 초기화(list)
    retList = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        #특정 글자가 postlist에 있고 특정 글자가 아직 없다(retList)
        if x in postlist and x not in retList:
            retList.append(x)
    return retList

#함수를 호출
print(intersect("HAM","SPAM"))
