import json
rooms = {}
rooms["Entry"] = {
    "name": "Entry",
    "id": 1,
    "descL": "The large entry way into the tomb, there are hieroglyphs on each of the walls. There is a large doorway in front of you that looks like it leads to a larger space.",
    "descMod": "",
    "descAdd": "",
    "descS": "You are in the entry of the tomb. There is a doorway in front of you.",
    "items": "",
    "features": ["On the left side of the room the hieroglyphs says, 'Intruders beware crushing death and grief, soaked with blood of the trespassing thief'","On the right side of the room the hieroglyphs says 'The key to my return lies within the heart of the underworld'"],
    "visited": False,
    "north_room": "Main Passage",
    "south_room": "",
    "east_room": "",
    "west_room": ""
}	
rooms["Main Passage"] =	{
    "name": "Main Passage", 
      
} 

s = json.dumps(rooms)

with open("rm.txt","w+") as f:
	f.write(s)
