# DemoFile2.py 

#파일을 쓰기(파이썬은 태생이 리눅스, 유닉스) 
f = open("c:/work/demo.txt", "wt")
#약간불편(오래된 언어)
f.write("한글데이터\nabcd\n1234\n")
f.close()

#파일을 읽기(raw notation기법)
f = open(r"c:\work\demo.txt", "rt")
result = f.read()
print(result)
f.close()  