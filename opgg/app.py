from flask import Flask, render_template, request
## from : 사용자가 지정한 값을 어디론가 보내줌
# flask request를 통해 연결된 url, 요청받은 IP주소 등 많은 정보를 알아낼 수 있다.
import requests # 우리 대신 요청을 보내주는 역할
from bs4 import BeautifulSoup as BTS

# template_folder를 지정해주면 해당 폴더에서 return하는 파일(render_template을 통해)을 찾음
app = Flask(__name__, template_folder="views")

# 가장 기본적인 root route 항상 정의
@app.route("/")
def index():
    return render_template('index.html') # 동적으로 파일을 보냄
    # return "<h1>OP.GG</h1>" # html코드를 적용해줌
    
    
@app.route("/search")
def search():
    ## flask는 요청을 특정 객체(request)에 담아둔다.
    # print(request.full_path)
    # print(request.remote_addr)
    # print(request.url)
    # print(request.headers)
    userInput = request.args['userName']
    # ImmutableMultiDict([('userName', 'uid')])
    
    # 1. op.gg에 있는 데이터를 검색해서
    #   - op.gg에 요청을 보내서,
    #   - op.gg로 부터 html 파일 중,
    url = "http://www.op.gg/summoner/userName=" # + "사용자가 입력한 id"
    
    response = requests.get(url + userInput)
    
    # print(response.text)
    # 2. 승, 패 정보만 가져온다.
    doc = BTS(response.text)
    
    wins = doc.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins').text
    loses = doc.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')
    print(wins)
    return render_template('search.html', userInput=userInput, wins=wins[:-1], loses=loses.text[:-1])