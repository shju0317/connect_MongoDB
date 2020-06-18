# 제목
# 내용
# 작성일자
# 작성자

import requests
from bs4 import BeautifulSoup

url = 'http://news.sarangbang.com/talk/bbs/free/163946?url=%2F%2Fnews.sarangbang.com%2Fbbs.html%3Ftab%3Dfree'
resp = requests.get(url)

if resp.status_code != 200:
    print('WARNING: 잘못된 URL 접근!')

soup = BeautifulSoup(resp.text, 'html.parser')

title = soup.select('h3.tit_view')[0].text.strip()
writer = soup.select('a.name_more')[0].text.strip()
reg_dt = soup.select('span.tit_cat')[1].text.strip()[:10] # dt = date # 구조가 항상 동일할 때만 [i] 지정 가능. # [:10]을 통해 년월일만 출력
contents = soup.select('div.bbs_view p')

txt = ''
for i in contents:
    txt += i.text.strip()

print('Title ▶', title)
print('Writer ▶', writer)
print('Date ▶', reg_dt)
print('Contents ▶\n', txt)
