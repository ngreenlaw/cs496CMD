#This is the main file for running the game
from __future__ import print_function
import json
import watson_developer_cloud
import sys
import egyptclass as ec
import os
import os.path

#Variables to hold things such that they are easier to edit
ITEM_FILES_VAR = "items.json";
FEATURE_FILES_VAR = "features.json";
ROOM_FILES_VAR = ["room1.json", "room2.json", "room3.json", "room4.json", "room5.json", "room6.json", "room7.json", "room8.json", "room9.json", "room10.json", "room11.json", "room12.json", "room13.json", "room14.json", "room15.json"];
r_a = ['room1','room2','room3','room4','room5','room6','room7','room8','room9','room10', 'room11','room12', 'room13', 'room14', 'room15']

#function for main menu, returns 0 if new game and 1 if load game, exits if exit is entered or returns 2 if it doesn't understand
def mainMenu():
    
	get_input = raw_input("Please enter if you would like to start a new game, load a game or quit: ");
	if get_input.lower() == "new game":
		return 0;
	elif get_input.lower() == "load game":
		return 1;
	elif get_input.lower() == "quit":
		sys.exit();
	else:
		print("I am not sure what you mean. Please try again.\n");
		return 2;

def intro():
    sys.stdout.write("\x1b[8;25;90t")
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')
    print('          _____ _   _______  _____ ___________   _____ ________  _________  ');
    print('         /  __ \ | | | ___ \/  ___|  ___|  _  \ |_   _|  _  |  \/  || ___ \ ');
    print('         | /  \/ | | | |_/ /\ `--.| |__ | | | |   | | | | | | .  . || |_/ / ');
    print('         | |   | | | |    /  `--. \  __|| | | |   | | | | | | |\/| || ___ \ ');
    print('         | \__/\ |_| | |\ \ /\__/ / |___| |/ /    | | \ \_/ / |  | || |_/ / ');
    print('          \____/\___/\_| \_|\____/\____/|___/     \_/  \___/\_|  |_/\____/  \n');
                
    print("     Egypt 1926, Valley of the kings - Archeologist Charles Carter is on the verge of discovering the tomb of the great sorcerer to Rameses II. On opening the tomb, Charles ventures in alone, not sure of what dangers lie ahead. As soon as he steps foot into the first chamber a pressure lever is triggered sliding a giant stone wheel in front of the opening. Leaving him trapped in the tomb with only his trusty torch. You must help Carter complete his expedition and escape!\n");
          
    return 0;
                
#these functions get the object from the name, returns 1 if there is an error
def getItemFromName(list_i, item):
	for i in range(0, len(list_i)):
		if item == list_i[i].name:
			return list_i[i];
	return 1;
	
def getFeatureFromName(list_f, feature):
	for i in range(0, len(list_f)):
		if feature == list_f[i].name:
			return list_f[i];
	return 1;
	
def getRoomFromName(list_r, room):
	for i in range(0, len(list_r)):
		if i != None:
			if room == list_r[i].name:
				return list_r[i];
	return 1;

def getItemFromParser(list_i, item):
	for i in range(0, len(list_i)):
		if item == list_i[i].parser:
			return list_i[i];
	return 1;
	
def getFeatureFromParser(list_f, feature):
	for i in range(0, len(list_f)):
		if feature == list_f[i].parser:
			return list_f[i];
	return 1;
	
#function to create the items
def createItem(files_list):
	list_of_objects = [];

	f = open(files_list, "r");
	rf = f.read();
	fj = json.loads(rf);
	f.close()

	for f_item in fj:
		i = f_item['name']
		j = f_item['desc']
		k = f_item['parser']
		object_created = ec.Item(i,j,k);
		list_of_objects.append(object_created);
		
	return list_of_objects;

