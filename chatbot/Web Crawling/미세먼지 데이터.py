import requests
import os
from bs4 import BeautifulSoup

key = os.getenv('AIR_KEY')
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey={}&sidoName=서울&pageNo=3'.format(key)
response = requests.get(url).text
soup = BeautifulSoup(response, 'xml')
gn = soup('item')[7]
location = gn.stationName.text
time = gn.dataTime.text
dust = int(gn.pm10Value.text)

print('{0} 기준: 서울시 {1}의 미세먼지 농도는 {2} 입니다.'.format(time, location, dust))

# 미세먼지 농도가 좋은지, 나쁜지, 매우 나쁜지, 보통인지 출력하세요
gb = ""
if(dust < 30):
  gb = "좋음"
elif(dust < 80):
  gb = "보통"
elif(dust < 150):
  gb = "나쁨"
else:
  gb = "매우나쁨"
  
print(gb)