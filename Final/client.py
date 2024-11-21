#CLient
import socket

def clientTCP(server_tcp,mess):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        sock.connect(server_tcp)
        sock.sendall(mess.encode())
        response = sock.recv(1024)
        print(f'Recv: {response.decode()}')

def clientUDP(server_udp,mess):
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as sock:
        sock.sendto(mess.encode(),server_udp)
        response, _ = sock.recvfrom(1024)
        print(f"Recv: {response.decode()}")
 
server_tcp = ("10.20.30.2",3456)
server_udp = ("10.20.30.2",7890)
mess = "hola tcp"