#function to create the features
def createFeature(files_list):
	list_of_objects = [];
	
	f = open(files_list, "r");
	rf = f.read();
	fj = json.loads(rf);
	f.close()

	for f_feature in fj:
		i = f_feature['name']
		j = f_feature['desc']
		k = f_feature['descMod']
		x = f_feature['parser']
		object_created = ec.Feature(i,j,k,x);
		list_of_objects.append(object_created);
		
	return list_of_objects;

def createFeatureLoad(name):
	list_of_objects = [];
	f = open(name, "r");
	rf = f.read();
	fj = json.loads(rf)[2];
	f.close()

	fj_f = fj['feature']

	for f_feature in fj_f:
		object_created = ec.Feature(fj_f[f_feature]['name'], fj_f[f_feature]['desc'], fj_f[f_feature]['descMod'], fj_f[f_feature]['parser']);
		descMod = True;
		if fj_f[f_feature]['descModBool'] == "False":
			descMod = False;
		object_created.modified_description_bool = descMod;
		list_of_objects.append(object_created);
	return list_of_objects;
	
#function to set the north, south, east and west rooms after the create function to replace the names with the room object itself
def createRoomNSEW(roomList):
	for r in roomList:
		if r.north_room == "":
			r.north_room = None;
		else:
			for ro in roomList:
				if ro.name == r.north_room:
					r.north_room = ro;
					break;

		if r.south_room == "":
			r.south_room = None;
		else:
			for ro in roomList:
				if ro.name == r.south_room:
					r.south_room = ro;
					break;
					
		if r.east_room == "":
			r.east_room = None;
		else:
			for ro in roomList:
				if ro.name == r.east_room:
					r.east_room = ro;
					break;
					
		if r.west_room == "":
			r.west_room = None;
		else:
			for ro in roomList:
				if ro.name == r.west_room:
					r.west_room = ro;
					break;
					
#function to create the rooms
def createRoom(files_list):

	list_of_objects = [];
	
	#read the files
	for fi in files_list:
		f = open(fi, "r");
		rf = f.read();
		fj = json.loads(rf);
		f.close();
		
		tf_lock = True;
		if fj['locked'] == "False":
			tf_lock = False;

		object_created = ec.Room(fj['name'], fj['descL'], fj['descS'], fj['items'], fj['features'], tf_lock,fj['north_room'],fj['south_room'],fj['east_room'],fj['west_room']);
		
		list_of_objects.append(object_created);
	return list_of_objects;
	
def createRoomLoad(fname):
	list_of_objects = [];
	f = open(fname, "r");
	rf = f.read();
	fj = json.loads(rf)[1];
	f.close()
	

	global r_a;
	
	for i in range(0, len(r_a)):
		tf_lock = True;
		if fj['rooms'][r_a[i]]['locked'] == "False":
			tf_lock = False;
		
		tf_visit = True;
		if fj['rooms'][r_a[i]]['visited'] == "False":
			tf_visit = False;
			
		object_created = ec.Room(fj['rooms'][r_a[i]]['name'], fj['rooms'][r_a[i]]['descL'], fj['rooms'][r_a[i]]['descS'], fj['rooms'][r_a[i]]['items'], fj['rooms'][r_a[i]]['features'], tf_lock, fj['rooms'][r_a[i]]['north_room'], fj['rooms'][r_a[i]]['south_room'], fj['rooms'][r_a[i]]['east_room'], fj['rooms'][r_a[i]]['west_room']);
		object_created.visited = tf_visit;
		list_of_objects.append(object_created);
	return list_of_objects;
	
	
#function to create the player
def createPlayer(items, tc, cr):
	p = ec.Player(items, tc, cr);
	return p;

#function to create the player
def createPlayerLoad(name, rooms):
	f = open(name, "r");
	rf = f.read();
	fj = json.loads(rf)[0];
	f.close()
	
	for r in rooms:
		if r.name == fj['player']['current_room']:
			ro = r
			break;

	p = ec.Player(fj['player']['inventory'], fj['player']['turn_count'], ro);
	p.ears = fj['player']['ears']
	return p;
	
#function to save the game

