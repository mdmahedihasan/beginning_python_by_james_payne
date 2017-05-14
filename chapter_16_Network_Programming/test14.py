import socket


class MirrorClient:
    def __init__(self, server, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(server, port)

    def mirror(self, s):
        if s[-1] != '\n':
            s += '\r\n'
        self.socket.send(bytes(s, 'utf-8'))

        buf = []
        input = ''
        while not '\n' in input:
            try:
                input = self.socket.recv(1024)
                buf.append(input)
            except socket.error:
                break
        return ''.join(buf)[:-1]

    def close(self):
        self.socket.send(bytes('\r\n', 'utf-8'))
        self.socket.close()


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 4:
        print("usage : %s [host][port][text to be mirrored]" % sys.argv[0])
        sys.exit(1)

    hostname = sys.argv[1]
    port = int(sys.argv[2])
    toMirror = sys.argv[3]

    m = MirrorClient(hostname, port)
    print(m.mirror(toMirror))
    m.close()