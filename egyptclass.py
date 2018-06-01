#This is a file containing the classes and functions for the game

#This is the item class in the game
class Item:
	name = ""; #name of item
	description = ""; #description of item
	parser = ""
		
	def displayDescription(self):
		return(self.description);
			
	def __init__(self, na, desc, pa):
		self.name = na;
		self.description = desc;
		self.parser = pa;

#This is the feature class in the game
class Feature:
	name = ""; #name of the feature
	description = ""; #description of the feature
	modified_description = ""; #description of the feature when modified
	modified_description_bool = False; # Tells whether or not to use the modified description
	parser = ""; # The value that matches the parser returning	

	def displayDescription(self):
		if self.modified_description_bool == False:
			return(self.description);
		else:
			return(self.modified_description);

#This is where the touching of features will happen
	#The feature will have this function called on it so self is the object you are working on
	########################----------------------------------THIS FUNCTION IS WHERE INTERACTIONS GO
	def touchFeature(self, player):
		name = self.name #This returns the name of the object, will be used for the if/elif statements
		cr = player.current_room;
		wr = cr.west_room;
		nr = cr.north_room
		er = cr.east_room;
		if name == "Cylinder" and wr.locked == True:
			print("What would you like to set the cylinder to? 0 to 9 Ox")
			
			#accepted input, will loop until an accepted value is put in
			av_array = ["1","2","3","4","5","6","7","8","9","0"]; 
			
			get_input = raw_input(">> ")
			while get_input not in av_array:
				print("Input a number 0 to 9.");
				get_input = raw_input(">> ");
			
			if get_input == "5":
				print("You hear the doors on the west and east wall start to open.\n") #need to set variable to open door
				wr.locked = False; #Set the rooms locked to false meaning that it can be entered
				er.locked = False;
				self.modified_description_bool = True
				return 1; #Return the number of turns used up
			else:
				print("Nothing happens.\n");
			return 1;

		if name == "Cylinder" and wr.locked == False:
			print("There is no need to touch the cylinder, the door is open already.\n");
			return 0;
			
		if name == "Switch" and nr.locked == True:
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
				nr.locked = False;
				return 1;
			else:
				print("Nothing happens.\n")
			return 1;
			
			if name == "Switch" and nr.locked == False:
				print("There is no need to touch the switches, the door is open already.\n");
				return 0;

		#accepted input, will loop until an accepted value is put in
		av_array = ["head","chest", "stomach"]; 

		if name == "Statue of Osiris":
			print("What part of the statue would you like to press? (head/chest/stomach)")
			get_input = raw_input(">> ")
			while get_input.lower() not in av_array:
				print("Input head, chest or stomach please.");
				get_input = raw_input(">> ");

			print("A thick cloud of smoke starts coming from the statue, you turn to run but are overwhelmed by the gas.\n")
			return 1;

		if name == "Statue of Horus":
			print("What part of the statue would you like to press? (head/chest/stomach)")
			get_input = raw_input(">> ")
			while get_input.lower() not in av_array:
				print("Input head, chest or stomach please.");
				get_input = raw_input(">> ");

			print("A thick cloud of smoke starts coming from the statue, you turn to run but are overwhelmed by the gas.\n")
			return 1;

		if name == "Statue of Anubis":
			print("What part of the statue would you like to press? (head/chest/stomach)")
			get_input = raw_input(">> ")

			while get_input.lower() not in av_array:
				print("Input head, chest or stomach please.");
				get_input = raw_input(">> ");

			#print("A thick cloud of smoke starts coming from the statue, you turn to run but are overwhelmed by the gas.\n")
			
			if get_input == "chest":
				print("The statues hand extends holding a key.\n")
				
				##Adding the key to the players inventory
				player.inventory.append("Chamber of Passing Key");
				print("Chamber of Passing Key: A key used to open a locked door leading to the Chamber of Passing.")
				print("Added key to inventory.\n");
				###

			else:
				print("A thick cloud of smoke starts coming from the statue, you turn to run but are overwhelmed by the gas.\n")
			return 1;
		
		################Starting here follow the format of above
		##Return the number of turns lost by touching the feature
		if name == "Urn":
			av_array = ["top","side"]
			print("What part of the urn would you like to press? (top/side)")
			get_input = raw_input(">> ")
			while get_input.lower() not in av_array:
				print("Input top or side please.");
				get_input = raw_input(">> ");
			if get_input == "top":
				print("Pressing down on the urn reveals its hard, cold, and study structure.\n")
			else: 
				player.removeFromInventory("Urn");
				cr.items.remove("Urn")
				print("Upon dropping the urn, it lands on the ground and breaks open revealing a shiny brooch. You decide to pick it up and add it to your inventory.\n");
				cr.items.append("Scarab Brooch")
				player.addToInventory("Scarab Brooch")
			return 1;
		
		if name == "Shaky Mummy":
			if self.modified_description_bool == False:
				print("Upon closer inspection, the mummy turns out to be a mythical crocodile. It bites your arm causing great pain before scampering off into the dark.")
				self.modified_description_bool = True
				return 3;
			else:
				print("The Mythical Crocodile Mummy has scampered into the dark. You cannot touch it.")
				return 0;
				
		if name == "Mirror Spider":
			if self.modified_description_bool == False:
				print("The rustling turns out to be a gigantic spider.  The spider bites you and causes pain and injury.")
				self.modified_description_bool = True
				return 3;
			else:
				print("The gigantic spider has scampered off.")
				return 0;
			
		if name == "Food Spider":
			if self.modified_description_bool == False:
				print("The rustling turns out to be a gigantic spider.  The spider bites you and causes pain and injury.")
				self.modified_description_bool = True
				return 3;
			else:
				print("The gigantic spider has scampered off.")
				return 0;
		
		if name == "Noisy Sarcophagus":
			if self.modified_description_bool == False:
				print("Upon opening the sarcophagus, a mythical pharaoh mummy jumps out, makes a loud screech, and then attacks you before disappearing into the darkness.")
				self.modified_description_bool = True
				return 3
			else:
				print("An empty Sarcophagus that a mythical pharaoh jumped out of and hurt you before running away.")
				return 0;
	
		########################################################################################################
		
		if name == "Tapestry of Ra":
			if "Sword" in player.inventory:
				print("Upon touching the tapestry it appears thin enough to cut through it with your sword, would you like to? (yes/no)")
				av_array = ["yes", "no"]
				get_input = raw_input(">> ")
				while get_input.lower() not in av_array:
					print("Input yes or no please.");
					get_input = raw_input(">> ");
				if get_input == "yes":
					print("With a slash of the sword the tapestry falls apart revealing a staircase behind it.\n")
					cr.north_room.locked = False #allow moving into the next room
					self.modified_description = "The tapestry previously of Ra is now in tatters.";
					self.modified_description_bool = True;
					return 1;
				else: 
					print("The tapestry is left untouched.\n")
					return 0;
			else:
				print("Upon touching the tapestry it appears thin enough to cut through it with something. You also feel a breeze coming from behind it.")
			return 0;
		
		if name == "Tapestry of Set":
			if "Sword" in player.inventory:
				print("Upon touching the tapestry it appears thin enough to cut through it with your sword, would you like to? (yes/no)")
				av_array = ["yes", "no"]
				get_input = raw_input(">> ")
				while get_input.lower() not in av_array:
					print("Input yes or no please.");
					get_input = raw_input(">> ");
				if get_input == "yes":
					print("With a slash of the sword the tapestry falls apart revealing the wall behind it.\n")
					self.modified_description = "The tapestry previously of Set is now in tatters.";
					self.modified_description_bool = True;
					return 1;
				else: 
					print("The tapestry is left untouched.\n")
					return 0;
			else:
				print("Upon touching the tapestry it appears thin enough to cut through it with something.")
			return 0;

		if name == "Tapestry of Isis":
			if "Sword" in player.inventory:
				print("Upon touching the tapestry it appears thin enough to cut through it with your sword, would you like to? (yes/no)")
				av_array = ["yes", "no"]
				get_input = raw_input(">> ")
				while get_input.lower() not in av_array:
					print("Input yes or no please.");
					get_input = raw_input(">> ");
				if get_input == "yes":
					self.modified_description = "The tapestry previously of Isis is now in tatters.";
					self.modified_description_bool = True;
					return 1;
				else: 
					print("The tapestry is left untouched.\n")
					return 0;
			else:
				print("Upon touching the tapestry it appears thin enough to cut through it with something.")
			return 0;

		if name == "Wooden Door":
			if "Chamber of Passing Key" in player.inventory:
				cr.north_room.locked = False;
				self.modified_description_bool = True;
				print("You put the key in the lock and turn it and with a click the door swings open.\n");
				return 1;
			else:
				print("It looks like there is a spot to put a key in the door.\n")
				return 0;

		if name == "Statue of Sphinx":
			if self.modified_description_bool == True:
				print("There is a scarab shaped hole that has appeared in the sphinx, it appears that you can put something in it. Would you like to? (yes/no)?")
				av_array = ["yes", "no"]
				get_input = raw_input(">> ")
				while get_input.lower() not in av_array:
					print("Input yes or no please.");
					get_input = raw_input(">> ");
				if get_input == "yes":
					print("What item from your inventory would you like to try?")
					for i in player.inventory:
						print(i);
					get_input = raw_input(">> ");
					if get_input.lower() == "scarab necklace" and "Scarab Necklace" in player.inventory:
						print("You insert the necklace into the hole and you hear a click. The sphinx statue then slides to reveal a staircase heading down.\n")
						cr.west_room.locked = False;
						self.modified_description = "The sphinx statue has slid revealing a staircase.";	
						return 1;
					else:
						print("You tried to insert the object and nothing happens.\n")
						return 1
				else: 
					print("The hole in the sphinx is left untouched.\n")
					return 0;
			

		if name == "Statue of Griffin":
			av_array = ["yes", "no"]
			print("Upon further inspection it appears the beak can be pulled like a lever. Would you like to? (yes/no)");
			get_input = raw_input(">> ")
			while get_input.lower() not in av_array:
				print("Input yes or no please.");
				get_input = raw_input(">> ");
			if get_input == "yes":
				print("\nYou hear a click as you pull down the lever and then you hear a loud resonding thud from the entrance of the tomb.")
				print("Looking around you see a system of pulleys that you could not see before, it appears that this was the way to unblock the entrance.")
				print("You take a deep breath feeling the air come back into the tomb.\n")
				print("Congratulations! You have assisted in successfully helping Carter complete his expedition! Thank you for playing!")
				exit() #GAME ENDS
				return 1;
			else: 
				print("You decide to leave the statue alone.\n")
				return 0;

		if name == "Statue of Eagle":
			av_array = ["yes", "no"]
			print("Upon further inspection it appears the beak can be pulled like a lever. Would you like to? (yes/no)");
			get_input = raw_input(">> ")
			while get_input.lower() not in av_array:
				print("Input yes or no please.");
				get_input = raw_input(">> ");
			if get_input == "yes":
				print("You pull the beak down and a cloud of gas spits out at you. This causes you to gasp for air, using up precious amounts of the little air you have.\n")
				return 5;
			else: 
				print("You decide to leave the statue alone.\n")
				return 0;
	
		else:
			print("You touch the " + self.name + " and nothing happens.\n")
			return 0;
		
	def __init__(self, na, desc, md, pa):
		self.description = desc
		self.name = na
		self.modified_description = md;
		self.parser = pa;

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
	

	#Function that adds an item to the room using its' id, returns nothing
	def addItemToRoom(self, item_to_add):
		self.items.append(item_to_add);
		return 0;
	
	#Function that removes an item from the room using its' id, returns 0 if fine or 1 if there is no item to remove
	def removeItemFromRoom(self, item_to_remove):
		self.items.remove(item_to_remove);
		return 0;
	
	#Function to set all the rooms at once and returns 0
	def setNSEWRooms(self, nr, sr, er, wr):
		self.north_room = nr;
		self.south_room = sr;
		self.east_room = er;
		self.west_room = wr;
		
	#Function to display the correct description, returns the string for the game to output
	def displayDescription(self):
		if self.visited == False:
			return self.long_description;
		else:
			return self.short_description;
	
	#Function to initialize a Room object, takes id, long desc, short desc, additional desc, items, and features 
	def __init__(self, na, ld, sd, it, fe, lk, nr, sr, er, wr):
		self.name = na;
		self.long_description = ld;
		self.short_description = sd;
		self.items = it;
		self.features = fe;
		self.visited = False;
		self.locked = lk;
		self.north_room = nr;
		self.south_room = sr;
		self.east_room = er;
		self.west_room = wr;
		
