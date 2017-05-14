import quopri

encoded = quopri.encodestring(bytes("this is a test", "utf-8"))
print(encoded)

decoded = quopri.decodestring(encoded)
print(decoded)