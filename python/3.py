
import  socket

PORT = 4000
HOST = ''

s = socket.socket(AF_INET, socket.SOCK_STREAM)
print 'socket created'

try:
	s.bind((HOST, PORT))
except socket.error ,msg:
	print 'Bind failed. Error code:'+ str(msg[0]) + 'Error message:' + msg[1]
	sys.exit()

print 'Socket bind complete'
s.listen(1)
print 'Socket now listening'
while 1:
	conn, addr = s.accept()
	print 'Connected with' + addr[0] + ':' + str(addr[1])
	data = conn.recv(1024)
	reply = 'ok...' + data
	if not data: break
	conn.send(data)
conn.close()
s.close()

