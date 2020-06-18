import requests
from bs4 import BeautifulSoup

page = 1
cnt = 0
compare_writer = ''
break_point = False # 이중반복문을 빠져나가기 위한 조건

while True:
    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=191436&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'.format(page)

    resp = requests.get(url)

    if resp.status_code != 200:
        print('존재하지 않는 URL')

    soup = BeautifulSoup(resp.text, 'html.parser')

    reply_list = soup.select('div.score_result li')

    for i, reply in enumerate(reply_list):
        # content = reply.select('span#_filtered_ment_'+str(i))[0].text.strip() # 좋은방법아님
        content = reply.select('div.score_reple > p > span ')[0].text.strip()  # 좋은방법

        # 네이버에 영화댓글의 작성자는 닉네임(아이디) 구조
        # ex) 뽀로로(prr*****) -> 닉네임만 추출(그러나 닉네임이 없는 경우도 있음)
        # 닉네임이 없는 경우 ()안의 아이디를 사용하는 코드 작성
        previous_writer = reply.select('div.score_reple a > span')[0].text.strip()
        cut_index = previous_writer.find('(')

        if cut_index > 0:
            writer = previous_writer[:cut_index]
        else:
            writer = previous_writer

        score = reply.select('div.star_score > em')[0].text.strip()

        reg_date = reply.select('div.score_reple em')[1].text.strip()[:10]  # slicing할 경우는 무조건 길이가 고정일 때

        # 네이버 영화 댓글 수집 페이지의 마지막 페이지를 계산하는 코드
        # 네이버는 1명의 작성자가 1개의 댓글만 작성할 수 있음
        # 매페이지의 첫번째 게시글의 작성자를 compare_writer에 저장하고
        # 매페이지의 첫번째 게시글 작성자와 compare_writer를 비교해서 같으면 중복페이지 -> 수집종료
        if i == 0:
            if compare_writer == writer:
                print('Finished Collect:>')
                break_point = True
                break
            else:
                compare_writer = writer # 0번 작성자 바뀜

        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print('▶ 내용: ', content)       # 내용
        print('▶ 작성자: ', writer)      # 작성자
        print('▶ 평점: ', score)         # 평점
        print('▶ 작성일자: ', reg_date)  # 날짜

        cnt += 1
    # 이중 반복문 break
    if break_point:
        break

    page += 1
print('수집한 영화댓글은 총 {}건입니다.'.format(cnt))