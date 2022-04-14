#크롤링하는 라이브러리 선언 
from bs4 import BeautifulSoup

#웹페이지를 로딩
#웹페이지를 로딩(메서드 체인)
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색객체 생성
soup = BeautifulSoup(page, "html.parser")
print(soup.prettify())
#print(soup.prettify())

#문서 내부의 <p>태그 몽땅
print(soup.find_all("p"))
0 comments on commit 341b36e