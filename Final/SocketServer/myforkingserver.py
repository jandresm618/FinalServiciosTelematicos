from socketserver import ForkingTCPServer, BaseRequestHandler
import sys


class myHandler(BaseRequestHandler):
	def handle(self):
		print ("Connection from ", str(self.client_address))
		while True:
			data = self.request.recv(1024)
			if data.decode() == "bye\r\n": break
			self.request.send(data.upper())
		self.request.close()

myServer = ForkingTCPServer(("127.0.0.1", 3456), myHandler)
myServer.serve_forever()
