from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/session', methods=['POST']) # post로 읽어올 때는 꼭 method를 작성해야 한다. # 여러개가 올 수도 있기 때문에 배열로 작성
def session():
    # request.args는 POST방식에서 읽어올 수 없다.
    email = request.form.get('email')
    password = request.form.get('password')
    
    # 유저 1명 뿐 : asdf@asdf.com & 12341234
    # 만약 email == asdf@asdf.com, password == 12341234
    # 로그인이 되었습니다. (msg = "로그인이 되었습니다.")
    # 아닐경우,
    #   로그인이 되지 않았습니다.
    if email == 'asdf@asdf.com' and password == '12341234':
        # msg = "로그인이 되었습니다."
        return redirect("/") # session창에 갔다가 돌아옴
    else:
        msg = "로그인이 되지 않았습니다."
        return render_template('session.html', msg=msg)




# 자동으로 서버를 껏다켜서 수정된 것을 자동반영
if __name__ == "__main__":
    app.run(debug=True)
    # => git bash 창에
    # python app.py
    # 를 입력하여 자동 reloading하게 해준다.
    # 그러나 html이 수정되었을 때만 반영이된다.