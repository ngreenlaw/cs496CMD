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
		print("I am not sure what you mean. Please try again.");
		return 2;

def intro():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print('          _____ _   _______  _____ ___________   _____ ________  _________  ');
    print('         /  __ \ | | | ___ \/  ___|  ___|  _  \ |_   _|  _  |  \/  || ___ \ ');
    print('         | /  \/ | | | |_/ /\ `--.| |__ | | | |   | | | | | | .  . || |_/ / ');
    print('         | |   | | | |    /  `--. \  __|| | | |   | | | | | | |\/| || ___ \ ');
    print('         | \__/\ |_| | |\ \ /\__/ / |___| |/ /    | | \ \_/ / |  | || |_/ / ');
    print('          \____/\___/\_| \_|\____/\____/|___/     \_/  \___/\_|  |_/\____/  \n');
                
    print("     Egypt 1926, Valley of the kings - Archeologist Charles Carter is on the verge of discovering the tomb of the great sorcerer to Rameses II. On opening the tomb, Charles ventures in alone, not sure of what dangers lie ahead. As soon as he steps foot into the first chamber a pressure lever is triggered sliding a giant stone wheel in front of the opening. \n");
          
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
	
	nu = "I didn\'t understand. You can try rephrasing.";

	while(returned_tag == nu):
		returned_tag = getInput();
		print(returned_tag);
	#Set up the needed variables
	cr = player.getCurrentRoom();
	
	#set up the items list
	all_items_look = [];
	all_items_drop = [];
	all_items_take = [];
	features_touch = [];

	items_in_room = cr.getItems()[:];
	items_to_take = cr.getItems()[:];
	features_in_room = cr.getFeatures()[:];
	items_in_inventory = player.getInventory()[:];
	all_items = items_in_room[:];

	print(cr.getItems());
	
	for i in items_in_inventory:
		all_items.append(i);
		all_items_drop.append("drop " + i);
	
	for j in all_items:
		all_items_look.append("look at " + j);
	
	for k in items_to_take:
		all_items_take.append("take " + k);
	
	for n in features_in_room:
		features_touch.append("touch " + n);

	#Set up the variables that will execute certain functions
	direction = ["go north", "go south", "go east", "go west"];
	look = "look";
	look_at_item = all_items_look;
	look_at_feature = "look at room" #features_in_room;
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
	
	#Move Room if the returned Tag is a direction
	if returned_tag in direction:
		m = player.moveRoom(returned_tag);
		if m == 1: #If there is no room
			return 0; #return no turn taken up
		else:
			return 1; #return turn taken up
		
	#Display the description if the returned tag is look
	elif returned_tag == look:
		cr.displayDescription();
		return 0;
		
	#Display the description if the returned tag is look item
	#returned_tag == look <item> ex: look torch
	elif returned_tag in look_at_item: 
		#Search through the items list and then compare the name to the returned tag
		for its in look_at_item:
			if returned_tag == its: #Everything after "Look "
				ret = getItemFromName(ite, its[8:]);
				print(ret.displayDescription());
				break;
		return 0;
	
	#Display description for feature
	elif returned_tag in look_at_feature: 
		#Search through the items list and then compare the name to the returned tag
		for f in features_in_room:
			ret = f.getFeatureFromName(f, fea);
			ret.displayDescription();
			break;
		return 0;
	
	#Display help function
	elif returned_tag == help_display:
		print("VERBS THAT CAN BE USED") ################################FIX HERE
		return 0;
		
	#Display inventory
	elif returned_tag == player_inventory:
		print("In inventory:");
		for i in player.getInventory():
			print(i);
		return 0;
		
	elif returned_tag in drop_item:
		for its in drop_item:
			if returned_tag == its: #Everything after "Look "
				ret = getItemFromName(ite, its[5:]);
				print("Dropped " + ret.getName() + " on the ground.");
				player.removeFromInventory(ret.getName());
				break;
		return 0;
			
	elif returned_tag in take_item: 
		#Search through the items list and then compare the name to the returned tag
		for its in take_item:
			if returned_tag == its: #Everything after "Look "
				ret = getItemFromName(ite, its[5:]);
				ret.displayDescription();
				print("Added " + ret.getName() + " to inventory.");
				player.addToInventory(ret.getName());
				break;
		return 0;

	elif returned_tag in touch_feature:
		for f in touch_feature:
			if returned_tag == f:
				ret = getFeatureFromName(fea, f[6:]);
				ret.touchFeature();
				return 1;
	#...
	#...
	#...
	
	
	print("You cannot do that");
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
		print("Loading Game");

    else:
		print("DEBUG - SOMETHING WENT WRONG IN THE MAIN MENU, THIS SHOULD NOT HAPPEN");
	
	#Begin Game
	#While the turn count is > 0
    turns_left = gameManager.getTurnCount();
    while turns_left > 0:
		turn = 0;
	
		#Display description
		cr = player.getCurrentRoom();
		print(cr.displayDescription());
		
		#Get input and resolve actions
		input_given = getInput();
		print(input_given);
		#Display result / if error then do not print result
		turn = processTag(input_given, player, items, features);
		
		#Reduce turn count
		if turn == 1:
			gameManager.setTurnCount(turns_left-1);
			turns_left = gameManager.getTurnCount();
		
#run the program
if __name__ == "__main__":
	main();
