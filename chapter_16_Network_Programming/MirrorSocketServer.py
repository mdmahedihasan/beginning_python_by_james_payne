import socketserver


class RequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        l = True
        while l:
            l = self.rfile.readline().strip()
            if l:
                self.wfile.write(l[::-1] + bytes('\n', 'utf-8'))


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("usage : %s [hostname][port number]" % sys.argv[0])
        sys.exit(1)

    hostname = sys.argv[1]
    port = int(sys.argv[2])

    socketserver.TCPServer((hostname, port), RequestHandler).serve_forever()