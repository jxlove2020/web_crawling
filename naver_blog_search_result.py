import urllib.request
# 검색어 입력시 한글 검색이 잘 될 수 있도록 인코딩 해주는 모듈
import urllib.parse

from bs4 import BeautifulSoup

base_url = 'https://search.naver.com/search.naver?where=view&sm=tab_jum&query='
search_url = input('검색어를 입력해 주세요 : ')
# urllib.parse.quote_plus(검색어) : 인코딩 시켜줌
url = base_url + urllib.parse.quote_plus(search_url)

# print(url)

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

total_area = soup.find_all(class_='total_area')

# 네이버 VIEW 탭의 검색 결과 출력
for i in total_area: 
  a = i.find('a', {'class': 'api_txt_lines total_tit'})
  link = a.attrs['href']

  print()
  print(a.text)
  print(link)
