import socket


class MirrorServer:
    def __init__(self, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(port)
        self.socket.listen(5)

    def run(self):
        while True:
            request, client_address = self.socket.accept()
            input = request.makefile("rb", 0)
            output = request.makefile("wb", 0)
            l = True
            try:
                while l:
                    l = input.readline().strip()
                    if l:
                        output.write(l[::-1] + bytes('\r\n', 'utf-8'))
                    else:
                        request.shutdown(2)
            except socket.error:
                pass


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("usage : %s [hostname][port number]" % sys.argv[0])
        sys.exit(1)

    hostname = sys.argv[1]
    port = int(sys.argv[2])
    MirrorServer((hostname, port)).run()