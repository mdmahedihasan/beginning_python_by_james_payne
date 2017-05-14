import socket
import sys


if len(sys.argv) < 3:
    print("usage : %s [hostname][port number]" % sys.argv[0])
    sys.exit(1)

hostname = sys.argv[1]
port = int(sys.argv[2])

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sckt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sckt.bind((hostname, port))
sckt.listen(1)
print("waiting for the request")

request, clientAddress = sckt.accept()
print("received request from ", clientAddress)
request.send(bytes('-=SuperSimpleSocketServer 3000=-\n', 'utf-8'))
request.send(bytes("go away\n", "utf-8"))
request.shutdown(2)
print("stopping server")
sckt.close()