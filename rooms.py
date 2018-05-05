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

room1["Entry"] = {
	"name": "Entry",
	"descL": "The large entry way into the tomb, there are hieroglyphs on each of the walls. There is a large doorway in front of you that looks like it leads to a larger space.",
	"descMod": "",
	"descS": "You are in the entry of the tomb. There is a doorway in front of you.",
	"items": "",
	"features": [
	{
		"name": "Left hieroglyphs", 
		"desc": "On the left side of the room the hieroglyphs says, 'Intruders beware crushing death and grief, soaked with blood of the trespassing thief'",
		"descMod": "",
		"usage": ""
	},
	{
		"name": "Right hieroglyphs", 
		"desc": "On the right side of the room the hieroglyphs says, 'The key to my return lies within the heart of the underworld'",
		"descMod": "",
		"usage": ""
	},
	{
		"name": "Exit",
		"descFalse": "There is a large stone wheel blocking the exit.",
		"descTrue": "The large stone wheel seems to be moved out of the way.",
		"blocking": False,
		"descMod": "",
		"usage": ""
	}],
	#"features": "hi", "there",
	#features['1'] = {"hieroglyphs sefsef"} features['2'] = {"soaked with"}, 
	 
	#"features": "On the left side of the room the hieroglyphs says 'Intruders beware crushing death and grief, soaked with blood of the trespassing thief'", "On the right side of the room the hieroglyphs says 'The key to my return lies within the heart of the underworld'",
	"visited": False,
	"north_room": "Main Passage",
	"south_room": "",
	"east_room": "",
	"west_room": "",
	"locked": False
}	
room2["Main Passage"] =	{
    "name": "Main Passage", 
	"descL": "As you move into the main passageway you notice that the air is a little thinner in here, might be a good idea to find an exit before the air in the tomb runs out. On the wall in front of you there is what looks like a large cylinder with different markings on it.",
	"descMod": "",
	"descS": "On the wall in front of you there is what looks like a large cylinder with different markings on it.",
	"items": "",
	"features": [
	{
		"name": "Puzzle", 
		"desc": "Upon further investigation of the wall you notice that it's a sequence of pictures that proceed a recessed cylinder in the wall. The sequence is 3 Bulls, 1 Eagle, 4 Lions, 1 Sun.",
		"descCyl": "The cylinder - consists of 0 to 9 Ox", 
		"descMod": "",
		"usage": ""
	}, 
	{
		"name": "Stone door", 
		"desc": "A small stone door that is set in the middle of the wall.",
		"descOpen": "The small stone door seems to be open now.",
		"descMod": "",
		"usage": ""
	},
	{
		"name": "Door 1",
		"descTrue": "The giant stone door to your left is closed." ,
		"descFalse":  "The giant stone door to your left is open.",
		"closed": False,
		"descMod": "",
		"usage": ""
	},
	{
		"name": "Door 2",
		"descTrue": "The giant stone door to your right is closed.",
		"descFalse": "The giant stone door to your right is open.",
		"closed": False,
		"descMod": "",
		"usage": ""
	}],
	"visited": False,
	"north_room": "",
	"south_room": "Entry",
	"east_room": "Pharaoh Mummy Room",
	"west_room": "Antechamber 1",
	"locked": False
	
} 
room3["Antechamber 1"] = {
"name": "Antechamber 1", 
	"descL": "Upon entering the chamber you notice a door right in front of you covered in four switches, there is nothing in the chamber except that the walls are covered in hieroglyphs. While walking by one of them you notice that a small hole in the wall seemed to light up as you passed by.",
	"descMod": "",
	"descS": "Upon entering the chamber you notice a door right in front of you, there is nothing in the chamber except that the walls are covered in hieroglyphs.",
	"items": "",
	"features": [
	{
		"name": "Odd hole", 
		"desc": "As you look at the wall more closely, you notice the odd placement of the holes on the wall",
		"descMod": "",
		"usage": ""
	},
	{
		"name": "Door switches", 
		"desc": "The door has 4 switches located on it, all set in the up position.",
		"descMod": "",
		"usage": ""
	}],
	"visited": False,
	"north_room": "Antechamber 2",
	"south_room": "",
	"east_room": "Main Passage",
	"west_room": "",
	"locked": False
}
room4["Antechamber 2"] = {
	"name": "Antechamber 2", 
	"descL":"As you enter the antechamber you notice that the door behind you starts to close, it must have been something you stepped on. Along the wall the hieroglyphs seem to keep saying the same thing. 'Believe in me as all are descendants from me.'",
	"descMod": "",
	"descS":"",
	"items": "",
	"features": [
	{
		"name": "Falcon carving", 
		"desc": "An ornate wall with the carving of a falcon on it.",
		"descMod": "",
		"usage": ""
	},
	{
		"name": "Lettered floor", 
		"desc": "A floor layed out in a grid like pattern with different letters on it. ",
		"descMod": "",
		"usage": ""
	}],
	"visited": False,
	"north_room": "",
	"south_room": "Antechamber 2",
	"east_room": "",
	"west_room": "Treasure Room",
	"locked": False
}
room5["Treasure Room"] = {
	"name": "Treasure Room", 
	"descL": "As you enter the room you notice that this should be the treasury room. A room that was once full of gold to make sure the sorcerer could pay his way into the afterlife. However, this room must have been raided millenia ago, all that remains are that of bones around three large statues. I might want to be careful I don't meet the same fate as the rest of these men.",
	"descMod": "",
	"descS": "A room that was once full of gold to make sure the sorcerer could pay his way into the afterlife. However, this room must have been raided millenia ago, all that remains are that of bones around three large statues.",
	"items": "",
	"features": [
	{
		"name": "Statue of Osiris", 
		"desc": "Looks like small pressure plates on the head, chest and stomach of the statue.",
		"descMod": "",
		"usage": ""
	},
	{
		"name": "Statue of Horus", 
		"desc": "Looks like small pressure plates on the head, chest and stomach of the statue.",
		"descMod": "",
		"usage": ""
	},
	{
		"name": "Statue of Anubis", 
		"desc": "Looks like small pressure plates on the head, chest and stomach of the statue.",
		"descMod": "",
		"usage": ""
	}],
	"visited": False,
	"north_room": "",
	"south_room": "",
	"east_room": "Treasure Room",
	"west_room": "",
	"locked": False
}
room6["Pharaoh Mummy Room"] = {
	"name": "Treasure Room", 
	"descL": "Upon entering the room, you notice several sarcophagi that are ornately decorated with jewels and carvings of deities and animals in the stone.  However, time and nature has worn away at the decorations, but you can see that they were once beautiful.  In the corner, strange knocking and scraping noises are coming from one of the sarcophagi.",
	"descMod": "",
	"descS": "",
	"items": "",
	"features": [
	{
		"name": "Noisy Sarcophagus", 
		"desc": "Upon closer inspection, the strange noises coming from the sarcophagus get louder and louder",
		"descMod": "Upon opening the sarcophagus, a mythical pharaoh mummy jumps out, makes a loud screech, and then kills you",
		"usage": "Kills the player"
	},
	{
		"name": "Urn", 
		"desc": "There is a plain looking urn in the corner of the room.",
		"descMod": "Upon breaking open the urn, you see that it contains a yellow jeweled scarab necklace",
		"usage": ""
	}],
	"visited": False,
	"north_room": "Mirror Room",
	"south_room": "",
	"east_room": "",
	"west_room": "Main Passage",
	"locked": False
}	
room7["Mirror Room"] = {
	"name": "Mirror Room", 
	"descL": "Upon entering the room, you notice several polished copper mirrors along the walls.  There are bats and insects flying and crawling around and the mirrors amplify their numbers.  It is also hard to tell where everything is because of them. ",
	"descMod": "",
	"descS": "",
	"items": "",
	"features": [
	{
		"name": "Sculpture of Cat", 
		"desc": "There is a small stone sculpture of an egyptian cat next to a mirror in the corner.",
		"descMod": "",
		"usage": ""
	},
	{
		"name": "Spider", 
		"desc": "There is something rustling around in the room by one of the mirrors.",
		"descMod": "The rustling turns out to be a gigantic spider.  The spider bites you and causes pain and injury.  Lose 1 turn.",
		"usage": ""
	}],
	"visited": False,
	"north_room": "",
	"south_room": "Pharaoh Mummy Room",
	"east_room": "Skeleton Room",
	"west_room": "Guard's Room",
	"locked": False
}
room8["Skeleton Room"] = {
	"name": "Skeleton Room", 
	"descL": "Upon entering the room, you see bones and skulls scattered everywhere.  It is hard to tell how old they are or why they are there.  Perhaps they are previous explorers? It surprises you that there might be so many.",
	"descMod": "",
	"descS": "",
	"items": "",
	"features": [
	{
		"name": "Spider", 
		"desc": "There is something rustling around in the room by one of the sacks of food.",
		"descMod": "The rustling turns out to be a gigantic spider.  The spider bites you and causes pain and injury.  Lose 1 turn.",
		"usage": ""
	},
	{
		"name": "Sculpture of Scarab", 
		"desc": "There is a small stone sculpture of a scarab that looks like it was left as a gift for the great dead Pharaohs",
		"descMod": "",
		"usage": ""
	}],
	"visited": False,
	"north_room": "Food Room",
	"south_room": "",
	"east_room": "",
	"west_room": "Mirror Room",
	"locked": False
}
room9["Food Room"] = {
	"name": "Food Room", 
	"descL": "Upon entering the room, you find multiple sources of food.  There are sacks of grain and fruits.  The smell, however,  is putrid and you quickly realize that there is also mummified meat in this room.",
	"descMod": "",
	"descS": "",
	"items": "",
	"features": [
	{
		"name": "Book", 
		"desc": "There is a book laying next to a skull in the room, and it appears to be a previous explorer's journal.",
		"descMod": "",
		"usage": ""
	},
	{
		"name": "Elephant Tusk", 
		"desc": "There is an elephant tusk in the corner that looks untouched by time and geology",
		"descMod": "",
		"usage": ""
	}],
	"visited": False,
	"north_room": "",
	"south_room": "Skeleton Room",
	"east_room": "Mummified Animals Room",
	"west_room": "",
	"locked": False
}
room10["Mummified Animals Room"] = {
	"name": "Mummified Animals Room", 
	"descL": "Upon entering the room, you find that the air is putrid here too and realize that the room is filled with mummified pets.  There are birds, cats, crocodiles, baboons, vultures, and many others.  It's hard to tell, but one of the mummies seems to be shaking very slightly.  There are hieroglyphs on the walls too.",
	"descMod": "",
	"descS": "",
	"items": "",
	"features": [
	{
		"name": "Shaky Mummy", 
		"desc": "As you walk toward the shaking mummy, the shaking gets stronger and it appears that the mummy might still be alive.",
		"descMod": "Upon closer inspection, the mummy turns out to be a mythical crocodile. It bites your arm causing great pain before scampering off into the dark. Lose 1 turn.",
		"usage": ""
	},
	{
		"name": "Hieroglyphs", 
		"desc": "Upon closer inspection, the hieroglyphs say, 'Here lies the end of this branch of the tomb. You must turn around.'",
		"descMod": "",
		"usage": ""
	}],
	"visited": False,
	"north_room": "",
	"south_room": "",
	"east_room": "",
	"west_room": "Food Room",
	"locked": False
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

with open("room1.txt","w+") as f:
	f.write(s)
with open("room2.txt","w+") as f:
	f.write(t)
with open("room3.txt","w+") as f:
	f.write(u)
with open("room4.txt","w+") as f:
	f.write(v)
with open("room5.txt","w+") as f:
	f.write(w)
with open("room6.txt","w+") as f:
	f.write(x)
with open("room7.txt","w+") as f:
	f.write(y)
with open("room8.txt","w+") as f:
	f.write(z)
with open("room9.txt","w+") as f:
	f.write(a)
with open("room10.txt","w+") as f:
	f.write(b)
	
