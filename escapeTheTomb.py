#This is the main file for running the game
from __future__ import print_function
import json
import watson_developer_cloud
import sys
import egyptclass as ec
import os
import os.path

#Variables to hold things such that they are easier to edit
ITEM_FILES_VAR = ["items.json"];
FEATURE_FILES_VAR = ["features.json"];
ROOM_FILES_VAR = ["room1.json", "room2.json", "room3.json", "room4.json", "room5.json", "room6.json", "room7.json", "room8.json", "room9.json", "room10.json", "room11.json", "room12.json", "room13.json", "room14.json", "room15.json"];
r_a = ['room1','room2','room3','room4','room5','room6','room7','room8','room9','room10', 'room11','room12', 'room13', 'room14', 'room15']

#function for main menu, returns 0 if new game and 1 if load game, exits if exit is entered or returns 2 if it doesn't understand
def mainMenu():
    
	get_input = raw_input("Please enter if you would like to start a new game, load a game or exit: ");
	if get_input.lower() == "new game":
		return 0;
	elif get_input.lower() == "load game":
		return 1;
	elif get_input.lower() == "exit":
		sys.exit();
	else:
		print("I am not sure what you mean. Please try again.\n");
		return 2;

def intro():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print('          _____ _   _______  _____ ___________   _____ ________  _________  ');
    print('         /  __ \ | | | ___ \/  ___|  ___|  _  \ |_   _|  _  |  \/  || ___ \ ');
    print('         | /  \/ | | | |_/ /\ `--.| |__ | | | |   | | | | | | .  . || |_/ / ');
    print('         | |   | | | |    /  `--. \  __|| | | |   | | | | | | |\/| || ___ \ ');
    print('         | \__/\ |_| | |\ \ /\__/ / |___| |/ /    | | \ \_/ / |  | || |_/ / ');
    print('          \____/\___/\_| \_|\____/\____/|___/     \_/  \___/\_|  |_/\____/  \n');
                
    print("     Egypt 1926, Valley of the kings - Archeologist Charles Carter is on the verge of discovering the tomb of the great sorcerer to Rameses II. On opening the tomb, Charles ventures in alone, not sure of what dangers lie ahead. As soon as he steps foot into the first chamber a pressure lever is triggered sliding a giant stone wheel in front of the opening. Leaving him trapped in the tomb with only his trusty torch.\n");
          
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
		
#function to create the items
def createItem(files_list):
	#FIX BASED ON WHAT THE JSON FILE IS
	object_created = None;
	list_of_objects = [];
	#read the files
	for fi in files_list:
		f = open(fi, "r");
		rf = f.read();
		fj = json.loads(rf);
		f.close()
		
		#create the object HERE IS WHERE TO EDIT
	for f_item in fj:
		object_created = ec.Item(f_item['name'], f_item['desc']);
		list_of_objects.append(object_created);
		
	return list_of_objects;

#function to create the features
def createFeature(files_list):
	#FIX BASED ON WHAT THE JSON FILE IS
	object_created = None;
	list_of_objects = [];
	
	#read the files
	for fi in files_list:
		f = open(fi, "r");
		rf = f.read();
		fj = json.loads(rf);
		f.close()
		
	#create the object HERE IS WHERE TO EDIT
	for f_feature in fj:
		object_created = ec.Feature(f_feature['name'], f_feature['desc'], f_feature['descMod'], f_feature['usage']);
		list_of_objects.append(object_created);
		
	return list_of_objects;

def createFeatureLoad(name):
	#FIX BASED ON WHAT THE JSON FILE IS
	object_created = None;
	list_of_objects = [];
	
	list_of_objects = [];
	f = open(name, "r");
	rf = f.read();
	fj = json.loads(rf)[3];
	f.close()

	fj_f = fj['feature']
	#create the object HERE IS WHERE TO EDIT
	for f_feature in fj_f:
		object_created = ec.Feature(fj_f[f_feature]['name'], fj_f[f_feature]['desc'], fj_f[f_feature]['descMod'], fj_f[f_feature]['usage']);
		list_of_objects.append(object_created);
	return list_of_objects;
	
