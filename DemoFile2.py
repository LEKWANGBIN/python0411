# DemoFile2.py 

#파일을 쓰기(파이썬은 태생이 리눅스, 유닉스) 
f = open("c:/work/demo.txt", "wt")
f = open("c:\\work\\demo.txt", "wt")
#약간불편(오래된 언어)
f.write("한글데이터\nabcd\n1234\n")
f.close()

#파일을 읽기(raw notation기법)
#파일을 읽기(raw string notation기법): 로우 푸드(황성수 비건)
#탈출문자: \n, \t
f = open(r"c:\work\demo.txt", "rt")
result = f.read()
#파일을 처음부터 끝까지 하나의 문자열변수 읽기 
# result = f.read()
# print(result)
# f.close() 
#파일을 한줄씩 읽기(파일의 규모가 크면 한줄씩 읽어서 처리)
#로그파일(서버의 작업을 텍스트로 기록): 1GB
# print(f.readline(), end="")
# print(f.readline(), end="")
# f.close() 
#파일전체를 읽어서 리스트로 반환
result = f.readlines()
print(result)
f.close()  