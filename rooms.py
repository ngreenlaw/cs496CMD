import json
rooms = {}
rooms["Entry"] = {
	"name": "Entry",
	"descL": "The large entry way into the tomb, there are hieroglyphs on each of the walls. There is a large doorway in front of you that looks like it leads to a larger space.",
	"descMod": "",
	"descAdd": "",
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
		"desc": "On the right side of the room the hieroglyphs says 'The key to my return lies within the heart of the underworld'",
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
	"visited": False,
	"north_room": "Main Passage",
	"south_room": "",
	"east_room": "",
	"west_room": "",
	"locked": False
}	
rooms["Main Passage"] =	{
    "name": "Main Passage", 
	"descL": "As you move into the main passageway you notice that the air is a little thinner in here, might be a good idea to find an exit before the air in the tomb runs out. On the wall in front of you there is what looks like a large cylinder with different markings on it.",
	"descMod": "",
	"descAdd": "",
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
rooms["Antechamber 1"] = {
"name": "Antechamber 1", 
	"descL": "Upon entering the chamber you notice a door right in front of you covered in four switches, there is nothing in the chamber except that the walls are covered in hieroglyphs. While walking by one of them you notice that a small hole in the wall seemed to light up as you passed by.",
	"descMod": "",
	"descAdd": "",
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
rooms["Antechamber 2"] = {
	"name": "Antechamber 2", 
	"descL":"As you enter the antechamber you notice that the door behind you starts to close, it must have been something you stepped on. Along the wall the hieroglyphs seem to keep saying the same thing. 'Believe in me as all are descendants from me.'",
	"descMod": "",
	"descAdd": "",
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
rooms["Treasure Room"] = {
	"name": "Treasure Room", 
	"descL": "As you enter the room you notice that this should be the treasury room. A room that was once full of gold to make sure the sorcerer could pay his way into the afterlife. However, this room must have been raided millenia ago, all that remains are that of bones around three large statues. I might want to be careful I don't meet the same fate as the rest of these men.",
	"descMod": "",
	"descAdd": "",
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

s = json.dumps(rooms)

with open("rm.txt","w+") as f:
	f.write(s)
