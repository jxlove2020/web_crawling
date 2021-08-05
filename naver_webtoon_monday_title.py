# pip3 로 bs4 (BeautifulSoup) 와 request 설치
# pprint 는 print 보다 보기 쉽게 출력해 줍니다. 
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://comic.naver.com/webtoon/weekday')
soup = bs(html.text, 'html.parser')
html.close()

# 월요 웹툰 영역 추출하기
data1 = soup.find('div', {'class':'col_inner'})
# pprint(data1)

# 제목 포함영역 추출하기
data2 = data1.findAll('a', {'class':'title'})
# pprint(data2)

# 텍스트만 추출

# title_list = []
# for t in data2:
#   title_list.append(t.text)

# for 문에서 더 간략하게 list로 추출
title_list = [t.text for t in data2]
print(title_list)


