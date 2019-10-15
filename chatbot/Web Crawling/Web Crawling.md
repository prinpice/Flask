# Web Crawling

## 기본구조

* 특정 검색어의 원하는 정보를 내 컴퓨터에 저장
* `request` package 사용(설치필요)
  * `requests.get(url)`
  * `requests.get(url).text` : 스크랩한 내용 출력(코드형태)
  * `requests.get(url).status_code` : status code 출력

## BeautifulSoup

* 파이썬이 읽기 쉽도록 만들어주는 패키지

* 설치 후 사용

  ```git
  $ pip install beautifulsoup4
  ```

* `bs4.BeautifulSoup([html 문서])`

* `bs4.BeautifulSoup([html 문서]).select(경로)` : 특정 내용 추출(배열 가능)

* `bs4.BeautifulSoup([html 문서]).select_one(경로)` : 특정 내용 중 첫번째 내용 추출

* 경로

  * 원하는 내용에서 우클릭 => 검사
  * 웹 페이지의 검사에서 해당 html 코드 우클릭 => copy selector

  예시) Daum kospi data

  ```python
  # kospi 정보를 스크랩한다.
  
  import requests
  import bs4
  
  url = "http://finance.daum.net"
  #requests.get(url) #해당 url에 있는 정보를 받아온다
  
  response = requests.get(url).text
  
  doc = bs4.BeautifulSoup(response, 'html.parser') #BeautifulSoup에서 파이썬으로 검색하기 좋은 폼으로 예쁘게 만듬, html파싱한 것으로...
  
  result = doc.select_one('#boxIndexTabs > span > h4')
  
  print(result.text)
  ```

  