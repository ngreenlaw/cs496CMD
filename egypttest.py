#Test Script For Egypt Game

import egyptclass as ec

test_count_pass = 0;
total_test_count = 0;

def addTestPass():
        global test_count_pass;
        test_count_pass += 1;

def addTestCount():
        global total_test_count;
        total_test_count += 1;

#add the testing writing to a file and the date/time
def assertCorrect(test_string, value_received, value_expected):
        print("--------------------");
        print(test_string + ": " + "Expected: " + str(value_expected) + " Received: " + str(value_received));
        if value_received == value_expected:
                print("-----PASS");
                addTestPass();
        else:
                print("-----FAILED");
        print("--------------------");
        addTestCount();

def assertIsCorrect(test_string, value_received, value_expected):
        print("--------------------");
        print(test_string + ": " + "Expected: " + str(value_expected) + " Received: " + str(value_received));
        if value_received is value_expected:
                print("-----PASS");
                addTestPass();
        else:
                print("-----FAILED");
        print("--------------------");
        addTestCount();
		
def main():

	print("------------------------BEGIN TESTING-------------------------------");

	#Set up all the variables, create the items first, then the features, then the rooms, then the 
	test_id_list = [];
	for i in range(0,10):
		test_id_list.append(i);

	emptyList = [];		
	#Set up Items
	test_item_1 = ec.Item("Torch", "Used to light the way");
	test_item_2 = ec.Item("Sword", "Used to slash things");
	test_item_3 = ec.Item("Scarab Brooch", "Brooch shaped like a scarab");
	
	#Set up features
	test_feature_1 = ec.Feature("Door", "An object that separates rooms", "The door is now unlocked",["Scarab Brooch"]);
	test_feature_2 = ec.Feature("Jackal Statue","A sculpture of a jackal", "The statue is now broken", [""]);
	test_feature_3 = ec.Feature("Ra Tapestry", "A tapestry featuring the god Ra", "The tapestry is ripped up", ["Sword"]);
	
	#Set up item list
	test_item_list_1 = [test_item_1.name, test_item_2.name];
	test_item_list_2 = [test_item_3.name];

	#set up feature list
	test_feature_list_1 = [test_feature_1.name, test_feature_2.name];
	test_feature_list_2 = [test_feature_3.name];
	
	#set features usage with items
	test_feature_1.setUsage([test_item_3.name]);
	test_feature_3.setUsage(["Sword"]);
	
	#Set up rooms
	test_room_1 = ec.Room("Test Room 1", "This is the long description", "Short", test_item_list_1, test_feature_list_2, False)
	test_room_2 = ec.Room("Test Room 2", "Long desc", "Sh",test_item_list_2, test_feature_list_1, False);
	
	test_room_1.setNorthRoom(test_room_2);
	test_room_2.setSouthRoom(test_room_1);
	
	#set up game manager
	test_gameManager = ec.GameManager(50, test_room_1, test_room_1);
	
	#set up player
	test_player = ec.Player(emptyList, test_gameManager);
	
	#---------------Start the testing of the functions
	
	#Test the player
	emptyList = [];
	
	assertCorrect("Player Current Room", test_player.getCurrentRoom(), None);
	assertCorrect("Player Inventory", test_player.getInventory(), emptyList);
	
	#Test Move Room
	assertCorrect("Room 1 Visited", test_room_1.getVisited(), False);
	test_player.setCurrentRoom(test_room_1);
	test_room_1.setVisited(True);
	assertCorrect("Attempt to Move to South Room", test_player.moveRoom("South"), 1);
	test_player.moveRoom("north");
	assertIsCorrect("Move to Room 2", test_player.getCurrentRoom(), test_room_2);
		
	#Test the Room

	assertCorrect("Long Desc", test_room_1.getLongDescription(), "This is the long description");
	assertCorrect("Short Desc", test_room_1.getShortDescription(), "Short");
	assertCorrect("Modified Desc", test_room_1.getModifiedDescription(), "Short");
	assertCorrect("Items in room", test_room_1.getItems(), test_item_list_1);
	assertCorrect("Features in room", test_room_1.getFeatures(), test_feature_list_2);
	assertCorrect("Room 1 Visited", test_room_1.getVisited(), True);
	assertIsCorrect("Room 1 is South of Room 2", test_room_2.getSouthRoom(), test_room_1);
	assertCorrect("Room 1 East is None", test_room_1.getEastRoom(), None); 
	
	#Test the items
	assertCorrect("Item name", test_item_1.getName(), "Torch");
	assertCorrect("Item Desc", test_item_1.getDescription(), "Used to light the way");
	
	#Test items interacting with features
	assertCorrect("Item Used Function True", test_item_3.useItem(True, "Door"), 0); 
	assertCorrect("Item Used Function False", test_item_3.useItem(False, test_feature_3.name), 1); 
	
	#Test Player picking up and dropping items
	#Includes players and room for testing
	
	#Test the features
	assertCorrect("Feature name", test_feature_1.getName(), "Door");
	assertCorrect("Feature desc", test_feature_2.getDescription(), "A sculpture of a jackal");
	assertCorrect("Feature desc mod", test_feature_3.getModifiedDescription(), "The tapestry is ripped up");
	
	#test the features interacting with items
	assertCorrect("Use Torch on Door", test_feature_1.interactWith(test_item_1), 1);
	assertCorrect("Use Sword on Tapestry", test_feature_3.interactWith(test_item_2), 0);
	assertCorrect("Door Desc not modified after interaction", test_feature_1.modified_description_bool, False);
	assertCorrect("Tapestry Modified After Interaction", test_feature_3.modified_description_bool, True);
	
	#Test the game manager
	assertCorrect("GM Turn Count", test_gameManager.getTurnCount(), 50);
	assertIsCorrect("GM Current Room", test_gameManager.getCurrentRoom().name, test_room_2.name);

	print(str(test_count_pass) + " out of " + str(total_test_count) + " passed");
	print("------------------------TESTING FINISHED-------------------------------");
                      
#run the program
if __name__ == "__main__":
	main();
	
