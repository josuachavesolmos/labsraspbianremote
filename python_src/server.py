import http.server
BaseHTTPServer = CGIHTTPServer = SimpleHTTPServer = http.server

class projectServer(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		if self.path.endswith('/prueba'):
			self.send_response(200)
			self.send_header('content-type','text/html')
			self.end_headers()
			output=''
			output+='<html><body>'
			output+='<h1>Prueba</h1>'
			output+='</body></html>'
			self.wfile.write(output.encode())
		else:
			super().do_GET()		

def test(HandlerClass = projectServer,
         ServerClass = BaseHTTPServer.HTTPServer):
    BaseHTTPServer.test(HandlerClass, ServerClass)


if __name__ == '__main__':
    test()