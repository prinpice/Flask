# kospi 정보를 스크랩한다.

import requests
import bs4

url = "http://finance.naver.com/sise/"

#requests.get(url) #해당 url에 있는 정보를 받아온다

response = requests.get(url).text

doc = bs4.BeautifulSoup(response, 'html.parser') #BeautifulSoup에서 파이썬으로 검색하기 좋은 폼으로 예쁘게 만듬, html파싱한 것으로...

result = doc.select_one('#KOSPI_now') # # : unify id값

print(result.text)