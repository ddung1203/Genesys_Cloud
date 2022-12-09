from flask import Flask, request, render_template
import call_list
import call_list_update
import call_list_management
import call_list_delete
import os


app = Flask(__name__)

@app.route('/')
def hello():
  return '''<!DOCTYPE HTML><html>
  <head>
    <title>Flask app</title>
  </head>
  <body>
    <h1><a href="/">GS Neotek</a></h1>
    <a href="./call_list_update">리스트 갱신</a>
    <br>
    <a href="./campaign">캠페인 시작</a>
    <br>
    <a href="./all">리스트 갱신 및 캠페인 시작</a>
    <br>
    <a href="./crontab">주기 생성</a>
    <br>
    <a href="./delete">리스트 삭제</a>
  </body>
</html>'''

@app.route('/call_list_update')
def update():
  return call_list_update.run()

@app.route('/crontab')
def crontab():
  return '''<!DOCTYPE HTML><html>
  <head>
    <title>Flask app</title>
  </head>
  <body>
    <h1><a href="/">GS Neotek</a></h1>
    <h2>현재 주기는 평일 15시입니다. 계속하시겠습니까?</h2>
    <a href="./crontab/complete">계속하기</a>
    <a href="./crontab/delete">삭제하기</a>
  </body>
</html>'''

@app.route('/crontab/complete')
def complete():
  os.system('(crontab -l 2>/dev/null; echo "0 15 * * 1-5 /home/vagrant/call_list_update.py") | crontab -')
  return '''<!DOCTYPE HTML><html>
  <head>
    <title>Flask app</title>
  </head>
  <body>
    <h1><a href="/">GS Neotek</a></h1>
    <h2>Complete!!</h2>
  </body>
</html>'''

@app.route('/crontab/delete')
def delete():
  os.system('crontab -r')
  return '''<!DOCTYPE HTML><html>
  <head>
    <title>Flask app</title>
  </head>
  <body>
    <h1><a href="/">GS Neotek</a></h1>
    <h2>Complete!!</h2>
  </body>
</html>'''

@app.route('/campaign')
def campaign():
  
  return call_list_management.run()

@app.route('/all')
def all():
  
  return call_list.run()

@app.route('/delete')
def user_del():
  
  return render_template('delete.html')


@app.route('/delete/complete', methods=['GET'])
def user_del_comp():
  tmp = request.args.get('delete')
  
  return call_list_delete.run(tmp)


if __name__ == '__main__':
  app.run()