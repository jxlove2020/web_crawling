# pip3 로 bs4 (BeautifulSoup) 와 request 설치
# pprint 는 print 보다 보기 쉽게 출력해 줍니다. 
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=경기도 용인시 수지구 죽전동 날씨')
# pprint(html.text)

soup = bs(html.text, 'html.parser')
# pprint(soup)


title = soup.find('div', {'class':'select_box'}) #영역추출
data1 = soup.find('div', {'class':'detail_box'}) #영역추출
# pprint(title.text)

data2 = data1.findAll('dd')
# pprint(data2)

find_title = title.find('em').text
find_dust = data2[0].find('span', {'class':'num'}).text
print(find_title)
print("미세먼지 : ", find_dust)