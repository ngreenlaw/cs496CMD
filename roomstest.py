f=open("rooms.json", "r")
s = f.read()
import json
rooms = json.loads(s)
for room in rooms.keys():
    print (rooms[room]['name'])
