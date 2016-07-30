import os
import hashlib
import sqlite3

from flask import Flask, request, make_response
from HTTP.Request import Request
from HTTP.Response import Response
from DB.DataBase import DataBase

app = Flask(__name__)
app.debug = True

@app.route('/', methods= ['GET', 'POST'])
def application():
    return make_response("Hello!")

@app.route('/weixin', methods= ['GET', 'POST'])
def weixin_handler():
    open('a.txt', 'w')
    if request.method == 'GET':
        token = 'weixin'
        query = request.args
        signature = query.get('signature', '')
        timestamp = query.get('timestamp', '')
        nonce = query.get('nonce', '')
        echostr = query.get('echostr','')
        s = [timestamp, nonce, token]
        s.sort()
        s = ''.join(s)
        if hashlib.sha1(s).hexdigest() == signature :
            return make_response(echostr)
    else:
        _request = Request(request)
        paramDict = _request.parse('ToUserName', 'FromUserName', 'Content')
        response = Response()
        return response.makeResponse(**paramDict)

if __name__ == '__main__':
    app.run('0.0.0.0', port=int('80'))
    db = DataBase()
    db.init()


    
