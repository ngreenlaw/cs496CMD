import json
room1 = {}
room2 = {}
room3 = {}
room4 = {}
room5 = {}
room6 = {}
room7 = {}
room8 = {}
room9 = {}
room10 = {}

room1 = {
	"name": "Entry",
	"descL": "The large entry way into the tomb, there are hieroglyphs on each of the walls. There is a large doorway in front of you that looks like it leads to a larger space.",
	"descMod": "",
	"descS": "You are in the entry of the tomb. There is a doorway in front of you.",
	"features": ["left hieroglyphs", "right hieroglyphs"],
	"items": [],
	"visited": "False",
	"north_room": "Main Passage",
	"south_room": "",
	"east_room": "",
	"west_room": "",
	"locked": "False"
}	
room2 =	{
    	"name": "Main Passage", 
	"descL": "As you move into the main passageway you notice that the air is a little thinner in here, might be a good idea to find an exit before the air in the tomb runs out. On the wall in front of you there is what looks like a large cylinder with different markings on it.",
	"descMod": "",
	"descS": "On the wall in front of you there is what looks like a large cylinder with different markings on it.",
	"features": ["cylinder","stone door", "door 1", "door 2"],
	"items": [],
	"visited": "False",
	"north_room": "",
	"south_room": "Entry",
	"east_room": "Pharaoh Mummy Room",
	"west_room": "Antechamber 1",
	"locked": "False"
	
} 
room3 = {
	"name": "Antechamber 1", 
	"descL": "Upon entering the chamber you notice a door right in front of you covered in four switches, there is nothing in the chamber except that the walls are covered in hieroglyphs. While walking by one of them you notice that a small hole in the wall seemed to light up as you passed by.",
	"descMod": "",
	"descS": "Upon entering the chamber you notice a door right in front of you, there is nothing in the chamber except that the walls are covered in hieroglyphs.",
	"features": ["odd hole", "switch"],
	"items": [],
	"visited": "False",
	"north_room": "Antechamber 2",
	"south_room": "",
	"east_room": "Main Passage",
	"west_room": "",
	"locked": "True"
}
room4 = {
	"name": "Antechamber 2", 
	"descL":"As you enter the antechamber you notice the hieroglyphs on the wall seem to keep saying the same thing. 'The key is in the heart of the underworld.'",
	"descMod": "",
	"descS":"",
	"features": ["falcon carving", "lettered floor"],
	"items": [],
	"visited": "False",
	"north_room": "",
	"south_room": "Antechamber 1",
	"east_room": "",
	"west_room": "Treasure Room",
	"locked": "False"
}
room5 = {
	"name": "Treasure Room", 
	"descL": "As you enter the room you notice that this should be the treasury room. A room that was once full of gold to make sure the sorcerer could pay his way into the afterlife. However, this room must have been raided millenia ago, all that remains are that of bones around three large statues of horus, osiris, and anubis. I might want to be careful I don't meet the same fate as the rest of these men.",
	"descMod": "",
	"descS": "A room that was once full of gold to make sure the sorcerer could pay his way into the afterlife. However, this room must have been raided millenia ago, all that remains are that of bones around three large statues.",
	"features": ["statue of osiris", "statue of horus", "statue of anubis"],
	"items": [],
	"visited": "False",
	"north_room": "",
	"south_room": "",
	"east_room": "Antechamber 2",
	"west_room": "",
	"locked": "False"
}
room6 = {
	"name": "Pharaoh Mummy Room", 
	"descL": "Upon entering the room, you notice several sarcophagi that are ornately decorated with jewels and carvings of deities and animals in the stone.  However, time and nature has worn away at the decorations, but you can see that they were once beautiful.  In the corner, strange knocking and scraping noises are coming from one of the sarcophagi.",
	"descMod": "",
	"descS": "",
	"features": ["Noisy Sarcophagus", "Urn"],
	"items": [],
	"visited": "False",
	"north_room": "Mirror Room",
	"south_room": "",
	"east_room": "",
	"west_room": "Main Passage",
	"locked": "True"
}	
room7 = {
	"name": "Mirror Room", 
	"descL": "Upon entering the room, you notice several polished copper mirrors along the walls.  There are bats and insects flying and crawling around and the mirrors amplify their numbers.  It is also hard to tell where everything is because of them. ",
	"descMod": "",
	"descS": "",
	"features": ["Sculpture of Cat", "Spider"],
	"items": [],
	"visited": "False",
	"north_room": "",
	"south_room": "Pharaoh Mummy Room",
	"east_room": "Skeleton Room",
	"west_room": "Guard's Room",
	"locked": "False"
}
room8 = {
	"name": "Skeleton Room", 
	"descL": "Upon entering the room, you see bones and skulls scattered everywhere.  It is hard to tell how old they are or why they are there.  Perhaps they are previous explorers? It surprises you that there might be so many.",
	"descMod": "",
	"descS": "",
	"features": ["Book", "Elephant Tusk"],
	"items": [],
	"visited": "False",
	"north_room": "Food Room",
	"south_room": "",
	"east_room": "",
	"west_room": "Mirror Room",
	"locked": "False"
}
room9 = {
	"name": "Food Room", 
	"descL": "Upon entering the room, you find multiple sources of food.  There are sacks of grain and fruits.  The smell, however,  is putrid and you quickly realize that there is also mummified meat in this room.",
	"descMod": "",
	"descS": "",
	"features": ["Spider", "Scarab Sculpture"],
	"items": [],
	"visited": "False",
	"north_room": "",
	"south_room": "Skeleton Room",
	"east_room": "Mummified Animals Room",
	"west_room": "",
	"locked": "False"
}
room10 = {
	"name": "Mummified Animals Room", 
	"descL": "Upon entering the room, you find that the air is putrid here too and realize that the room is filled with mummified pets.  There are birds, cats, crocodiles, baboons, vultures, and many others.  It's hard to tell, but one of the mummies seems to be shaking very slightly.  There are hieroglyphs on the walls too.",
	"descMod": "",
	"descS": "",
	"features": ["Shaky Mummy", "Hieroglyphs"],
	"items": [],
	"visited": "False",
	"north_room": "",
	"south_room": "",
	"east_room": "",
	"west_room": "Food Room",
	"locked": "False"
}

s = json.dumps(room1)
t = json.dumps(room2)
u = json.dumps(room3)
v = json.dumps(room4)
w = json.dumps(room5)
x = json.dumps(room6)
y = json.dumps(room7)
z = json.dumps(room8)
a = json.dumps(room9)
b = json.dumps(room10)

with open("room1.json","w+") as f:
	f.write(s)
with open("room2.json","w+") as f:
	f.write(t)
with open("room3.json","w+") as f:
	f.write(u)
with open("room4.json","w+") as f:
	f.write(v)
with open("room5.json","w+") as f:
	f.write(w)
with open("room6.json","w+") as f:
	f.write(x)
with open("room7.json","w+") as f:
	f.write(y)
with open("room8.json","w+") as f:
	f.write(z)
with open("room9.json","w+") as f:
	f.write(a)
with open("room10.json","w+") as f:
	f.write(b)
