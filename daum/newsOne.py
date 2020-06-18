# 다음에서 뉴스 한건의 기사와 내용을 수집

import requests
from bs4 import BeautifulSoup

# url은 내가 수집하고 싶은 데이터가 위치한 웹사이트 주소를 가리킴
url = 'https://news.v.daum.net/v/20200615220011696'

# url주소를 이용해서 해당 웹페이지의 모든 소스코드를 불러와서 resp에 저장
resp = requests.get(url)

# resp에 status_code가 200이면 성공, 나머지는 실패
if resp.status_code == 200:
    print('Success')
else:
    print('Wrong URL')

# requests는 소스코드만 전부 가져오는거고 거기서 원하는 내용은 추출 불가
# 원하는 내용만 추출하려면 BeautifulSoup을 사용해야 함.
# beautifulsoup에 input으로 resp의 값(웹사이트의 소스코드 전체)을 전달
# soup에 웹사이트의 소스코드 전체가 저장
# soup.select()를 이용하여 원하는 정보만 추출
soup = BeautifulSoup(resp.text, 'html.parser') # html.parser를 이용해서 읽으세요

# find 잘 쓰지 않음. 불편.
# soup.find('tag명', '선택자')

title = soup.select('h3.tit_view') # (tag+선택자). <-tag생략가능하지만 같이 쓰는 것이 좋음. 결과를 list로 받아옴.
print(title)
print(title[0].text)

print('==========================================================================')
# 본문 긁어오기
contents = soup.select('div.news_view') # id일 경우 -> ex) div#mArticle
#print(contents)
print(contents[0].text.strip())
# strip()은 앞뒤 공백 제거. 중간중간 있는 공백은 제거해주지 않음.

# soup.select()는 무조건 return을 list type으로 반환
# [val1, val2, ...]
# ex) contents[i]

print('==========================================================================')
# 공백없이 깔끔하게 하려면 더 깊게 들어가면 됨.
con1 = soup.select('div.news_view p')
print(con1)

con2 = soup.select('div#harmonyContainer p')
print(con2)

print('==========================================================================')
# 리스트에서 내용만 꺼내오기
txt = ''
for i in con2:
    txt += i.text
print(txt)

