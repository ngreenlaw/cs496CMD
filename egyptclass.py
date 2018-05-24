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
		return(self.getDescription());
		
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
			return(self.getDescription());
		else:
			return(self.getModifiedDescription());
		
	#interaction function, returns desc if successful and 0 if not successful
	def interactWith(self, item_tried):
		able_to_use = False;
		item_tried_name = item_tried.getName();
		if item_tried_name in self.usage:
			able_to_use = True;
		result = item_tried.useItem(able_to_use, self.getName());
		if result == 0:
			self.modified_description_bool = True;
			return(self.getModifiedDescription());
		return 0;

#This is where the touching of features will happen
	#The feature will have this function called on it so self is the object you are working on
	########################----------------------------------THIS FUNCTION IS WHERE INTERACTIONS GO
	def touchFeature(self, player):
		name = self.getName() #This returns the name of the object, will be used for the if/elif statements
		cr = player.getCurrentRoom();
		if name == "cylinder":
			print("What would you like to set the cylinder to? 0 to 9 Ox")
			
			#accepted input, will loop until an accepted value is put in
			av_array = ["1","2","3","4","5","6","7","8","9","0"]; 
			
			get_input = raw_input(">> ")
			while get_input not in av_array:
				print("Input a number 0 to 9.");
				get_input = raw_input(">> ");
			
			if get_input == "5":
				print("You hear the door on the west wall start to open.\n") #need to set variable to open door
				wr = cr.getWestRoom();#Get the room to the east of the current room (room 3)
				wr.setLocked(False); #Set the rooms locked to false meaning that it can be entered
				return 1; #Return the number of turns used up
			else:
				print("Nothing happens.\n");
			return 1;

		if name == "switch":
			switch_array =[]
			#accepted input, will loop until an accepted value is put in
			av_array = ["up","down"]; 
			
			print("What would you like to set the first switch to up or down?")
			get_input = raw_input(">> ")
			while get_input.lower() not in av_array:
				print("Input Up or down please.");
				get_input = raw_input(">> ");

			switch_array.append(get_input)
			
			print("What would you like to set the second switch to up or down?")
			get_input = raw_input(">> ")
			while get_input.lower() not in av_array:
				print("Input Up or down please.");
				get_input = raw_input(">> ");

			switch_array.append(get_input)
			

			print("What would you like to set the third switch to up or down?")
			get_input = raw_input(">> ")
			while get_input.lower() not in av_array:
				print("Input Up or down please.");
				get_input = raw_input(">> ");


			switch_array.append(get_input)
			

			print("What would you like to set the fourth switch to up or down?")
			get_input = raw_input(">> ")
			while get_input.lower() not in av_array:
				print("Input Up or down please.");
				get_input = raw_input(">> ");


			switch_array.append(get_input)

			if switch_array[0] == 'up' and switch_array[1] == 'down' and switch_array[2] == 'down' and switch_array[3] == 'up':
				print("The door on the north wall starts to open.\n")
			else:
				print("Nothing happens.\n")
			return 1;

		#accepted input, will loop until an accepted value is put in
		av_array = ["head","chest", "stomach"]; 

		if name == "statue of osiris":
			print("What part of the statue would you like to press? (head/chest/stomach)")
			get_input = raw_input(">> ")
			while get_input.lower() not in av_array:
				print("Input head, chest or stomach please.");
				get_input = raw_input(">> ");

			print("A thick cloud of smoke starts coming from the statue, you turn to run but are overwhelmed by the gas.\n")
			return 1;

		if name == "statue of horus":
			print("What part of the statue would you like to press? (head/chest/stomach)")
			get_input = raw_input(">> ")
			while get_input.lower() not in av_array:
				print("Input head, chest or stomach please.");
				get_input = raw_input(">> ");

			print("A thick cloud of smoke starts coming from the statue, you turn to run but are overwhelmed by the gas.\n")
			return 1;

		if name == "statue of anubis":
			print("What part of the statue would you like to press? (head/chest/stomach)")
			get_input = raw_input(">> ")

			while get_input.lower() not in av_array:
				print("Input head, chest or stomach please.");
				get_input = raw_input(">> ");

			print("A thick cloud of smoke starts coming from the statue, you turn to run but are overwhelmed by the gas.\n")
			if get_input == "chest":
				print("The statues hand extends holding a key.\n")
				
				##Adding the key to the players inventory
				player.getInventory().append("key");
				print("key: A key used to open a locked door leading to the Chamber of Passing.")
				print("Added key to inventory.\n");
				###

				print("Congrats on completing the demo. Come back when the game is finished!!\n")
				exit()
			else:
				print("A thick cloud of smoke starts coming from the statue, you turn to run but are overwhelmed by the gas.\n")
			return 1;
		
		################Starting here follow the format of above
		##Return the number of turns lost by touching the feature
		if name == "urn":
			av_array = ["top","side"]
			print("What part of the urn would you like to press? (top/side)")
			get_input = raw_input(">> ")
			while get_input.lower() not in av_array:
				print("Input top or side please.");
				get_input = raw_input(">> ");
			if get_input == "top":
				print("Pressing down on the urn reveals its hard, cold, and study structure.\n")
			else: 
				print("The urn falls over on its side, and it breaks open and reveals a shiny brooch. So you decide to pick up the brooch, and add it to your inventory.\n")
				cr.items.append("brooch") 
			return 1;
		
		
		########################################################################################################

	def __init__(self, na, desc, md, us):
		self.setDescription(desc);
		self.setName(na);
		self.setModifiedDescription(md);
		self.setUsage(us);

