# DemoFile3.py

#파일쓰기 
f = open("c:\\Data.txt", "wt", encoding="utf-8")
#파일쓰기(유니코드로 작업) 
f = open("c:\\work\\Data.txt", "wt", encoding="utf-8")
f.write("첫줄\n두번째줄\n세번째줄\n")
f.close()

f = open("c:\\Data.txt", "a+", encoding="utf-8")
#기존 파일에 추가
f = open("c:\\work\\Data.txt", "a+", encoding="utf-8")
f.write("새로운 데이터추가\n")
f.close() 

#파일을 닫았는지?
print(f.closed)
