from flask import make_response
from DB.DataBase import DataBase

class Response(object):
	def __init__(self):
		super(Response, self).__init__()
		self.template = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"
		self.db = DataBase('wx.db')

	def makeResponse(self, FromUserName, ToUserName, curTime, Content):
		Content = self.test(FromUserName, Content)	
		response = make_response(self.template % (FromUserName, ToUserName, curTime, Content))
		response.content_type = 'application/xml'
		return response

	def test(self, Content, UserName):
		result = self.db.execute('select money from costs where uid = "%s"' % UserName)
		if not result:
			self.db.execute('insert into costs values("%s", 300)' % UserName)
		else:
			return result[0]





