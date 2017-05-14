import base64

encoded = base64.encodestring(bytes("this is a test", "utf-8"))
print(encoded)

decoded = base64.decodestring(encoded)
print(decoded)