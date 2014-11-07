
from socket import *
import os

fd = socket(AF_INET, SOCK_STREAM)
fd.bind(('127.0.0.1',4000))
fd.listen(2)

while True:
	new_fd, addr = fd.accept()
#	print 'got connection from' ,addr
	if os.fork() == 0:
		data = new_fd.recvfrom(1024)
		print 'data'	
		print data
		g = data[0]
		print '###########'
		token = g.split(' ')
		print token
		p =  token[1][1:]
	
		if p == '':
			p = 'index.html'
		print p
	
		file_fd = open(p)
		data = file_fd.read()
		fsize = os.path.getsize(p)
		print '###### size'
		print fsize
		
		extlist = p.split('.')
		if extlist[1] == 'png':
			extn = 'image/png'
		elif extlist[1] == 'html':
			extn = 'text/html'
		elif extlist[1] == 'jpg':
			extn = 'image/jpg'
		elif extlist[1]  == 'png':
			extn = 'image/png'			

		head = 'HTTP/1.1 200 OK\nContent-Length: %s\nContent-Type: %s\r\n\n'%(str(fsize),extn)
		new_fd.sendto(head+data,addr)
		new_fd.close

fd.close()
