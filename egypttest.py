#Test Script For Egypt Game

import egyptclass as ec

#add the testing writing to a file and the date/time
def assertCorrect(test_string, value_received, value_expected):
        print("--------------------");
        print(test_string + ": " + "Expected: " + str(value_expected) + " Received: " + str(value_received));
        if value_received == value_expected:
                print("-----PASS");
        else:
                print("-----FAILED");
        print("--------------------");

def assertIsCorrect(test_string, value_received, value_expected):
        print("--------------------");
        print(test_string + ": " + "Expected: " + str(value_expected) + " Received: " + str(value_received));
        if value_received is value_expected:
                print("-----PASS");
        else:
                print("-----FAILED");
        print("--------------------");
		
def main():

	print("------------------------BEGIN TESTING-------------------------------");

	#Set up all the variables, create the items first, then the features, then the rooms, then the 
	test_id_list = [];
	for i in range(0,10):
		test_id_list.append(i);

	emptyList = [];		
	test_item_1 = ec.Item(test_id_list[0], "Torch", "Used to light the way", "Light");
	test_item_2 = ec.Item(test_id_list[1], "Sword", "Used to slash things", "Weapon");
	test_item_3 = ec.Item(test_id_list[2], "Scarab Brooch", "Brooch shaped like a scarab", "Key");
	
	test_feature_1 = ec.Feature(test_id_list[3], "Door", "An object that separates rooms", "The door is now unlocked", "Door");
	test_feature_2 = ec.Feature(test_id_list[4], "Jackal Statue","A sculpture of a jackal", "The statue is now broken", "Statue");
	test_feature_3 = ec.Feature(test_id_list[5], "Ra Tapestry", "A tapestry featuring the god Ra", "The tapestry is ripped up", "Tapestry");
	
	test_item_list_1 = [test_item_1, test_item_2];
	test_item_list_2 = [test_item_3];
	
	test_feature_list_1 = [test_feature_1, test_feature_2];
	test_feature_list_2 = [test_feature_3];
	
	#set Item and features interaction/usage functions
	#test_feature_1.setUsage([list of item types it can interact with]) Later can be added to initialize function
	
	test_room_1 = ec.Room(test_id_list[6], "Test Room 1", "This is the long description", "Short", ["add"," this"], test_item_list_1, test_feature_list_2)
	test_room_2 = ec.Room(test_id_list[7], "Test Room 2", "Long desc", "Sh", ["this", "to add"], test_item_list_2, test_feature_list_1);
	
	test_room_1.setNorthRoom(test_room_2);
	test_room_2.setSouthRoom(test_room_1);

        #Set the features room location
	
	test_gameManager = ec.GameManager(test_id_list[9], 50, test_room_1);
	
	test_player = ec.Player(test_id_list[8], emptyList, test_gameManager);
	
	#Start the testing of the functions
	
	#Test the player
	emptyList = [];
	assertCorrect("Player id", test_player.getId(), 8);
	assertCorrect("Player Current Room", test_player.getCurrentRoom(), None);
	assertCorrect("Player Inventory", test_player.getInventory(), emptyList);
	
	#Test Move Room
	assertCorrect("Room 1 Visited", test_room_1.getVisited(), False);
	test_player.moveRoom(test_room_1);
	assertIsCorrect("Move to Room 1", test_player.getCurrentRoom(), test_room_1);
		
	#Test the Room
	assertCorrect("Room id", test_room_1.getId(), 6);
	assertCorrect("Long Desc", test_room_1.getLongDescription(), "This is the long description");
	assertCorrect("Short Desc", test_room_1.getShortDescription(), "Short");
	assertCorrect("Modified Desc", test_room_1.getModifiedDescription(), "Short");
	test_room_1.updateDescription(0);
	assertCorrect("Updated Desc", test_room_1.getModifiedDescription(), "Short add");
	assertCorrect("Items in room", test_room_1.getItems(), test_item_list_1);
	assertCorrect("Features in room", test_room_1.getFeatures(), test_feature_list_2);
	assertCorrect("Room 1 Visited", test_room_1.getVisited(), True);
	assertIsCorrect("Room 1 North is Room 2", test_room_1.getNorthRoom(), test_room_2);
	assertCorrect("Room 1 East is None", test_room_1.getEastRoom(), None); 
	
	#Test the room functions of item and features
	
	#Test the items
	
	#Test the features
	
	#Test the game manager
	assertIsCorrect("Room 2 is North in GameManager", test_gameManager.getNorthRoom(), test_room_2);
	
	print("------------------------TESTING FINISHED-------------------------------");
                      
#run the program
if __name__ == "__main__":
	main();
	
