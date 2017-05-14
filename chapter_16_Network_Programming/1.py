import socket
import sys


if len(sys.argv) < 3:
    print("usage : %s [hostname][portnumber]" % sys.argv[0])
    sys.exit(1)

hostname = sys.argv[1]
port = int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((hostname, port))
sock.listen(1)
print("waiting for a request...")

request, clientAddress = sock.accept()
print("received request from ", clientAddress)
request.send(bytes('-=SuperSimpleSocketServer 3000=-\n', 'utf-8'))
request.send(bytes("go away \n", "utf-8"))
request.shutdown(2)
print("stopping server....")
sock.close()