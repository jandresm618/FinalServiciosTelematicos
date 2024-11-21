from Handler import myHandler

ip_addr = '10.20.30.2'
tcp_port = 3456
udp_port = 7890

handler = myHandler(ip_addr=ip_addr,tcp_port=tcp_port,udp_port=udp_port)

handler.thread_init()