#This is the Room class in the game, it is the basis of the game, fix to match the rest of the classes with set/get functions
class Room:
	long_description = ""; # Long description for when entering the room for the first time
	short_description = ""; # Short Description for when entering the room every subsequent time
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
	
	#Function that returns the list of items in the room
	def getItems(self):
		return self.items;
		
	def setItems(self, i):
		self.items = i;
		return 0;
	#Function that adds an item to the room using its' id, returns nothing
	def addItemToRoom(self, item_to_add):
		i = self.getItems()
		i.append(item_to_add);
		self.setItems(i);
		return 0;
	
	#Function that removes an item from the room using its' id, returns 0 if fine or 1 if there is no item to remove
	def removeItemFromRoom(self, item_to_remove):
		i = self.getItems()
		i.remove(item_to_remove);
		self.setItems(i);
		return 0;
	
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
			return self.getShortDescription();
	
	#Function to initialize a Room object, takes id, long desc, short desc, additional desc, items, and features 
	def __init__(self, na, ld, sd, it, fe, lk):
		self.setName(na);
		self.long_description = ld;
		self.short_description = sd;
		self.items = it;
		self.features = fe;
		self.visited = False;
		self.setLocked(lk);

#This is the game manager class in the game
class GameManager:
	turn_count = -1; # turn count remaining
	current_room = None; # current room the game is in
		
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
		
	def __init__(self, tc, cr):
		self.turn_count = tc;
		self.current_room = cr;
		
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
		i = self.getInventory()
		i.append(item_to_add);
		self.setInventory(i);
		self.getCurrentRoom().removeItemFromRoom(item_to_add);
		return 0;
		
	def removeFromInventory(self, item_to_remove):
		i = self.getInventory()
		i.remove(item_to_remove);
		self.setInventory(i);
		self.getCurrentRoom().addItemToRoom(item_to_remove);
		return 0;
		
	def useItemFromInventory(self, item_to_use):
		inven = self.getInventory();
		for it in inven[:]:
			if item_to_use == it:
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
		
		if room_to_move_to_string == "go north":
			if room_to_north != None:
				if room_to_north.getLocked() == False:
					is_room = True;
					room_to_move_to = room_to_north;
				else:
					print("You tried to enter the " + room_to_north.getName() + " but it appears to be locked somehow.\n")
					return 1;		

		if room_to_move_to_string == "go south":
			if room_to_south != None:
				if room_to_south.getLocked() == False:
					is_room = True;
					room_to_move_to = room_to_south;
				else:
					print("You tried to enter the " + room_to_south.getName() + " but it appears to be locked somehow.\n")
					return 1;

		if room_to_move_to_string == "go east":
			if room_to_east != None:
				if room_to_east.getLocked() == False:
					is_room = True;
					room_to_move_to = room_to_east;		
				else:
					print("You tried to enter the " + room_to_east.getName() + " but it appears to be locked somehow.\n")
					return 1;
		
		if room_to_move_to_string == "go west":
			if room_to_west != None:
				if room_to_west.getLocked() == False:
					is_room = True;
					room_to_move_to = room_to_west;		
				else:
					print("You tried to enter the " + room_to_west.getName() + " but it appears to be locked somehow.\n")
					return 1;
					
		if is_room == True:
			gm = self.getGameManager();
			self.setCurrentRoom(room_to_move_to);
			gm.setCurrentRoom(room_to_move_to)
		
		else:
			print("There is no room in that direction\n");
			return 1; #Not able to move
		return 0; #Able to move
	
	def __init__(self, inven, gm):
		self.setInventory(inven);
		self.setGameManager(gm);