def saveGame(player, feat, rooms):
	name = raw_input("What would you like to call the save file?\n");
	data = []
	
	#Player data
	player_data = {
		'player': {
			'inventory': player.inventory,
			'ears': player.ears,
			'turn_count': player.turn_count,
			'current_room': player.current_room.name
			}
		}
	data.append(player_data);
	
	#Room data
	room_data = {
		'rooms':{
			}
		}
		
	global r_a;
		
	for i in range(0, len(r_a)):
		room_data['rooms'].update({r_a[i]:{}})

	for i in range(0,len(r_a)):

		room_data['rooms'][r_a[i]]['name'] = rooms[i].name
		room_data['rooms'][r_a[i]]['descL'] = rooms[i].long_description
		room_data['rooms'][r_a[i]]['descS'] = rooms[i].short_description
		room_data['rooms'][r_a[i]]['items'] = rooms[i].items
		room_data['rooms'][r_a[i]]['features'] = rooms[i].features

		true_false = "";

		if rooms[i].visited == True:
			true_false = "True"
		else:
			true_false = "False"

		room_data['rooms'][r_a[i]]['visited'] = true_false;

		if rooms[i].locked == True:
			true_false = "True"
		else:
			true_false = "False"


		room_data['rooms'][r_a[i]]['locked'] = true_false;
		
		nr = rooms[i].north_room;
		sr = rooms[i].south_room;
		er = rooms[i].east_room;
		wr = rooms[i].west_room;
		
		if nr == None:
			nr = "";
		else:
			nr = nr.name;
			
		if sr == None:
			sr = "";
		else:
			sr = sr.name;
			
		if er == None:
			er = "";
		else:
			er = er.name;
			
		if wr == None:
			wr = "";
		else:
			wr = wr.name;
		
		room_data['rooms'][r_a[i]]['north_room'] = nr
		room_data['rooms'][r_a[i]]['south_room'] = sr
		room_data['rooms'][r_a[i]]['east_room'] = er
		room_data['rooms'][r_a[i]]['west_room'] = wr		

	data.append(room_data);
	
	#Feature data
	feature_data = {
		'feature':{
			}
		}
	for i in range(0,len(feat)):
		feature_data['feature'].update({str(i):{}})
		m_b = "True"
		if feat[i].modified_description_bool == False:
			m_b = "False"
	
		feature_data['feature'][str(i)]['name'] = feat[i].name;
		feature_data['feature'][str(i)]['desc'] = feat[i].description;
		feature_data['feature'][str(i)]['descMod'] = feat[i].modified_description;
		feature_data['feature'][str(i)]['parser'] = feat[i].parser;
		feature_data['feature'][str(i)]['descModBool'] = m_b;
	
	data.append(feature_data);
	
	name = name + '.json'
	with open(name, 'w') as outfile:
		j = json.dumps(data, indent=4)
		outfile.write(j)
		outfile.close()
	
	print("Game successfully saved to " + name +"\n");
	
	return 0;

#functions to get the input and parse it
class DictQuery(dict):
    def get(self, path, default = None):
        keys = path.split("/")
        val = None
        
        for key in keys:
            if val:
                if isinstance(val, list):
                    val = [ v.get(key, default) if v else None for v in val]
                else:
                    val = val.get(key, default)
            else:
                val = dict.get(self, key, default)
            
            if not val:
                break;
        return val

assistant = watson_developer_cloud.AssistantV1(
                                               username='171ad7e1-fd51-4399-ba54-87fd88b8775f',
                                               password='EZ22BDDwOTao',
                                               version='2018-05-01'
                                               )

def getInput():
	#FILL IN THE FUNCTIONS WITH THE NATURAL LANGUAGE PARSER OR IMPORT THE MODULE
	#RETURNS THE TAG TO BE PROCESSED
    text = ''
    response = ''
    while text != 'quit':
        text = raw_input('>> ')
        response = assistant.message(
                                     workspace_id='6e437ce3-3817-47ba-971c-c39142841f73',
                                     input={
                                     'text': text
                                     }
                                     )
        data = json.dumps(response)
        return(", ".join(DictQuery(response).get('output/text')))     

