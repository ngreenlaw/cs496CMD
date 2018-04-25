f=open("rm.txt", "r")
s = f.read()
import json
rooms = json.loads(s)
print rooms
print
print rooms['Entry']['features'][0]
print 
print rooms['Entry']['north_room']
