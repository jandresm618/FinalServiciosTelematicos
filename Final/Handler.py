from socketserver import ForkingTCPServer, ForkingUDPServer, BaseRequestHandler
from threading import Thread

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
		print("...")
		print("Connection from: ",str(self.client_address))
		data, conn = self.request
		conn.sendto(data.upper(),self.client_address)

class myHandler():
    def __init__(self,ip_addr="127.0.0.1",tcp_port=3456,udp_port=7890):
        self.ip=ip_addr
        self.tcp_port=tcp_port
        self.udp_port=udp_port
        self.myTCPServer = ForkingTCPServer((ip_addr, tcp_port), myTCPHandler)
        self.myUDPServer = ForkingUDPServer((ip_addr, udp_port), myUDPHandler)

    def thread_init(self):
        tcp_thread = Thread(target=self.myTCPServer.serve_forever)
        udp_thread = Thread(target=self.myUDPServer.serve_forever)

        # Iniciar los hilos.
        tcp_thread.start()
        print(type(tcp_thread))
        print ("TCP started on port %s" % self.tcp_port)
        udp_thread.start()
        print(type(udp_thread))
        print ("UDP started on port %s" % self.udp_port)