#function to set the north, south, east and west rooms after the create function to replace the names with the room object itself
def createRoomNSEW(roomList):
	for r in roomList:
		if r.getNorthRoom() == "":
			r.setNorthRoom(None);
		else:
			for ro in roomList:
				if ro.getName() == r.getNorthRoom():
					r.setNorthRoom(ro);
					break;

		if r.getSouthRoom() == "":
			r.setSouthRoom(None);
		else:
			for ro in roomList:
				if ro.getName() == r.getSouthRoom():
					r.setSouthRoom(ro);
					break;
					
		if r.getEastRoom() == "":
			r.setEastRoom(None);
		else:
			for ro in roomList:
				if ro.getName() == r.getEastRoom():
					r.setEastRoom(ro);
					break;
					
		if r.getWestRoom() == "":
			r.setWestRoom(None);
		else:
			for ro in roomList:
				if ro.getName() == r.getWestRoom():
					r.setWestRoom(ro);
					break;
					
#function to create the rooms
def createRoom(files_list):
	#FIX BASED ON WHAT THE JSON FILE IS
	object_created = None;
	list_of_objects = [];
	#read the files
	for fi in files_list:
		f = open(fi, "r");
		rf = f.read();
		fj = json.loads(rf);
		f.close();
		
		tf_lock = True;
		#create the object HERE IS WHERE TO EDIT
		if fj['locked'] == "False":
			tf_lock = False;
		object_created = ec.Room(fj['name'], fj['descL'], fj['descS'], fj['items'], fj['features'], tf_lock);
		object_created.setNorthRoom(fj['north_room']);
		object_created.setSouthRoom(fj['south_room']);
		object_created.setEastRoom(fj['east_room']);
		object_created.setWestRoom(fj['west_room']);
		list_of_objects.append(object_created);
	return list_of_objects;
	
def createRoomLoad(fname):
	list_of_objects = [];
	f = open(fname, "r");
	rf = f.read();
	fj = json.loads(rf)[2];
	f.close()
	

	global r_a;
	
	for i in range(0, len(r_a)):
		tf_lock = True;
		if fj['rooms'][r_a[i]]['locked'] == "False":
			tf_lock = False;
		
		tf_visit = True;
		if fj['rooms'][r_a[i]]['visited'] == "False":
			tf_visit = False;
			
		object_created = ec.Room(fj['rooms'][r_a[i]]['name'], fj['rooms'][r_a[i]]['descL'], fj['rooms'][r_a[i]]['descS'], fj['rooms'][r_a[i]]['items'], fj['rooms'][r_a[i]]['features'], tf_lock);
		object_created.setNorthRoom(fj['rooms'][r_a[i]]['north_room']);
		object_created.setSouthRoom(fj['rooms'][r_a[i]]['south_room']);
		object_created.setEastRoom(fj['rooms'][r_a[i]]['east_room']);
		object_created.setWestRoom(fj['rooms'][r_a[i]]['west_room']);
		object_created.setVisited(tf_visit);
		list_of_objects.append(object_created);
	return list_of_objects;
	
#function to create the game manager
def createGameManager(tc, room):
	gm = ec.GameManager(tc, room);
	return gm;

def createGameManagerLoad(name, rooms):
	f = open(name, "r");
	rf = f.read();
	fj = json.loads(rf)[0];
	f.close()

	cr = fj['game_manager']['current_room']

	cr_o = getRoomFromName(rooms,cr);
	gm = ec.GameManager(int(fj['game_manager']['turn_count']), cr_o);
	
	return gm;
	
#function to create the player
def createPlayer(gm, items):
	p = ec.Player(items, gm);
	return p;

#function to create the player
def createPlayerLoad(gm, name):
	f = open(name, "r");
	rf = f.read();
	fj = json.loads(rf)[1];
	f.close()
	
	p = ec.Player(fj['player']['inventory'], gm);
	p.ears = fj['player']['ears']
	return p;
	
#function to save the game

