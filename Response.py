from flask import make_response

class Response(object):
	def __init__(self):
		super(Response, self).__init__()
		self.template = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"

	def makeResponse(self, FromUserName, ToUserName, curTime, Content):
		response = make_response(self.template % (FromUserName, ToUserName, curTime, Content))
		response.content_type = 'application/xml'
		return response
