from flask import Flask, render_template, request
import os
import sys
import requests
app = Flask(__name__)

naver_id = os.getenv('NAVER_ID')
naver_secret = os.getenv('NAVER_PWD')
my_url = "https://cli-piie.c9users.io"
url = "https://openapi.naver.com/v1/papago/n2mt"



headers = {
    'X-Naver-Client-Id': naver_id,
    'X-Naver-Client-Secret': naver_secret
}





@app.route("/") # 주문받을(요청받을) 서비스
def index(): # 해당하는 주문/요청에 대한 결과
    return render_template('index.html')
    
@app.route("/show") # index에 날려준 단어를 받아
def show():         # 그대로 출력한다.
    words=request.args.get('words')
    
    data = {
        'source' : 'en',
        'target' : 'ko',
        'text' : words
            }
    
    res = requests.post(url, headers=headers, data=data) # post로 요청을 보낼때는 post로 입력
    
    res_dict = res.json()
    
    end_res = res_dict.get('message').get('result').get('translatedText')
    
    return render_template('show.html', words=end_res)