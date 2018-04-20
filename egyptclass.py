#This is a file containing the classes and functions for the game

#This is the item class in the game
class Item:
	id = -1; #id of object in game
	name = ""; #name of item
	description = ""; #description of item
	type = ""; #Type of item, eventually change to having a lookup table, ex: 1 = Light, 2 = Weapon
	usage = []; #The features that items can interact with
	
	def getId(self):
		return self.id;
	
	def setId(self, id_value):
		self.id = id_value;
		return 0;
	
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
		
	def getUsage(self):
		return self.usage;
		
	def setUsage(self, usage_value):
		self.usage = usage_value;
		return 0;
		
	def getType(self):
		return self.type;
		
	def setType(self, type_value):
		self.type = type_value;
		return 0;
		
	#Interaction Functions
	
	def __init__(self, iden, na, desc, ty):
		self.setId(iden);
		self.setName(na);
		self.setType(ty);
		self.setDescription(desc);

#This is the feature class in the game
class Feature:
	id = -1; #id of feature throughout the game
	name = ""; #name of the feature
	description = ""; #description of the feature
	modified_description = ""; #description to of the feature when modified
	type = ""; #Type of feature ex: statue, door
	room_location = None; #the room that the feature is in
	usage = []; #the types of items tha can interact with it ex: weapon, key
	
	def getId(self):
		return self.id;
	
	def setId(self, id_value):
		self.id = id_value;
		return 0;
	
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
		
	def getType(self):
		return self.type;
		
	def setType(self, type_value):
		self.type = type_value;
		return 0;
		
	def getRoomLocation(self):
		return self.room_location;
		
	def setRoomLocation(self, room_location_value):
		self.room_location = room_location_value;
		return 0;

	#interaction functions
	
	def __init__(self, iden, na, desc, md, ty):
		self.setId(iden);
		self.setDescription(desc);
		self.setName(na);
		self.setModifiedDescription(md);
		self.setType(ty);

#This is the Room class in the game, it is the basis of the game, fix to match the rest of the classes with set/get functions
class Room:
	id = -1; # id for the room based on all things in the game, unique
	long_description = ""; # Long description for when entering the room for the first time
	short_description = ""; # Short Description for when entering the room every subsequent time
	modified_description = short_description; # Modified description based on actions
	additional_descriptions = []; # A list of additional descriptions based on what needs to be added
	modified_description_bool = False; # Tells whether or not to use the modified description
	items = []; # List of item objects in the room
	features = []; # List of feature objects in the room
	visited = False; # Boolean to determine if the room has been visited
	north_room = None; # room to the north of this room, none if there is not one
	south_room = None; # room to the south of this room, none if there is not one
	east_room = None; # room to the east of this room, none if there is not one
	west_room = None; # room to the west of this room, none if there is not one
	
	#Function that returns the id of the room
	def getId(self):
		return self.id;
		
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
	def __init__(self, iden, na, ld, sd, ad, it, fe):
		self.id = iden; #change all these to set functions and finish adding set functions to rooms
		self.setName(na);
		self.long_description = ld;
		self.short_description = sd;
		self.modified_description = sd;
		self.additional_descriptions = ad;
		self.modified_description_bool = False;
		self.items = it;
		self.features = fe;
		self.visited = False;

#This is the game manager class in the game
class GameManager:
	id = -1; #id of game manager
	turn_count = -1; # turn count remaining
	current_room = None; # current room the game is in
	room_to_north = None; # the room to the north of the current room, none if there is not one
	room_to_south = None; # the room to the south of the current room, none if there is not one
	room_to_east = None; # the room to the east of the current room, none if there is not one
	room_to_west = None;# the room to the west of the current room, none if there is not one
	
	def getId(self):
		return self.id;
	
	def setId(self, id_value):
		self.id = id_value;
		return 0;
		
	def getCurrentRoom(self):
		return self.current_room;
	
	def setCurrentRoom(self, current_room_value):
		self.current_room = current_room_value;
		return 0;
		
	#Function that returns the north room object or none if there isn't one
	def getNorthRoom(self):
		return self.room_to_north;	
	
	#Function that sets the room to the north and returns 0
	def setNorthRoom(self, north_room_value):
		self.room_to_north = north_room_value
		return 0;

	#Function that returns the south room object or none if there isn't one
	def getSouthRoom(self):
		return self.room_to_south;	
	
	#Function that sets the room to the south and returns 0
	def setSouthRoom(self, south_room_value):
		self.room_to_south = south_room_value
		return 0;	

	#Function that returns the east room object or none if there isn't one	
	def getEastRoom(self):
		return self.room_to_east;	
	
	#Function that sets the room to the east and returns 0
	def setEastRoom(self, east_room_value):
		self.room_to_east = east_room_value
		return 0;	

	#Function that returns the west room object or none if there isn't one	
	def getWestRoom(self):
		return self.room_to_west;	
	
	#Function that sets the room to the west and returns 0
	def setWestRoom(self, west_room_value):
		self.room_to_west = west_room_value
		return 0;			
	
	#Function to set all the rooms at once based on the current room
	def setNSEWRoomsGM(self, cr):
		self.setNorthRoom(cr.getNorthRoom());
		self.setSouthRoom(cr.getSouthRoom());
		self.setEastRoom(cr.getEastRoom());
		self.setWestRoom(cr.getWestRoom());
	
	def __init__(self, iden, tc, cr):
		self.id = iden;
		self.turn_count = tc;
		self.current_room = cr;
		
#This is the player class in the game
class Player:
	id = -1;
	current_room = None;
	inventory = [];
	game_manager = None;

	def getId(self):
		return self.id;
	
	def setId(self, id_value):
		self.id = id_value;
		return 0;
		
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
			if item_to_remove.getId() == it.getId():
				self.getInventory().remove(it);
				self.getCurrentRoom().addItemToRoom(it);
				return 0;
		return 1;
		
	def removeFromInventory(self, item_to_remove):
		inven = self.getInventory();
		for it in inven:
			if item_to_remove.getId() == it.getId():
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
	def moveRoom(self, room_to_move_to):
		self.setCurrentRoom(room_to_move_to);
		cr = self.getCurrentRoom()
		print(cr.displayDescription());
		cr.setVisited(True);
		gm = self.getGameManager()
		gm.setCurrentRoom(room_to_move_to)
		gm.setNSEWRoomsGM(room_to_move_to); #gets the gameManager, sets its room to the room to move to, then sets the rooms NSEW based on the room
		return 0;
	
	def __init__(self, iden, inven, gm):
		self.setId(iden);
		self.setInventory(inven);
		self.setGameManager(gm);
