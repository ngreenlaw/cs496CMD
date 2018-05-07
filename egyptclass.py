#This is a file containing the classes and functions for the game

#This is the item class in the game
class Item:
	name = ""; #name of item
	description = ""; #description of item
	
	def getName(self):
		return self.name;
		
	def setName(self, name_value):
		self.name = name_value;
		return 0;
		
	#Function that returns the item description
	def getDescription(self):
		return self.description;
		
	def setDescription(self, desc_value):
		self.description = desc_value;
		return 0;
		
	def displayDescription(self):
		print(self.getDescription());
		return 0;
		
	#Interaction Functions
	def useItem(self, works, feature_tried):
		result = "You used the " + self.getName() + " on the " + feature_tried;
		if works == True:
			result = result + " and it worked!"
			print(result);
			return 0;
		else:
			result = result + " and nothing happened.";
			print(result);
			return 1;
			
	def __init__(self, na, desc):
		self.setName(na);
		self.setDescription(desc);

#This is the feature class in the game
class Feature:
	name = ""; #name of the feature
	description = ""; #description of the feature
	modified_description = ""; #description of the feature when modified
	modified_description_bool = False; # Tells whether or not to use the modified description
	usage = []; # The id of the item that can interact with it
	
	def getName(self):
		return self.name;
		
	def setName(self, name_value):
		self.name = name_value;
		return 0;
		
	def getCurrentRoom(self):
		return self.current_room;
	
	def setCurrentRoom(self, current_room_value):
		self.current_room = current_room_value;
		return 0;
		
	def getDescription(self):
		return self.description;
		
	def setDescription(self, desc_value):
		self.description = desc_value;
		return 0;

	def getModifiedDescription(self):
		return self.modified_description;
		
	def setModifiedDescription(self, desc_value):
		self.modified_description = desc_value;
		return 0;		
		
	def getUsage(self):
		return self.usage;
		
	def setUsage(self, usage_value):
		self.usage = usage_value;
		return 0;

	def displayDescription(self):
		if self.modified_description_bool == False:
			print(self.getDescription());
		else:
			print(self.getModifiedDescription());
		
	#interaction function, returns 0 if successful and 1 if not successful
	def interactWith(self, item_tried):
		able_to_use = False;
		item_tried_name = item_tried.getName();
		if item_tried_name in self.usage:
			able_to_use = True;
		result = item_tried.useItem(able_to_use, self.getName());
		if result == 0:
			print(self.getModifiedDescription());
			self.modified_description_bool = True;
			return 0;
		return 1;
		
	def __init__(self, na, desc, md):
		self.setDescription(desc);
		self.setName(na);
		self.setModifiedDescription(md);

#This is the Room class in the game, it is the basis of the game, fix to match the rest of the classes with set/get functions
class Room:
	long_description = ""; # Long description for when entering the room for the first time
	short_description = ""; # Short Description for when entering the room every subsequent time
	modified_description = short_description; # Modified description based on actions
	additional_descriptions = []; # A list of additional descriptions based on what needs to be added
	modified_description_bool = False; # Tells whether or not to use the modified description
	items = []; # List of item objects in the room, ids of the items
	features = []; # List of feature objects in the room, ids of the features
	visited = False; # Boolean to determine if the room has been visited
	locked = False; #Boolean to determine if the room is locked, needs a puzzle or key to open it
	north_room = None; # room to the north of this room, none if there is not one
	south_room = None; # room to the south of this room, none if there is not one
	east_room = None; # room to the east of this room, none if there is not one
	west_room = None; # room to the west of this room, none if there is not one
	
	def getName(self):
		return self.name;
		
	def setName(self, name_value):
		self.name = name_value;
		return 0;

	#Function that returns the long description of the room
	def getLongDescription(self):
		return self.long_description;
	
	#Function that returns the short description of the room
	def getShortDescription(self):
		return self.short_description;
	
	#Function that returns the modified description of the room
	def getModifiedDescription(self):
		return self.modified_description;
	
	#Function that updates the modified description based on the location in the list, returns nothing
	def updateDescription(self, additional_descriptions_number):
		self.modified_description = self.modified_description + " " + self.additional_descriptions[additional_descriptions_number];
		self.modified_description_bool = True;
		return 0;
	
	#Function that returns the list of items in the room
	def getItems(self):
		return self.items;
		
	#Function that adds an item to the room using its' id, returns nothing
	def addItemToRoom(self, item_to_add):
		self.items.append(item_to_add);
		return 0;
	
	#Function that removes an item from the room using its' id, returns 0 if fine or 1 if there is no item to remove
	def removeItemFromRoom(self, item_to_remove):
		if item_to_remove in self.items:
			self.items.remove(item_to_remove);
			return 0;
		else:
			return 1;
	
	#Function that returns the features of the room
	def getFeatures(self):
		return self.features;
		
	def setFeatures(self, feat):
		self.features = feat;
		return 0;
	
	#Function that removes a feature from the room using its' id, returns 0 if successful and 1 if there is no feature
	def removeFeature(self, feature_to_remove):
		if feature_to_remove in self.features:
			self.features.remove(feature_to_remove);
			return 0;
		else:
			return 1;
	
	#Function that returns the north room object or none if there isn't one
	def getNorthRoom(self):
		return self.north_room;	
	
	#Function that sets the room to the north and returns 0
	def setNorthRoom(self, north_room_value):
		self.north_room = north_room_value
		return 0;

	#Function that returns the south room object or none if there isn't one
	def getSouthRoom(self):
		return self.south_room;	
	
	#Function that sets the room to the south and returns 0
	def setSouthRoom(self, south_room_value):
		self.south_room = south_room_value
		return 0;	

	#Function that returns the east room object or none if there isn't one	
	def getEastRoom(self):
		return self.east_room;	
	
	#Function that sets the room to the east and returns 0
	def setEastRoom(self, east_room_value):
		self.east_room = east_room_value
		return 0;	

	#Function that returns the west room object or none if there isn't one	
	def getWestRoom(self):
		return self.west_room;	
	
	#Function that sets the room to the west and returns 0
	def setWestRoom(self, west_room_value):
		self.west_room = west_room_value
		return 0;			
	
	#Function to set all the rooms at once and returns 0
	def setNSEWRooms(self, nr, sr, er, wr):
		self.setNorthRoom(nr);
		self.setSouthRoom(sr);
		self.setEastRoom(er);
		self.setWestRoom(wr);
	
	#Function that returns the visited value
	def getVisited(self):
		return self.visited;
	
	#Function that sets the visited value to either True or False and returns 0
	def setVisited(self, visited_value):
		self.visited = visited_value;
		return 0;
		
	#Functions to get and set the locked variable
	def getLocked(self):
		return self.locked;
	
	def setLocked(self, locked_value):
		self.locked = locked_value;
		return 0;
		
	#Function to display the correct description, returns the string for the game to output
	def displayDescription(self):
		if self.getVisited() == False:
			return self.getLongDescription();
		else:
			if self.modified_description_bool == False:
				return self.getShortDescription();
			else:
				return self.getModifiedDescription();
	
	#Function to initialize a Room object, takes id, long desc, short desc, additional desc, items, and features 
	def __init__(self, na, ld, sd, ad, it, lk):
		self.setName(na);
		self.long_description = ld;
		self.short_description = sd;
		self.modified_description = sd;
		self.additional_descriptions = ad;
		self.modified_description_bool = False;
		self.items = it;
		self.features = fe;
		self.visited = False;
		self.setLocked(lk);

