# 다음에서 뉴스 한 페이지에서 뉴스 기사와 내용을 수집(15건의 기사)

import requests
from bs4 import BeautifulSoup

cnt = 0

for i in range(1, 4):
    url = 'https://news.daum.net/breakingnews/digital?page={}'.format(i)
    # print(url)

    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    url_list = soup.select('ul.list_allnews a.link_txt')
    #print(url_list)

    for j in url_list:
        cnt += 1
        url = j['href']
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        title = soup.select('h3.tit_view')
        contents = soup.select('div#harmonyContainer p')

        txt = ''
        for k in contents:
            txt += k.text
        print("==========================================================================================================")
        print(title[0].text)
        print(txt)

print('★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★')
print('{}건의 뉴스기사를 수집하였습니다.'.format(cnt))
print('★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★')