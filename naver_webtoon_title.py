# pip3 로 bs4 (BeautifulSoup) 와 request 설치
# pprint 는 print 보다 보기 쉽게 출력해 줍니다. 
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://comic.naver.com/webtoon/weekday')
soup = bs(html.text, 'html.parser')
html.close()

# 웹툰 영역 추출하기
data1_list = soup.findAll('div', {'class':'col_inner'})
# pprint(len(data1_list))

# 전체 웹툰 리스트
week_title_list = []

# 제목 포함영역 추출하기
for data1 in data1_list:
  # 제목 포함 영역 추출
  data2 = data1.findAll('a', {'class': 'title'})
  # pprint(data2)

  # 텍스트만 추출
  title_list = [t.text for t in data2]

  week_title_list.append(title_list)

# 전체 웹툰 리스트
print(week_title_list)

# 요일별 웹툰 리스트
print(week_title_list[0]) # 월요일
print(week_title_list[1]) # 화요일
print(week_title_list[2]) # 수요일