#This is the game manager class in the game
class GameManager:
	turn_count = -1; # turn count remaining
	current_room = None; # current room the game is in
	previous_room = None; # Previous room
		
	def getTurnCount(self):
		return self.turn_count;
		
	def setTurnCount(self, turn_count_value):
		self.turn_count = turn_count_value;
		return 0;
		
	def getCurrentRoom(self):
		return self.current_room;
	
	def setCurrentRoom(self, current_room_value):
		self.current_room = current_room_value;
		return 0;
		
	def getPreviousRoom(self):
		return self.current_room;
	
	def setPreviousRoom(self, current_room_value):
		self.current_room = current_room_value;
		return 0;
	
	def __init__(self, tc, cr, pr):
		self.turn_count = tc;
		self.current_room = cr;
		self.previous_room = pr;
		
#This is the player class in the game
class Player:
	current_room = None;
	inventory = [];
	game_manager = None;
		
	def getCurrentRoom(self):
		return self.current_room;
	
	def setCurrentRoom(self, current_room_value):
		self.current_room = current_room_value;
		return 0;
		
	def getGameManager(self):
		return self.game_manager;
		
	def setGameManager(self, game_manager_value):
		self.game_manager = game_manager_value;
		return 0;
		
	def getInventory(self):
		return self.inventory;
	
	def setInventory(self, inventory_value):
		self.inventory = inventory_value;
		return 0;
		
	def addToInventory(self, item_to_add):
		rItems = self.getCurrentRoom().getItems(); 
		for it in rItems:
			if item_to_add == it:
				self.getInventory().append(it);
				self.getCurrentRoom().removeItemFromRoom(it);
				return 0;
		return 1;
		
	def removeFromInventory(self, item_to_remove):
		inven = self.getInventory();
		for it in inven:
			if item_to_remove == it:
				self.getInventory().remove(it);
				self.getCurrentRoom().addItemToRoom(it);
				return 0;
		return 1;
		
	def useItemFromInventory(self, item_to_use):
		inven = self.getInventory();
		for it in inven:
			if item_to_use.getId() == it.getId():
				#Process item to use using features and items interaction functions
				return 0;
		return 1;	
		
	#This function handles moving rooms	
	def moveRoom(self, room_to_move_to_string):
		cr = self.getCurrentRoom()
		room_to_north = cr.getNorthRoom();
		room_to_south = cr.getSouthRoom();
		room_to_east = cr.getEastRoom();
		room_to_west = cr.getWestRoom();
		is_room = False;
		room_to_move_to = None;
		
		if room_to_move_to_string == "north":
			if room_to_north != None:
				is_room = True;
				room_to_move_to = room_to_north;
		
		if room_to_move_to_string == "south":
			if room_to_south != None:
				is_room = True;
				room_to_move_to = room_to_south;
		
		if room_to_move_to_string == "east":
			if room_to_east != None:
				is_room = True;
				room_to_move_to = room_to_east;		
		
		if room_to_move_to_string == "west":
			if room_to_west != None:
				is_room = True;
				room_to_move_to = room_to_west;		
		
		if is_room == True:
			gm = self.getGameManager();
			gm.setPreviousRoom(cr);
			self.setCurrentRoom(room_to_move_to);
			cr = self.getCurrentRoom()
			print(cr.displayDescription());
			cr.setVisited(True);
			gm.setCurrentRoom(room_to_move_to)
		
		else:
			print("There is no room in that direction");
			return 1; #Not able to move
		return 0; #Able to move
	
	def __init__(self, inven, gm):
		self.setInventory(inven);
		self.setGameManager(gm);
