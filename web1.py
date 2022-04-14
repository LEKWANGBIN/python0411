# web1.py 
#크롤링하는 라이브러리 선언 
from bs4 import BeautifulSoup
#웹페이지를 로딩(메서드 체인)
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색객체 생성
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())

#문서 내부의 <p>태그 몽땅
print(soup.find_all("p"))
#print(soup.find_all("p"))

#첫번째 <p>
#print(soup.find("p"))

#필터링: <p class="outer-text">컨텐츠</p>
#파이썬에서 class키워드가 있어서 인자명(class_)
#print(soup.find_all("p", class_="outer-text"))

#최종적으로 문자열을 받기
for item in soup.find_all("p"):
    #text속성은 컨텐츠만 리턴
    title = item.text.strip()
    title = title.replace("\n", "")
    title = title.replace("\t", "")
    print(title)