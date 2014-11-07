
from socket import *
import select
fd = socket(AF_INET,SOCK_DGRAM)
fd.bind(('127.0.0.1',4000))

while True:
	n = select.select([0,fd], [], [],)
	if n[0][0] == 0 :
		str = raw_input()
		fd.sendto(str,('127.0.0.1',3000))
	elif n[0][0] == fd:
		print fd.recvfrom(100)