#This is the player class in the game
class Player:
	current_room = None;
	inventory = [];
	ears = "no";
	turns = -1;	
		
	def addToInventory(self, item_to_add):
		self.inventory.append(item_to_add);
		self.current_room.removeItemFromRoom(item_to_add);
		return 0;
		
	def removeFromInventory(self, item_to_remove):
		self.inventory.remove(item_to_remove);
		self.current_room.addItemToRoom(item_to_remove);
		return 0;
		
	#This function handles moving rooms	
	def moveRoom(self, room_to_move_to_string):
		cr = self.current_room
		room_to_north = cr.north_room;
		room_to_south = cr.south_room
		room_to_east = cr.east_room
		room_to_west = cr.west_room
		is_room = False;
		room_to_move_to = None;
		
		if room_to_move_to_string == "go north":
			if room_to_north != None:
				if room_to_north.locked == False:
					is_room = True;
					room_to_move_to = room_to_north;
				else:
					print("You tried to enter the " + room_to_north.name + " but it appears to be blocked somehow.\n")
					return 1;		

		if room_to_move_to_string == "go south":
			if room_to_south != None:
				if room_to_south.locked == False:
					is_room = True;
					room_to_move_to = room_to_south;
				else:
					print("You tried to enter the " + room_to_south.name + " but it appears to be blocked somehow.\n")
					return 1;

		if room_to_move_to_string == "go east":
			if room_to_east != None:
				if room_to_east.locked == False:
					is_room = True;
					room_to_move_to = room_to_east;		
				else:
					print("You tried to enter the " + room_to_east.name + " but it appears to be blocked somehow.\n")
					return 1;
		
		if room_to_move_to_string == "go west":
			if room_to_west != None:
				if room_to_west.locked == False:
					is_room = True;
					room_to_move_to = room_to_west;		
				else:
					print("You tried to enter the " + room_to_west.name + " but it appears to be blocked somehow.\n")
					return 1;
					
		if is_room == True:
			self.current_room = room_to_move_to;
		
		else:
			print("There is no room in that direction\n");
			return 1; #Not able to move
		return 0; #Able to move
	
	def __init__(self, inven, tc, cr):
		self.inventory = inven;
		self.turn_count = tc;
		self.current_room = cr;