#functions to resolve the action and update necessary variables
#Returns if a turn should be used up is 1, 0 if not
def processTag(returned_tag, player, ite, fea, rooms):
	
	#Check the I didnt understand result and ask to get input again
	nu = "I didn\'t understand. You can try rephrasing.";

	while(returned_tag == nu):
		print(nu);
		returned_tag = getInput();
	
	#Set up the needed variables
	cr = player.current_room;
	
	#set up the items list
	all_items_look = [];
	all_items_drop = [];
	all_items_take = [];
	features_touch = [];
	features_look = [];
	all_items_use = [];
	all_items_hit = [];
	
	#list of objects
	features_objects = [];
	items_objects = [];

	items_in_room = cr.items[:];
	items_to_take = cr.items[:];
	features_in_room = cr.features[:];
	items_in_inventory = player.inventory[:];
	all_items = items_in_room[:];
	
	for y in features_in_room:
		x = getFeatureFromName(fea, y);
		features_objects.append(x)
		features_look.append("look at " + x.parser);

	for y in items_in_inventory:
		i = getItemFromName(ite, y)
		all_items.append(i.name);
		all_items_drop.append("drop " + i.parser);
		all_items_use.append("use " + i.parser);
	
	for y in all_items:
		j = getItemFromName(ite, y)
		items_objects.append(j)
		all_items_look.append("look at " + j.parser);
		all_items_hit.append("hit " + j.parser);
	
	for y in items_to_take:
		k = getItemFromName(ite, y)
		all_items_take.append("take " + k.parser);
	
	for y in features_in_room:
		n = getFeatureFromName(fea, y)
		features_touch.append("touch " + n.parser);

	#Create ambiguous commands list
	ww = "What would you like to ";
	amb_comm = ["look at?", "drop?", "take?", "hit?", "touch?", "use?"]
	all_amb = [];
	for a in amb_comm:
		all_amb.append(ww+a);
		#print(ww+a)#DEBUG PRINT
	all_amb.append("Where would you like to move?");

	#Set up the variables that will execute certain functions
	direction = ["go north", "go south", "go east", "go west"];
	amb = all_amb[:];
	look_at_item = all_items_look;
	look_at_feature = features_look;
	help_display = "help";
	player_inventory = "show inventory";
	take_item = all_items_take;
	drop_item = all_items_drop;
	use_item = all_items_use;
	hit_target = all_items_hit; #DO THIS FUNCTION
	touch_feature = features_touch;	
	save_game = "save game"
	load_game = "load game"
		
	#use and touch both return touch

	if returned_tag == "look at room" and cr.name == "Chamber of Passing" and cr.short_description == "You are in a completely pitch black room. You cannot see anything.":
		print(cr.short_description);
		return 0;

	#Process the tag based on what is returned, includes the verbs used in the game
	#Display the description if the returned tag is look at room but otherwise handle the ambiguous input
	if returned_tag in amb:
		print (returned_tag)
		com_given = raw_input("Enter name or direction(north/south/east/west)>> ")
		
		av_array = look_at_feature[:]
		for i in look_at_item:
			av_array.append(i)
		for i in take_item:
			av_array.append(i)
		for i in drop_item:
			av_array.append(i)
		for i in use_item:
			av_array.append(i)
		for i in hit_target:
			av_array.append(i)
		for i in touch_feature:
			av_array.append(i)
		for i in direction[:]:
			av_array.append(i)	
		av_array.append("quit")
		av_array.append("look at room")

		if returned_tag == "Where would you like to move?":
			if com_given.lower() == "north":
				com_given = "go " + "north";
			if com_given.lower() == "south":
				com_given = "go " + "south";
			if com_given.lower() == "east":
				com_given = "go " + "east";
			if com_given.lower() == "west":
				com_given = "go " + "west";

		elif returned_tag == "What would you like to look at?":
			both_objects = features_objects[:]
			both_objects.append(items_objects)
			x = getFeatureFromName(features_objects, com_given)
			if x != 1:
				com_given = "look at " + x.parser
			
		elif returned_tag == "What would you like to drop?":
			x = getItemFromName(items_objects, com_given)
			if x != 1:
				com_given = "drop " + x.parser;
			
		elif returned_tag == "What would you like to take?":
			x = getItemFromName(items_objects, com_given)
			if x != 1:
				com_given = "take " + x.parser;
					
		elif returned_tag == "What would you like to hit?":
			x = getItemFromName(items_objects, com_given)
			if x != 1:
				com_given = "hit " + x.parser;
					
		elif returned_tag == "What would you like to touch?":
			x = getFeatureFromName(features_objects, com_given)
			if x != 1:
				com_given = "touch " + x.parser;
					
		elif returned_tag == "What would you like to use?":
			x = getItemFromName(items_objects, com_given)
			if x != 1:
				com_given = "use " + x.parser;
		
		returned_tag = com_given;
				
		while(returned_tag not in av_array):
			print("That is not a valid item/feature/direction/command.")
			return 0;
		
		if returned_tag == "quit":
			print("Exiting game.")
			exit()			

		if returned_tag == "look at room":
			print(cr.name + ": " + cr.displayDescription());
			nsew_rooms = [cr.north_room, cr.south_room, cr.east_room, cr.west_room];
			
			ro = 0;
			for r in nsew_rooms:
				if r != None:
					if ro == 0:
						print("There appears to be an entrance to another room on the north wall");
					elif ro == 1:
						print("There appears to be an entrance to another room on the south wall");
					elif ro == 2:
						print("There appears to be an entrance to another room on the east wall");
					elif ro == 3:
						print("There appears to be an entrance to another room on the west wall");
				ro+=1;

			print("\nFeatures of Note:");
			for f in features_objects:
				print(f.name + ": " + f.displayDescription());
			if len(items_in_room) != 0:
				print("\nItems in room:");
				for i in items_in_room:
					print(i);
				print("");
			else:
				print("\nThere are no items in this room to be picked up.\n");	
			return 0;

	if returned_tag == "quit":
		print("Exiting game.")
		exit()			

	
	#Move Room if the returned Tag is a direction
	elif returned_tag in direction:
		#crossing the river
		d = "You are in a small room with a river flowing through the middle from west to east. On the north side of the river is a door and on opposite sides of the river are mermaid statues. You can hear beautiful singing."
		if cr.name == "Nile River" and returned_tag == "go north" and cr.short_description == d:
			if player.ears != "plugged":
				print("You attempt to cross the river and the siren's song keeps you from concentrating as you stumble and begin to drown.")
				print("You stumble back out of the river taking many deep breaths using up what precious little air you have left. There has to be a way to block the Siren's Song from your ears.\n")
				return 5;

			else:
				print("You successfully cross the river. And the Siren's Song stops.\n")
				cr.short_description = "You are in a small room with a river flowing through the middle from west to east. On the north side of the river is a door and on opposite sides of the river are mermaid statues."
				return 1;
				
		m = player.moveRoom(returned_tag);
		if m == 1: #If there is no room
			return 0; #return no turn taken up
		else:
			print("");
			print(player.current_room.displayDescription());
			print("");
			player.current_room.visited = True;
			return 1; #return turn taken up
	
	#Look at room
	elif returned_tag == "look at room":
		print(cr.name + ": " + cr.displayDescription());
		nsew_rooms = [cr.north_room, cr.south_room, cr.east_room, cr.west_room];
		
		ro = 0;
		for r in nsew_rooms:
			if r != None:
				if ro == 0:
					print("There appears to be an entrance to another room on the north wall");
				elif ro == 1:
					print("There appears to be an entrance to another room on the south wall");
				elif ro == 2:
					print("There appears to be an entrance to another room on the east wall");
				elif ro == 3:
					print("There appears to be an entrance to another room on the west wall");
			ro+=1;

		print("\nFeatures of Note:");
		for f in features_objects:
			print(f.name + ": " + f.displayDescription());
		if len(items_in_room) != 0:
			print("\nItems in room:");
			for i in items_in_room:
				print(i);
			print("");
		else:
			print("\nThere are no items in this room to be picked up.\n");	
		return 0;


	#Display the description if the returned tag is look item
	#returned_tag == look at <item> ex: look at torch
	elif returned_tag in look_at_item:
		ret = getItemFromParser(items_objects, returned_tag[8:])
		print(ret.displayDescription());
		print("");
		return 0;
	
	#Display description for feature
	elif returned_tag in look_at_feature: 
		d = "You are in a small room with a river flowing through the middle from west to east. On the north side of the river is a door and on opposite sides of the river are mermaid statues. You can hear beautiful singing."
		ret = getFeatureFromParser(features_objects, returned_tag[8:]);
		#Search through the items list and then compare the name to the returned tag
		if returned_tag == "look at sphinx":
			#ret = getFeatureFromParser(features_objects, returned_tag[8:]);
			print(ret.displayDescription());
			print("")

			if ret.modified_description_bool == False:
				print("Would you like to solve the puzzle? (yes/no)")
				get_input = raw_input(">> ")
				while get_input.lower() != "yes" and get_input.lower() != "no":
					print("Input yes or no please.")
					get_input = raw_input(">> ")
				if get_input == "yes":
					print("What is your answer?")
					get_input = raw_input(">> ")
					if get_input.lower() == "day and night" or get_input.lower() == "night and day":
						print("A loud sound of \"Correct!\" bursts out from the sphinx as a scarab like hole in it's chest appears.\n")
						ret.modified_description_bool = True;
					else:
						print("You hear the sphinx chortle a little. It seems you were incorrect.\n")
						return 0;
				else:
					print("You hear the sphinx chortle a little.\n")
					return 0;
			else:
				return 0;

		elif returned_tag == "look at adventurer":
			#ret = getFeatureFromParser(features_objects, "adventurer")
			if ret.modified_description_bool == False:
				print(ret.displayDescription())
				print("You decide to take the earplugs.\n");
				ret.modified_description_bool = True;
				i = getItemFromName(ite, "Earplugs");
				print(i.name + ":" + i.description)
				print("Added Earplugs to your inventory.\n")
				player.inventory.append("Earplugs");
				return 0;
					
		elif returned_tag == "look at door" and cr.name == "Nile River" and cr.short_description == d:
			print("You cannot see it well across the river.\n")
			return 0;
			
		elif returned_tag == "look at journal":
			print("You read the journal and it says:")
			print(ret.modified_description)
			print("")
			return 1;		

		else:
			#ret = getFeatureFromParser(features_objects, returned_tag[8:])
			print(ret.displayDescription());
			print("");
		return 0;
	
	#Display help function
	elif returned_tag == help_display:
		print("Verbs that can be used:") 
		verbs = ["help", "look at", "look at room", "inventory", "quit", "save game", "load game", "use", "touch", "hit", "take", "drop", "move", "go"]
		for i in verbs:
			print(i);
		print("");
		return 0;
		
	#Display inventory
	elif returned_tag == player_inventory:
		if len(player.inventory) != 0:
			print("In inventory:");
			for i in player.inventory:
				print(i);
			print("");
		else:
			print("No Items in inventory\n");
		return 0;
		
	elif returned_tag in drop_item:
		ret = getItemFromParser(items_objects, returned_tag[5:]);
		#TORCH DROPPING FOR ROOM 3
		if returned_tag == "drop torch" and cr.name == "Antechamber 1":
			#ret = getItemFromParser(items_objects, returned_tag[5:]);
			print("Dropped " + ret.name + " on the ground.\n");
			player.removeFromInventory(ret.name);
			print("When the torch hits the ground you notice on the wall the holes repeat the pattern: up, down, down, up.\n");
			return 1;
			
		########################URN DROPPING HERE
		elif returned_tag == "drop urn":				
			#ret = getItemFromParser(items_objects, returned_tag[5:]);
			print("Dropped " + ret.name + " on the ground.\n");
			player.removeFromInventory(ret.name);
			cr.items.remove("Urn")
			print("Upon dropping the urn, it lands on the ground and breaks open revealing a shiny brooch. You decide to pick it up and add it to your inventory.\n");
			cr.items.append("Scarab Brooch")
			player.addToInventory("Scarab Brooch")
			return 1;
		
		########################################################
		
		#EVERYTHING ELSE 
		else:
			#ret = getItemFromParser(items_objects, returned_tag[5:]);
			print("Dropped " + ret.name + " on the ground.\n");
			player.removeFromInventory(ret.name);
		return 0;
			
	elif returned_tag in take_item: 
		#specific thing for taking item
		if returned_tag == "take brooch" and cr.name == "Chamber of Passing":
			f = getFeatureFromParser(features_objects, "chimera");
			f.modified_description_bool = True;

		elif returned_tag == "take necklace" and cr.name == "Chamber of Passing":
			f = getFeatureFromParser(features_objects, "jackal"); #COULD DO SOMETHING HERE WITH DISPLAYING DESC IN IF STATEMENT BASED ON MODBOOL
			f.modified_description_bool = True;

		elif returned_tag == "take ancient artifact" and cr.name == "Burial Chamber":
			f = getFeatureFromParser(features_objects, "large tomb");
			f.modified_description_bool = True;

		
		ret = getItemFromParser(items_objects, returned_tag[5:]);
		print(ret.name + ": " + ret.displayDescription());
		print("Added " + ret.name + " to inventory.\n");
		player.addToInventory(ret.name);
		return 1;

	elif returned_tag in touch_feature:
		d = "You are in a small room with a river flowing through the middle from west to east. On the north side of the river is a door and on opposite sides of the river are mermaid statues. You can hear beautiful singing."
		if returned_tag == "touch door" and cr.short_description == d:
			print("You have to move across the river to touch it first.\n")
			return 0;
	
		else:
			ret = getFeatureFromParser(features_objects, returned_tag[6:]);
			turn_x = ret.touchFeature(player);
			return turn_x;
	
	elif returned_tag in use_item:
		if returned_tag == "use earplugs":
			if cr.name == "Nile River":
				print("You can no longer hear the Siren's Song. You feel more confident crossing the River.\n")
			else:
				print("You place the earplugs in your ears. They help to deafen the sounds of the tomb.\n")
			player.ears = "plugged"
			return 1;

		if returned_tag == "use torch" and cr.name == "Chamber of Passing":
			d = "You see writings all across the north wall. On the east wall is a staircase that leads down and on the west wall are a jackal and chimera statue facing the staircase."
			if cr.short_description != d:
				print("You light up your torch and next to you is a brazier to light and when you do so you can now see the room.\n");
				print(d)
				print("")
				cr.short_description = d;
				return 1;
			else:
				print("You tried to use the Torch and nothing happens.\n");

			###################################HERE IS WHERE ANY ADDITIONAL USE CODE FOR ITEMS GOES
			#YOU CAN USE THE ABOVE CODE AS A GUIDE
	



			####################################################################################

		else:
			ret = getItemFromParser(items_objects, returned_tag[4:]);
			print("You tried to use the " + ret.name + " and nothing happens.\n");
			return 0;	

	elif returned_tag in hit_target:
		ret = getItemFromParser(items_objects, returned_tag[4:])
		
		if ret.name == "Urn" and "Urn" in cr.items:
			if "Elephant's Tusk" in player.inventory:
				print("Upon hitting the urn with the Elephant's Tusk, it breaks open revealing a shiny brooch. You decide to pick it up and add it to your inventory.\n");
				cr.items.append("Scarab Brooch")
				player.addToInventory("Scarab Brooch")
				cr.items.remove("Urn")
				return 0;
			else:
				print("You hit the urn and nothing happens except your hand hurts.")
				return 0;
		else:
			print("You tried to hit the " + ret.name + " and nothing happens.\n")
			return 0;
	
	elif returned_tag == save_game:
		saveGame(player, fea, rooms);
		return 0;
	
	elif returned_tag == load_game:
		return -1;
	#...
	#...
	
	
	print("You cannot do that.\n");
	return 0;

