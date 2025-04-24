import requests

class API:
	def __init__(self, target):
		self.target = target
		self.headers = {}
		self.body = {}
	
	def set_headers(self, headers):
		self.headers = headers
	
	def set_body(self, body):
		self.body = body
	
	def add_header(self, key, content):
		self.headers[key] = content
	
	def add_body_element(self, key, content):
		self.body[key] = content
	
	def debug_html_request(self):
		print('<REQ_HEADER>')
		for e in self.headers.items():
			print('%s: %s' % (e[0], e[1]))
		print('<REQ_BODY>')
		for e in self.body.items():
			print('%s: %s' % (e[0], e[1]))
		
	def post(self, payload_type='json'):
		response = {'code': -1}
		if payload_type == 'json':
			res = requests.post(self.target, headers=self.headers, json=self.body)
			response['code'] = res.status_code
			response['text'] = res.text
		return response
