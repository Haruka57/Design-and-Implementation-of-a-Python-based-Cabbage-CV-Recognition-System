from flask import Flask, request, jsonify, redirect, url_for
from flask_cors import CORS
from User import reg, login, change_password

app = Flask(__name__)
# 允许跨域
CORS(app)

@app.route('/reg', methods=['POST'])
def reg1():
    # 获取传过来的json数据
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    print(username, password)
    flag = reg(username, password)
    # 返回注册的结果
    return jsonify({'k': flag})
@app.route('/login', methods=['POST'])
def login1():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    flag = login(username, password)
    return jsonify({'success': flag})

@app.route('/change_password', methods=['POST'])
def change_password1():
    data = request.get_json()
    username = data.get('username')
    new_password = data.get('password')
    flag = change_password(username, new_password)
    return jsonify({'change': flag})


if __name__ == '__main__':
    app.run(debug=True, port=5000)