#CONVERT THE MAIN FUNCTION TO THIS AND RETURN -1 FOR PROCESS TAG IN 	
def playGame(get_main_menu_result):
#Process command from main menu
	#new game issued
	global ITEM_FILES_VAR;
	if get_main_menu_result == 0:
		#Begin creating game
		
		#Create items for the whole game
		items = createItem(ITEM_FILES_VAR);
		
		#Create items for the whole game
		global FEATURE_FILES_VAR;
		features = createFeature(FEATURE_FILES_VAR);
		
		#Create rooms for the whole game
		global ROOM_FILES_VAR
		rooms = createRoom(ROOM_FILES_VAR);
		createRoomNSEW(rooms);
		
		#Create player
		starting_inventory = ["Torch"];
		player = createPlayer(starting_inventory, 90, rooms[0]);
		
	#Load game
	elif get_main_menu_result == 1:
		#BEGIN GAME LOADING
		name = raw_input("What is the name of the file to load? (Without the extension)\n")
		if name.lower() == "quit":
			exit()
		name = name +'.json'
		contin = 0;
		if os.path.isfile(name):
			contin = 1;
		while contin == 0:
			print("There is no file by that name. Try again. Or type quit to exit.\n")
			name = raw_input("What is the name of the file to load? (Without the extension)\n")
			if name.lower() == "quit":
				exit()
			name = name +'.json'
			if os.path.isfile(name):
				contin = 1;
		
    		os.system('cls' if os.name == 'nt' else 'clear')
		#DO THINGS WITH LOADING
		#Begin creating game
		
		#Create items for the whole game
		items = createItem(ITEM_FILES_VAR);
		
		#Create items for the whole game
		features = createFeatureLoad(name);
		
		#Create rooms for the whole game
		rooms = createRoomLoad(name);
		createRoomNSEW(rooms);
		
		#Create player
		player = createPlayerLoad(name, rooms);

	else:
		print("DEBUG - SOMETHING WENT WRONG IN THE MAIN MENU, THIS SHOULD NOT HAPPEN");
		exit()
	
	#Begin Game
	#While the turn count is > 0

	print("Verbs that may be of help to know:")
	verbs = ["help", "look at", "look at room", "inventory", "quit", "save game", "load game", "use", "touch", "hit", "take", "drop", "move", "go"]
	for i in verbs:
		print(i);
	print("");

	
	turns_left = player.turn_count;
	cr = player.current_room;
	print("");
	print(cr.displayDescription());
	print("");
	cr.visited = True;	
	
	while turns_left > 0:
		turn = 0;
		print("Amount of air left: " + str(turns_left))
		print("")
		#Display description
		cr = player.current_room;
		#print(cr.displayDescription());
		
		#Get input and resolve actions
		input_given = getInput();

		#Display result / if error then do not print result
		turn = processTag(input_given, player, items, features, rooms);
		if turn == -1:
			return -1;
		
		#Reduce turn count
		player.turn_count = turns_left-turn;
		turns_left = player.turn_count;

	if turns_left <= 0:
		print("You have unfortunately ran out of air.");
		print("GAME OVER");
		return 1;

def main():
	# Display's intro
	intro()
	#Start Main Menu, until a result of save, load or exit is given, repeat asking for input
	get_main_menu_result = 2;
	while get_main_menu_result == 2:
		get_main_menu_result = mainMenu();
		
	g = 0;
	while g <= 0:
		if g == -1:
			g = playGame(1);
		else:
			g = playGame(get_main_menu_result)
	return 0;
	
			
#run the program
if __name__ == "__main__":
	main();
