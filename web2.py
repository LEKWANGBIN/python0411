
# web2.py
#웹서버에 요청
import urllib.request
#크롤링
from bs4 import BeautifulSoup

#문자열변수(1800줄)
data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
#검색이 용이한 객체 
soup = BeautifulSoup(data, "html.parser")

# <td class="title">
# 	<a href="/webtoon/detail">마음의 소리 50화 <격렬한 나의 하루> </a>
# </td>
cartoons = soup.find_all("td", class_="title")
#리턴형이 리스트
print("개수:{0}".format(len(cartoons)))
#0번방 슬라이싱
print(cartoons[0].find("a").text)
print(cartoons[0].find("a")["href"])

for item in cartoons:
    tag = item.find("a")
    print(tag.text.strip())

#파일 생성
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
#수열함수로 페이지 번호 생성
for i in range(1,6):
    url = \
    "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" \
    + str(i)
    print(url)
    data = urllib.request.urlopen(url)
    #검색이 용이한 객체 
    soup = BeautifulSoup(data, "html.parser")
    cartoons = soup.find_all("td", class_="title")
    for item in cartoons:
        tag = item.find("a")
        print(tag.text.strip())
        f.write(tag.text.strip() + "\n")
f.close()