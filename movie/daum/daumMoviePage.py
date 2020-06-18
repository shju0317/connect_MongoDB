# 댓글 긁어오기
# 리플을 통째로 긁어와서 필요한 요소들 하나씩 꺼내기

import requests
from bs4 import BeautifulSoup
import movie.persistence.MongoDAO as DAO

# 객체생성
mDAO = DAO.MongoDAO()

cnt = 0
page = 1

#for page in range(1, 5):
while True:
    url = 'https://movie.daum.net/moviedb/grade?movieId=126335&type=netizen&page={}'.format(page)
    resp = requests.get(url)

    if resp.status_code != 200:
        print('WARNING: 잘못된 URL 접근!')

    soup = BeautifulSoup(resp.text, 'html.parser')
    reply_list = soup.select('div.review_info')
    # print(len(reply_list))

    if len(reply_list) == 0:
        print('마지막 페이지입니당')
        break

    print('********************************** {} page *************************************'.format(page))

    for reply in reply_list:
        cnt += 1
        writer = reply.select('em.link_profile')[0].text.strip()
        print('▶ 작성자: ', writer) # 작성자
        content = reply.select('p.desc_review')[0].text.strip()
        print(content) # 내용
        reg_date = reply.select('span.info_append')[0].text.strip() # slicing할 경우는 무조건 길이가 고정일 때
        print(reg_date) # 날짜
        index_val = print(reg_date.index(','))
        print('▶ 작성일자: ', reg_date[:index_val])
        score = reply.select('em.emph_grade')[0].text.strip()
        print(score) # 평점
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')

        # MongoDB에 저장하기 위해 Dict Type으로 변환
        data = {'content':content,
                'writer':writer,
                'score':score,
                'reg_date':reg_date}

        # 내용, 작성자, 평점, 작성일자 MongoDB에 Save
        mDAO.mongo_write(data)

    page += 1

print('수집한 영화댓글은 총 {}건입니다.'.format(cnt))

