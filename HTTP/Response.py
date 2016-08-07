from flask import make_response
from Service.ServiceFactory import ServiceFactory
import re

class Response(object):
	def __init__(self):
		super(Response, self).__init__()
		self.template = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"
		self.format = re.compile('^\d+.\s*\w+\s*$')
		self.defaultResponse = '0. Help\n1. Costs Service'

	def makeResponse(self, FromUserName, ToUserName, curTime, Content):
		info = self._confirm(Content)
		if info:
			service = ServiceFactory().getService(info[0])
			Content = service.parse(info[1])
		else:
			Content = self.defaultResponse 

		response = make_response(self.template % (FromUserName, ToUserName, curTime, Content))
		response.content_type = 'application/xml'
		return response

	def _confirm(self, content):
		print content
		if self.format.match(content):
			index = content.find('.')
			print index
			return [content[:index].strip(), content[index+1:].strip()]
		else:
			return None






