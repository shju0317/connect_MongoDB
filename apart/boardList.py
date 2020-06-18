import requests
from bs4 import BeautifulSoup

cnt = 0
list_url = 'http://news.sarangbang.com/bbs.html?tab=free&p=2'
resp = requests.get(list_url)

if resp.status_code != 200:
    print('WARNING: 잘못된 URL 접근!')

soup = BeautifulSoup(resp.text, 'html.parser')
board_list = soup.select('tbody#bbsResult > tr > td > a')
# print(board_list)

for i, href in enumerate(board_list):
    # print(i, href)
    if i % 2 == 0:
        cnt += 1
        url = 'http://home.sarangbang.com' + href['href']
        resp = requests.get(url)

        if resp.status_code != 200:
            print('WARNING: 잘못된 URL 접근!')

        soup = BeautifulSoup(resp.text, 'html.parser')

        title = soup.select('h3.tit_view')[0].text.strip()
        writer = soup.select('a.name_more')[0].text.strip()
        reg_dt = soup.select('span.tit_cat')[1].text.strip()[:10] # dt = date # 구조가 항상 동일할 때만 [i] 지정 가능. # [:10]을 통해 년월일만 출력
        contents = soup.select('div.bbs_view p')

        txt = ''
        for j in contents:
            txt += j.text.strip()

        print('Title ▶', title)
        print('Writer ▶', writer)
        print('Date ▶', reg_dt)
        print('Contents ▶\n', txt)

print('사랑방 부동산에서 {}건의 게시글을 수집하였습니다.'.format(cnt))