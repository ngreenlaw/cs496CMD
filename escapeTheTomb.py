#This is the main file for running the game
from __future__ import print_function
import json
from watson_developer_cloud import ConversationV1
import sys
import egyptclass as ec

#Variables to hold things such that they are easier to edit
ITEM_FILES_VAR = ["item1.txt", "item2.txt"]; #would like to change this to reading off of a file that contains the names of all the files
FEATURE_FILES_VAR = ["feature1.txt", "feature2.txt"];
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

#----------------------------------------CREATE GET ITEM/FEATURE/ROOM FROM NAME FUNCTIONS AND UPDATE THE OTEHR FUNCTIONS
		
#function to create the items
def createItem(files_list):
	#FIX BASED ON WHAT THE JSON FILE IS
	object_created = None;
	list_of_objects = [];
	#read the files
	for fi in files_list:
		f = open(fi, "r");
		rf = f.read();
		fj = json.loads(s);
		
		#create the object HERE IS WHERE TO EDIT
		object_created = ec.Item(fj['name'], fj['desc']);
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
		fj = json.loads(s);
		
		#create the object HERE IS WHERE TO EDIT
		object_created = ec.Feature(fj['name'], fj['desc'], fj['descMod'], fj['usage']);
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
		fj = json.loads(s);
		
		#create the object HERE IS WHERE TO EDIT
		object_created = ec.Room(fj['name'], fj['descL'], fj['descS'], fj['descAdd'], fj['items'], fj['features'], fj['locked']);
		object_created.setNorthRoom(fj['north_room']);
		object_created.setSouthRoom(fj['south_room']);
		object_created.setEastRoom(fj['east_room']);
		object_created.setWestRoom(fj['west_room']);
		list_of_objects.append(object_created);
		
	return list_of_objects;
	
#function to create the game manager
def createGameManager(room):
	f = open(GAME_MANAGER_FILE_VAR, "r");
	rf = f.read();
	fj = json.loads(s);
	gm = ec.GameManager(fj['turnCount'], room);
	return gm;

#function to create the player
def createPlayer(gm, items):
	f = open(PLAYER_FILE_VAR, "r");
	rf = f.read();
	fj = json.loads(s);
	gm = ec.Player(items, gm);
	return gm;

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

conversation = ConversationV1(
    username='57db025b-2f83-45b6-90e9-4890d0d3e616',
    password='COcz1TPoSKQD',
    version='2018-04-25')
workspace_id = '2c730ca5-72d1-44d0-a1d9-a12327957f18'

def getInput():
	#FILL IN THE FUNCTIONS WITH THE NATURAL LANGUAGE PARSER OR IMPORT THE MODULE
	#RETURNS THE TAG TO BE PROCESSED
    text = ''
    response = ''
    while text != 'quit':
        text = raw_input('>> ')
        response = conversation.message(
                                    workspace_id=workspace_id, input={
                                    'text': text
                                    })
        data = json.dumps(response)
        return(", ".join(DictQuery(response).get('output/text')))    

#functions to resolve the action and update necessary variables
def processTag(returned_tag, player):
	#Set up the needed variables
	'''cr = player.getCurrentRoom();
	
	#set up the items list
	items_in_room = cr.getItems();
	items_in_inventory = player.getInventory();
	for i in items_in_inventory:
		items_in_room.append(i);
	all_items = [];
	for it in items_in_room:
		all_items.append("look " + it.getName());
	'''
	#Set up the variables that will execute certain functions
	direction = ["north", "south", "east", "west"];
	look = "look";
	'''look_at_item = all_items;'''
	
	
	#Process the tag based on what is returned, includes the verbs used in the game
	
	#Move Room if the returned Tag is a direction
	if returned_tag in direction:
		#player.moveRoom(returned_tag);
		print("Move Room "+ returned_tag);
		exit();
	#Display the description if the returned tag is look
	'''elif returned_tag == look:
		cr.displayDescription();
		
	#Display the description if the returned tag is look item
	elif returned_tag in look_at_item: 
		#Search through the items list and then compare the name to the returned tag
		for its in items_in_room:
			if returned_tag[5:] == its.getName(): #Everything after "Look "
				its.displayDescription();
	
	#elif returned_tag == 
	#...
	#...
	#...
	
	else:
		print("You cannot do that");'''
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
		items = createItem(ITEM_FILES_VAR);
		
		#Create features for the whole game
		features = createFeature(FEATURE_FILES_VAR);
		
		#Create rooms for the whole game
		rooms = createRoom(ROOM_FILES_VAR);
		createRoomNSEW(rooms);
		
		#Create game manager
		gameManager = createGameManager(rooms[0]);
		
		#Create player
		starting_inventory = ["Torch"];
		player = createPlayer(gameManager, starting_inventory); 
		
	#Load game	
	elif get_main_menu_result == 1:
		#BEGIN GAME LOADING
		print("Loading Game");
		#TESTING THE PARSER, WILL REMOVE
		player = ec.Player(90,None);
		input_given = getInput();
		processTag(input_given,player);
                
	else:
		print("DEBUG - SOMETHING WENT WRONG IN THE MAIN MENU, THIS SHOULD NOT HAPPEN");
	
	#Begin Game
	#While the turn count is > 0
	turns_left = gameManager.getTurnCount();
	while turns_left > 0:
		#Display description
		cr = player.getCurrentRoom();
		cr.displayDescription();
		
		#Get input and resolve actions
		input_given = getInput();
		
		#Display result / if error then do not print result
		processTag(input_given, player);
		
		#Reduce turn count
		gameManager.setTurnCount(turns_left-1);
		turns_left = gameManager.getTurnCount();
		
#run the program
if __name__ == "__main__":
	main();
