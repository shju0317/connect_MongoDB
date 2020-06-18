# 다음에서 뉴스 한 페이지에서 뉴스 기사와 내용을 수집(15건의 기사)

import requests
from bs4 import BeautifulSoup

url = 'https://news.daum.net/breakingnews/digital'

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

url_list = soup.select('ul.list_allnews a.link_txt')
print(url_list)

# print(len(url_list)) # 잘 긁어왔는지 개수로 확인

# href만 추출
#for i in url_list:
#    print(i['href'])

for i in url_list:
    url = i['href']
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    title = soup.select('h3.tit_view')
    contents = soup.select('div#harmonyContainer p')

    txt = ''
    for i in contents:
        txt += i.text
    print("==========================================================================================================")
    print(title[0].text)
    print(txt)