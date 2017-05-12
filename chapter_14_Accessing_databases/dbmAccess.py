import dbm

db = dbm.open('websites', 'w')

db['www.wrox.com'] = 'Wrox home page'

if db['www.python.org'] != None:
    print('Found www.python.org')
else:
    print('Error : missing item')

for key in db.keys():
    print("Key = ", key, " value = ", db[key])

del db['www.wrox.com']
print('After deleting www.wrox.com, we have : ')

for key in db.keys():
    print("Key = ", key, " value = ", db[key])

db.close()
