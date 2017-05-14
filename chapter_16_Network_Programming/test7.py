import random
import quopri
import base64

length = 10000
randomBinary = ''.join([chr(random.randint(0, 128)) for x in range(0, length)])

print(len(quopri.encodestring(bytes(randomBinary, "utf-8"))) / float(length))
print(len(base64.encodestring(bytes(randomBinary, "utf-8"))) / float(length))