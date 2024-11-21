import sys
from socketserver import TCPServer, BaseRequestHandler, UDPServer

class myTCPHandler(BaseRequestHandler):
	def handle(self):
		print("Connection from ", str(self.client_address))
		while True:
			data = self.request.recv(1024)
			if data.decode() == "bye\r\n": break
			self.request.send(data.upper())
		self.request.close()



class myUDPHandler(BaseRequestHandler):
	def handle(self):
		print ("Connection from ", str(self.client_address))
		data, conn = self.request
		conn.sendto(data.upper(),self.client_address)

def selectProtocol(pro,ip,port):
	if pro.lower() == 'udp':
		myServer = UDPServer((ip, int(port)), myUDPHandler)
	elif pro.lower() == 'tcp':
		myServer = TCPServer((ip, int(3456)), myTCPHandler)
	else: 
		print("WRONG USAGE")
		print("OPTIONS: - tpc - udp ")
	myServer.serve_forever()


if len(sys.argv) == 4:
	pro = str(sys.argv[1])
	ip = sys.argv[2]
	port = sys.argv[3]
	
	selectProtocol(pro,ip,port)
else:
	print("USAGE: myechoserver <Protocol> <IP> <PORT>")
