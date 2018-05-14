#This is the main file for running the game
from __future__ import print_function
import json
import watson_developer_cloud
import sys
import egyptclass as ec
import os
#import simplejson

#Variables to hold things such that they are easier to edit
ITEM_FILES_VAR = ["items.json"]; #would like to change this to reading off of a file that contains the names of all the files
FEATURE_FILES_VAR = ["features.json"];
ROOM_FILES_VAR = ["room1.json", "room2.json", "room3.json", "room4.json", "room5.json", "room6.json", "room7.json", "room8.json", "room9.json", "room10.json"];
#GAME_MANAGER_FILE_VAR = "gm.json";
#PLAYER_FILE_VAR = "player.json";

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
		
	#create the object HERE IS WHERE TO EDIT
	for f_feature in fj:
		object_created = ec.Feature(f_feature['name'], f_feature['desc'], f_feature['descMod'], f_feature['usage']);
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
	
#function to create the game manager
def createGameManager(tc, room, pr):
	gm = ec.GameManager(tc, room, pr);
	return gm;

#function to create the player
def createPlayer(gm, items):
	p = ec.Player(items, gm);
	return p;
	
#Separate load file that will take all of the saved data and read it in.

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
def processTag(returned_tag, player, ite, fea):
	
	#Check the I didnt understand result and ask to get input again
	nu = "I didn\'t understand. You can try rephrasing.";

	while(returned_tag == nu):
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
	use_item_on_target = ""; #FIX BASED ON TAG
	hit_target_with_item = ""; #FIX BASED ON TAG
	touch_target = ""; #FIX BASED ON TAG
	touch_feature = features_touch;	
		
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
	
	#Move Room if the returned Tag is a direction
	if returned_tag in direction:
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
			if returned_tag == f:
				ret = getFeatureFromName(fea, f[8:]);
				print(ret.displayDescription());
				print("")
				break;
		return 0;
	
	#Display help function
	elif returned_tag == help_display:
		print("VERBS THAT CAN BE USED") ################################FIX HERE
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
			if returned_tag == its: #Everything after "Look "
				ret = getItemFromName(ite, its[5:]);
				print(ret.getName() + ": " + ret.displayDescription());
				print("Added " + ret.getName() + " to inventory.\n");
				player.addToInventory(ret.getName());
				break;
		return 0;

	elif returned_tag in touch_feature:
		for f in touch_feature:
			if returned_tag == f:
				ret = getFeatureFromName(fea, f[6:]);
				ret.touchFeature(player);
				return 1;
	#...
	#...
	#...
	
	
	print("You cannot do that\n");
	return 0;

def main():
	# Display's intro
	intro()
	#Start Main Menu, until a result of save, load or exit is given, repeat asking for input
	get_main_menu_result = 2;
	while get_main_menu_result == 2:
		get_main_menu_result = mainMenu();
		
	#Process command from main menu
	#new game issued
	if get_main_menu_result == 0:
		#Begin creating game
		
		#Create items for the whole game
		global ITEM_FILES_VAR;
		items = createItem(ITEM_FILES_VAR);
		
		#Create items for the whole game
		global FEATURE_FILES_VAR;
		features = createFeature(FEATURE_FILES_VAR);
		
		#Create rooms for the whole game
		global ROOM_FILES_VAR
		rooms = createRoom(ROOM_FILES_VAR);
		createRoomNSEW(rooms);
		
		#Create game manager
		gameManager = createGameManager(90,rooms[0], rooms[0]);
		
		#Create player
		starting_inventory = ["torch"];
		player = createPlayer(gameManager, starting_inventory);
		player.setCurrentRoom(gameManager.getCurrentRoom());
		
	#Load game
	elif get_main_menu_result == 1:
		#BEGIN GAME LOADING
		print("Loading Game Doesnt work yet");
		exit();

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
		turn = processTag(input_given, player, items, features);
		
		#Reduce turn count
		gameManager.setTurnCount(turns_left-turn);
		turns_left = gameManager.getTurnCount();

	if turns_left <= 0:
		print("You have unfortunately ran out of air.");
		print("GAME OVER");
		
#run the program
if __name__ == "__main__":
	main();
