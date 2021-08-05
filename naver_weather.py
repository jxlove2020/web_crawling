# pip3 로 bs4 (BeautifulSoup) 와 request 설치
# pprint 는 print 보다 보기 쉽게 출력해 줍니다. 
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=경기도 용인시 수지구 죽전동 날씨')
# pprint(html.text)

soup = bs(html.text, 'html.parser')

# urlopen을 진행한 후에는 close를 한다
html.close()

# pprint(soup)


title = soup.find('div', {'class':'select_box'}) #영역추출
main_info = soup.find('div', {'class':'main_info'}) #영역추출
data1 = soup.find('div', {'class':'detail_box'}) #영역추출
# pprint(main_info)

data2 = data1.findAll('dd')
# pprint(data2)

find_title = title.find('em').text
find_dust = data2[0].find('span', {'class':'num'}).text
print(find_title)
# strip() 함수는 왼쪽 lstrip(), 오른쪽 rstrip() 공백을 제거 해 줍니다. 
print(main_info.text.strip())
print("미세먼지 : ", find_dust)
