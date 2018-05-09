#This is the main file for running the game
from __future__ import print_function
import json
import watson_developer_cloud
import sys
import egyptclass as ec

#Variables to hold things such that they are easier to edit
ITEM_FILES_VAR = ["items.json"]; #would like to change this to reading off of a file that contains the names of all the files
FEATURE_FILES_VAR = ["features.json"];
ROOM_FILES_VAR = ["room1.txt", "room2.txt"];
GAME_MANAGER_FILE_VAR = "gm.txt";
PLAYER_FILE_VAR = "player.txt";

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

#these functions get the object from the name, returns 1 if there is an error
def getItemFromName(list, item):
	for i in range(0, len(list)):
		if item == i.name:
			return i;
	return 1;
	
def getFeatureFromName(list, feature):
	for i in range(0, len(list)):
		if feature == i.name:
			return i;
	return 1;
	
def getRoomFromName(list, room):
	for i in range(0, len(list)):
		if i != None:
			if item == i.room:
				return i;
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
		
		#create the object HERE IS WHERE TO EDIT
		object_created = ec.Room(fj['name'], fj['descL'], fj['descS'], fj['descAdd'], fj['items'], fj['features'], fj['locked']);
		object_created.setNorthRoom(fj['north_room']);
		object_created.setSouthRoom(fj['south_room']);
		object_created.setEastRoom(fj['east_room']);
		object_created.setWestRoom(fj['west_room']);
		list_of_objects.append(object_created);
		
	return list_of_objects;
	
#function to create the game manager
def createGameManager(tc, oom, pr):
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
        response = = assistant.message(
                                     workspace_id='6e437ce3-3817-47ba-971c-c39142841f73',
                                     input={
                                     'text': text
                                     }
                                     )
        data = json.dumps(response)
        return(", ".join(DictQuery(response).get('output/text')))     

#functions to resolve the action and update necessary variables
#Returns if a turn should be used up is 1, 0 if not
def processTag(returned_tag, player):
	#Set up the needed variables
	cr = player.getCurrentRoom();
	
	#set up the items list
	items_in_room = cr.getItems();
	features_in_room = cr.getFeatures();
	items_in_inventory = player.getInventory();
	all_items = items_in_room;
	for i in items_in_inventory:
		all_items.append(i);
		
	
	#Set up the variables that will execute certain functions
	direction = ["north", "south", "east", "west"];
	look = "look";
	look_at_item = all_items;
	look_at_feature = features_in_room;
	help = "help";
	player_inventory = "inventory";
	run = "run";
	listen = "listen"
	fight_target = "" #FIX BASED ON TAG
	take_item = items_in_room; #FIX BASED ON TAG
	throw_item_at_target = ""; #FIX BASED ON TAG
	drop_item = ""; #FIX BASED ON TAG
	smell_target = ""; #FIX BASED ON TAG
	use_item_on_target = ""; #FIX BASED ON TAG
	hit_target_with_item = ""; #FIX BASED ON TAG
	touch_target = ""; #FIX BASED ON TAG
	
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
	elif returned_tag[5:] in look_at_item: 
		#Search through the items list and then compare the name to the returned tag
		for its in look_at_item:
			if returned_tag[5:] == its: #Everything after "Look "
				ret = its.getItemFromName();
				ret.displayDescription();
				break;
		return 0;
	
	#Display description for feature
	elif returned_tag[5:] in look_at_feature: 
		#Search through the items list and then compare the name to the returned tag
		for fea in features_in_room:
			if returned_tag[5:] == fea: #Everything after "Look "
				ret = fea.getItemFromName();
				ret.displayDescription();
				break;
		return 0;
	
	#Display help function
	elif returned_tag == help:
		print("VERBS THAT CAN BE USED") ################################FIX HERE
		return 0;
		
	#Display inventory
	elif returned_tag == player_inventory:
		print(player.getInventory);
		return 0;
		
	elif returned_tag == run:
		pr = player.getGameManager().getPreviousRoom()
		if pr != cr:
			m = player.moveRoom(pr.getName());
			return 1;
		else: #Handles the case where run is input at the beginning of the game
			print("You cannot go to the previous room");
			return 0;
			
	elif returned_tag == listen:
		cr.displayDescription() #Change to display listening description, i.e. write the listening
		return 0;
	
	elif returned_tag == fight_target:
		#Fight function
		return 1;
		
	elif returned_tag[5:] in take_item: 
		#Search through the items list and then compare the name to the returned tag
		for its in take_item:
			if returned_tag[5:] == its: #Everything after "Look "
				ret = its.getItemFromName();
				ret.displayDescription();
				print("Added " + its + " to inventory.");
				player.addToInventory(its);
				break;
		return 0;
	#...
	#...
	#...
	
	else:
		print("You cannot do that");
def main():
	
	#Start Main Menu, until a result of save, load or exit is given, repeat asking for input
	get_main_menu_result = 2;
	while get_main_menu_result == 2:
		get_main_menu_result = mainMenu();
		
	#Process command from main menu
	#new game issued	
	if get_main_menu_result == 0:
		#Begin creating game
		
		#Create items for the whole game
		items = createItem(global ITEM_FILES_VAR);
		
		#Create items for the whole game
		features = createFeature(global FEATURE_FILES_VAR);
		
		#Create rooms for the whole game
		rooms = createRoom(global ROOM_FILES_VAR);
		createRoomNSEW(rooms);
		
		#Create game manager
		gameManager = createGameManager(90,rooms[0], rooms[0]);
		
		#Create player
		starting_inventory = ["Torch"];
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
		cr.displayDescription();
		
		#Get input and resolve actions
		input_given = getInput();
		
		#Display result / if error then do not print result
		turn = processTag(input_given, player);
		
		#Reduce turn count
		if turn == 1:
			gameManager.setTurnCount(turns_left-1);
			turns_left = gameManager.getTurnCount();
		
#run the program
if __name__ == "__main__":
	main();
