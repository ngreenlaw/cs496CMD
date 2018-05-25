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
room11 = {}
room12 = {}
room13 = {}
room14 = {}
room15 = {}

room1 = {
	"name": "Entry",
	"descL": "The large entry way into the tomb, there are hieroglyphs on each of the walls. There is a large doorway in front of you that looks like it leads to a larger space.",
	"descMod": "",
	"descS": "You are in the entry of the tomb. There is a doorway in front of you.",
	"features": ["left, hieroglyphs", "right hieroglyphs"],
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
	"descL":"As you enter the antechamber you notice that the door behind you starts to close, it must have been something you stepped on. Along the wall the hieroglyphs seem to keep saying the same thing. 'Believe in me as all are descendants from me.'",
	"descMod": "",
	"descS":"",
	"features": ["falcon carving", "lettered floor"],
	"items": [],
	"visited": "False",
	"north_room": "",
	"south_room": "Antechamber 2",
	"east_room": "",
	"west_room": "Treasure Room",
	"locked": "False"
}
room5 = {
	"name": "Treasure Room", 
	"descL": "As you enter the room you notice that this should be the treasury room. A room that was once full of gold to make sure the sorcerer could pay his way into the afterlife. However, this room must have been raided millenia ago, all that remains are that of bones around three large statues. I might want to be careful I don't meet the same fate as the rest of these men.",
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
	"locked": "False"
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
room11 = {
	"name": "Guard's Room", 
	"descL": "You enter a large room. Along the stone wall at the north side of the room are 3 tapestries, the one on the left has an image of the god Set pointing a sword to the right, the one in the middle has an image of the god Osiris sitting on a throne and the one on the right has an image of the goddess Isis kneeling. Along the west wall there are 3 small empty tombs with their lids already open and along the south wall is a weapons rack that has a few spears and swords. The room has a stench of death and laying by one of the tombs is a recently deceased adventurer with his pack still on his back.",
	"descMod": "",
	"descS": "You are in what appears to be a Guard's Room. There are 3 tapestries along the north wall, one of Set, one of Osiris, and one of Isis. Along the south wall is a weapons rack with a sword and a spear and along the west wall is a dead adventurer.",
	"features": ["Secret Stairs", "Decomposed Bodies", "Weapons Rack", "Adventurer Pack", "tapestry of set", "tapestry of ra", "tapestry of isis"],
	"items": ["sword", "spear"],
	"visited": "False",
	"north_room": "Nile River",
	"south_room": "",
	"east_room": "Mirror Room",
	"west_room": "",
	"locked": "False"
}
room12 = {
	"name": "Nile River", 
	"descL": "You descend down the stairs to find a small room with what looks like a river flowing through the middle of it from west to east. To the north across the small river is a closed door. On the east and west walls on the opposite side of the river as you are two statues of creatures that look like mermaids. As you approach the river you start to hear the sound of beautiful singing which distracts you from what you are doing.",
	"descMod": "",
	"descS": "You are in a small room with a river flowing through the middle from west to east. On the north side of the river is a door and on opposite sides of the river are mermaid statues. You can hear beautiful singing.",
	"features": ["River", "Siren Song","Locked Door","wooden door","siren statue"],
	"items": [],
	"visited": "False",
	"north_room": "Chamber of Passing",
	"south_room": "Guard's Room",
	"east_room": "",
	"west_room": "",
	"locked": "False"
}
room13 = {
	"name": "Chamber of Passing", 
	"descL": "You walk into the room and it is completely pitch black. You cannot see anything.",
	"descMod": "",
	"descS": "You are in a completely pitch black room. You cannot see anything.",
	"features": ["Stairs", "writings", "jackal statue","chimera statue"],
	"items": ["necklace", "brooch"],
	"visited": "False",
	"north_room": "",
	"south_room": "Nile River",
	"east_room": "",
	"west_room": "Sphinx's Room",
	"locked": "False"
}
room14 = {
	"name": "Sphinx's Room", 
	"descL": "You descend down the stairs and when you enter the room a voice booms out startling you and says: There are two sisters: one gives birth to the other and she, in turn, gives birth to the first. What are they? Greeting you is a sphinx statue directly in front of you on the east wall. The sphinx is massive and takes up the majority of the room and scattered around it are tons of jeweled scarabs.",
	"descMod": "",
	"descS": "As you enter the room, you see a sphinx statue on the east wall. The sphinx is massive and takes up the majority of the room and scattered around it are tons of jeweled scarabs.",
	"features": ["Sphinx", "Scarab Brooches", "jeweled beetles"],
	"items": [],
	"visited": "False",
	"north_room": "",
	"south_room": "",
	"east_room": "Chamber of Passing",
	"west_room": "Burial Chamber",
	"locked": "False"
}
room15 = {
	"name": "Burial Chamber", 
	"descL": "You carefully walk down the stairs and enter a large room. On the east wall in front of you is a giant unopened tomb in between two large Griffin statues. Although the room is massive it is otherwise empty. There are no other doors you see and thus appears to be a dead-end.",
	"descMod": "",
	"descS": "In the large room there is a giant unopened tomb in between two large Griffin statues. There are no other exits, this appears to be the end.",
	"features": ["Griffins", "large tomb", "griffin statue", "eagle statue"],
	"items": ["ancient artifact"],
	"visited": "False",
	"north_room": "",
	"south_room": "",
	"east_room": "Sphinx's Room",
	"west_room": "",
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
c = json.dumps(room11)
d = json.dumps(room12)
e = json.dumps(room13)
f = json.dumps(room14)
g = json.dumps(room15)

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
with open("room11.json","w+") as f:
	f.write(c)
with open("room12.json","w+") as f:
	f.write(d)
with open("room13.json","w+") as f:
	f.write(e)
with open("room14.json","w+") as f:
	f.write(f)
with open("room15.json","w+") as f:
	f.write(g)	