def saveGame(gm, player, feat, rooms):
	name = raw_input("What would you like to call the save file?\n");
	data = []
	#Game manager data
	gm_data = {
		'game_manager': {
			'turn_count': str(gm.getTurnCount()),
			'current_room': gm.getCurrentRoom().getName(),
			}
		}
	data.append(gm_data);
	
	#Player data
	player_data = {
		'player': {
			'inventory': player.getInventory(),
			'ears': player.ears
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
		room_data['rooms'][r_a[i]]['name'] = rooms[i].getName()
		room_data['rooms'][r_a[i]]['descL'] = rooms[i].getLongDescription()
		room_data['rooms'][r_a[i]]['descS'] = rooms[i].getShortDescription()
		room_data['rooms'][r_a[i]]['items'] = rooms[i].getItems()
		room_data['rooms'][r_a[i]]['features'] = rooms[i].getFeatures()
		room_data['rooms'][r_a[i]]['visited'] = str(rooms[i].getVisited())
		room_data['rooms'][r_a[i]]['locked'] = str(rooms[i].getLocked())
		
		nr = rooms[i].getNorthRoom();
		sr = rooms[i].getSouthRoom();
		er = rooms[i].getEastRoom();
		wr = rooms[i].getWestRoom();
		
		if nr == None:
			nr = "";
		else:
			nr = nr.getName();
			
		if sr == None:
			sr = "";
		else:
			sr = sr.getName();
			
		if er == None:
			er = "";
		else:
			er = er.getName();
			
		if wr == None:
			wr = "";
		else:
			wr = wr.getName();
		
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
	
		feature_data['feature'][str(i)]['name'] = feat[i].getName();
		feature_data['feature'][str(i)]['desc'] = feat[i].getDescription();
		feature_data['feature'][str(i)]['descMod'] = feat[i].getModifiedDescription();
		feature_data['feature'][str(i)]['usage'] = feat[i].getUsage();
		feature_data['feature'][str(i)]['descModBool'] = m_b;
	
	data.append(feature_data);
	
	name = name + '.json'
	with open(name, 'w') as outfile:
		json.dump(data, outfile)
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
		print(returned_tag);#DEBUG PRINT
	
	#Set up the needed variables
	cr = player.getCurrentRoom();
	
	#set up the items list
	all_items_look = [];
	all_items_drop = [];
	all_items_take = [];
	features_touch = [];
	features_look = [];
	all_items_use = [];

	items_in_room = cr.getItems()[:];
	items_to_take = cr.getItems()[:];
	features_in_room = cr.getFeatures()[:];
	items_in_inventory = player.getInventory()[:];
	all_items = items_in_room[:];
	
	for y in features_in_room:
		features_look.append("look at " + y);

	for i in items_in_inventory:
		all_items.append(i);
		all_items_drop.append("drop " + i);
		all_items_use.append("use " + i);
	
	for j in all_items:
		all_items_look.append("look at " + j);
	
	for k in items_to_take:
		all_items_take.append("take " + k);
	
	for n in features_in_room:
		features_touch.append("touch " + n);

	#Create ambiguous commands list
	ww = "What would you like to ";
	amb_comm = ["look at?", "drop?", "take?", "move?", "hit?", "touch?", "use?"]
	all_amb = [];
	for a in amb_comm:
		all_amb.append(ww+a);
		#print(ww+a)#DEBUG PRINT
	all_amb.append("Where would you like to move?");

	#Set up the variables that will execute certain functions
	direction = ["go north", "go south", "go east", "go west"];
	amb = all_amb[:];
	look_at_item = all_items_look;
	look_at_feature = features_look; #features_in_room;
	help_display = "help";
	player_inventory = "show inventory";
	take_item = all_items_take; #FIX BASED ON TAG
	drop_item = all_items_drop; #FIX BASED ON TAG
	use_item = all_items_use; #FIX BASED ON TAG
	hit_target = ""; #FIX BASED ON TAG
	touch_target = ""; #FIX BASED ON TAG
	touch_feature = features_touch;	
	save_game = "save game"
	load_game = "load game"
		
	#use and touch both return touch

	#Process the tag based on what is returned, includes the verbs used in the game
	#Display the description if the returned tag is look at room but otherwise handle the ambiguous input
	if returned_tag in amb:
		print(returned_tag);
		returned_tag = getInput();
		#print(returned_tag) #DEBUG PRINT
		while(returned_tag == nu):
			returned_tag = getInput();
			#print(returned_tag);#DEBUG PRINT
		
		if returned_tag == "quit":
			print("Exiting game.")
			exit()			

		if returned_tag == "look at room":
			print(cr.getName() + ": " + cr.displayDescription());
			nsew_rooms = [cr.getNorthRoom(), cr.getSouthRoom(), cr.getEastRoom(), cr.getWestRoom()];
			
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
			for f in features_in_room:
				ret = getFeatureFromName(fea, f);
				print(ret.getName() + ": " + ret.displayDescription());
			if len(items_in_room) != 0:
				print("\nItems in room:");
				for i in items_in_room:
					print(i);
				print("");
			else:
				print("\nThere are no items in this room to be picked up\n.");	
			return 0;

	if returned_tag == "quit":
		print("Exiting game.")
		exit()			

	
	#Move Room if the returned Tag is a direction
	if returned_tag in direction:
		#crossing the river
		if cr.getName() == "Nile River" and returned_tag == "go north":
			if player.ears != "plugged":
				print("You attempt to cross the river and the siren's song keeps you from concentrating as you stumble and begin to drown.")
				print("You manage to cross the river but you have to take many deep breaths using up what precious little air you have left.\n")

		m = player.moveRoom(returned_tag);
		if m == 1: #If there is no room
			return 0; #return no turn taken up
		else:
			print("");
			print(player.getCurrentRoom().displayDescription());
			print("");
			player.getCurrentRoom().setVisited(True);
			return 1; #return turn taken up
	
	#Look at room
	elif returned_tag == "look at room":
		print(cr.getName() + ": " + cr.displayDescription());
		nsew_rooms = [cr.getNorthRoom(), cr.getSouthRoom(), cr.getEastRoom(), cr.getWestRoom()];
		
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
		for f in features_in_room:
			ret = getFeatureFromName(fea, f);
			print(ret.getName() + ": " + ret.displayDescription());
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
		#Search through the items list and then compare the name to the returned tag
		for its in look_at_item:
			if returned_tag == its: #Everything after "Look at"
				ret = getItemFromName(ite, its[8:]);
				print(ret.displayDescription());
				print("");
				break;
		return 0;
	
	#Display description for feature
	elif returned_tag in look_at_feature: 
		#Search through the items list and then compare the name to the returned tag
		for f in look_at_feature:
			if returned_tag == f and returned_tag == "look at sphinx" and cr.getName() == "Sphinx's Room":
				ret = getFeatureFromName(fea, f[8:]);
				print(ret.displayDescription());
				print("")

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
						f = getFeatureFromName(fea, "sphinx");
						f.modified_description_bool = True;
					else:
						print("You hear the sphinx chortle a little. It seems you were incorrect.\n")
						return 0;
				else:
					print("You hear the sphinx chortle a little.\n")
					return 0;

			if returned_tag == f and returned_tag == "look at adventurer" and cr.getName() == "Guard's Room" and getFeatureFromName(fea, "adventurer").modified_description_bool == False:
				print(getFeatureFromName(fea, "adventurer").displayDescription())
				print("You decide to take the earplugs.\n");
				getFeatureFromName(fea, "adventurer").modified_description_bool = True;
				i = getItemFromName(ite, "earplugs");
				print(i.getName() + ":" + i.description)
				print("Added earplugs to your inventory.\n")
				player.inventory.append("earplugs");

			if returned_tag == f:
				ret = getFeatureFromName(fea, f[8:]);
				print(ret.displayDescription());
				print("")
				break;
		return 0;
	
	#Display help function
	elif returned_tag == help_display:
		print("Verbs that can be used:") 
		verbs = ["help", "look at", "inventory", "quit", "save game", "load game", "use", "touch", "hit", "take", "drop", "move", "go"]
		for i in verbs:
			print(i);
		print("");
		return 0;
		
	#Display inventory
	elif returned_tag == player_inventory:
		if len(player.getInventory()) != 0:
			print("In inventory:");
			for i in player.getInventory():
				print(i);
			print("");
		else:
			print("No Items in inventory\n");
		return 0;
		
	elif returned_tag in drop_item:
		for its in drop_item:
			#TORCH DROPPING FOR ROOM 3
			if returned_tag == its and returned_tag == "drop torch" and cr.getName() == "Antechamber 1":
				ret = getItemFromName(ite, its[5:]);
				print("Dropped " + ret.getName() + " on the ground.\n");
				player.removeFromInventory(ret.getName());
				print("When the torch hits the ground you notice on the wall the holes repeat the pattern: up, down, down, up.\n");
				break;
				
			########################URN DROPPING HERE
			if returned_tag == its and returned_tag == "drop urn" and cr.getName() == "Pharaoh Mummy Room":
				#Not sure if urn is in its[5] or where the urn is in that list
				ret = getItemFromName(ite, its[5:]);
				print("Dropped " + ret.getName() + " on the ground.\n");
				player.removeFromInventory(ret.getName());
				cr.items.remove("urn")
				print("Upon dropping the urn, it lands on the ground and breaks open revealing a shiny brooch. You decide to pick it up and add it to your inventory.\n");
				cr.items.append("brooch")
				player.addToInventory("brooch")
				break;
			
			
			########################################################

			#EVERYTHING ELSE 
			elif returned_tag == its: #Everything after "Look "
				ret = getItemFromName(ite, its[5:]);
				print("Dropped " + ret.getName() + " on the ground.\n");
				player.removeFromInventory(ret.getName());
				break;
		return 0;
			
	elif returned_tag in take_item: 
		#Search through the items list and then compare the name to the returned tag
		for its in take_item:
			#specific thing for taking item
			if returned_tag == its and returned_tag == "take brooch" and cr.getName() == "Chamber of Passing":
				f = getFeatureFromName(fea, "chimera");
				f.modified_description_bool = True;

			if returned_tag == its and returned_tag == "take necklace" and cr.getName() == "Chamber of Passing":
				f = getFeatureFromName(fea, "jackal");
				f.modified_description_bool = True;

			if returned_tag == its and returned_tag == "take ancient artifact" and cr.getName() == "Burial Chamber":
				f = getFeatureFromName(fea, "large tomb");
				f.modified_description_bool = True;

			if returned_tag == its: #Everything after "Look "
				ret = getItemFromName(ite, its[5:]);
				print(ret.getName() + ": " + ret.displayDescription());
				print("Added " + ret.getName() + " to inventory.\n");
				player.addToInventory(ret.getName());
				break;
		return 0;

	elif returned_tag in touch_feature:
		for f in touch_feature: #see if there is a way to get something from a list in python
			if returned_tag == f:
				ret = getFeatureFromName(fea, f[6:]);
				turn_x = ret.touchFeature(player);
				return turn_x;
	
	elif returned_tag in use_item:
		for its in use_item:
			#This is the code to copy
			if returned_tag == its and returned_tag == "use earplugs":
				if cr.getName() == "Nile River":
					print("You can no longer hear the Siren's Song. You feel more confident crossing the River.\n")
				else:
					print("You place the earplugs in your ears. They help to deafen the sounds of the tomb.\n")
				player.ears = "plugged"
				return 1;

			if returned_tag == its and returned_tag == "use torch" and cr.getName() == "Chamber of Passing":
				d = "You see writings all across the north wall. On the east wall is a staircase that leads down and on the west wall are a jackal and chimera statue facing the staircase."
				if cr.short_description != d:
					print("You light up your torch and next to you is a brazier to light and when you do so you can now see the room.\n");
					cr.shortdescription = d;
					return 1;
				else:
					print("You tried to use the torch and nothing happens.\n");

			###################################HERE IS WHERE ANY ADDITIONAL USE CODE FOR ITEMS GOES
			#YOU CAN USE THE ABOVE CODE AS A GUIDE
	



			####################################################################################

			if returned_tag == its:
				ret = getItemFromName(ite, its[4:]);
				print("You tried to use the " + ret.getName() + " and nothing happens.\n");
				return 0;	

	elif returned_tag == save_game:
		saveGame(player.getGameManager(), player, fea, rooms);
		return 0;
	
	elif returned_tag == load_game:
		return -1;
	#...
	#...
	
	
	print("You cannot do that\n");
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
		
		#Create game manager
		gameManager = createGameManager(90,rooms[0]);
		
		#Create player
		starting_inventory = ["torch", "key"]; ###############CHANGE HERE BEFORE FINALIZING
		player = createPlayer(gameManager, starting_inventory);
		player.setCurrentRoom(gameManager.getCurrentRoom());
		
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
		
		#DO THINGS WITH LOADING
		#Begin creating game
		
		#Create items for the whole game
		items = createItem(ITEM_FILES_VAR);
		
		#Create items for the whole game
		features = createFeatureLoad(name);
		
		#Create rooms for the whole game
		rooms = createRoomLoad(name);
		createRoomNSEW(rooms);
		
		#Create game manager
		gameManager = createGameManagerLoad(name, rooms);
		
		#Create player
		player = createPlayerLoad(gameManager, name);
		player.setCurrentRoom(gameManager.getCurrentRoom());

	else:
		print("DEBUG - SOMETHING WENT WRONG IN THE MAIN MENU, THIS SHOULD NOT HAPPEN");
	
	#Begin Game
	#While the turn count is > 0
	turns_left = gameManager.getTurnCount();
	cr = player.getCurrentRoom();
	print("");
	print(cr.displayDescription());
	print("");
	cr.setVisited(True);	
	
	while turns_left > 0:
		turn = 0;
	
		#Display description
		cr = player.getCurrentRoom();
		#print(cr.displayDescription());
		
		#Get input and resolve actions
		input_given = getInput();
		#print(input_given);#DEBUG PRINT

		#Display result / if error then do not print result
		turn = processTag(input_given, player, items, features, rooms);
		if turn == -1:
			print("Entered load game")
			return -1;
		
		#Reduce turn count
		gameManager.setTurnCount(turns_left-turn);
		turns_left = gameManager.getTurnCount();

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
