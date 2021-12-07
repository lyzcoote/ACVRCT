import random
import os
import api as api
"""
Create a function that shows the system Arch and OS in Python
"""

def get_arch_os():
    """
    Return the system architecture and OS
    """
    import platform
    return platform.system()

def os_platform():
    import os
    true_platform = os.environ['PROCESSOR_ARCHITECTURE']
    try:
            true_platform = os.environ["PROCESSOR_ARCHITEW6432"]
    except KeyError:
            pass
            #true_platform not assigned to if this does not exist
    return true_platform

def worldIDs(worldID):
    
    stockWorldID = {
	    0: "wrld_6caf5200-70e1-46c2-b043-e3c4abe69e0f",  #The Great Pug
	    1: "wrld_1917b43c-7d1b-4734-87db-2956c2069059",  #The Great Pug - West
	    2: "wrld_26b9df81-32de-48aa-af1a-fcfaac1ee221",  #Steak Meeting
	    3: "wrld_6c66441c-dc59-414a-8fb5-3ede903a1373",  #Rabbit Conference
	    4: "wrld_78373831-0109-4808-9b63-27382f4c6975",  #Presentation Room
	    5: "wrld_126db47b-55a1-47a0-a268-26261b66f614",  #Meeting Bunker
	    6: "wrld_8ef393c0-a985-4d7e-90f0-33ab10d41ee3",  #Avatar Testing
	    7: "wrld_d945fde1-987a-45f9-998c-a081fad71ba1",  #Gaia Night
	    8: "wrld_94ef6736-f998-4099-b456-b3a444734013",  #Open Mic Night
	    9: "wrld_7e10376a-29b6-43af-ac5d-6eb72732e90c",  #Void Club
	    10: "wrld_eb29da5f-a3db-4a35-be57-9bc993d8d156", #VOLT Dance Club
	    11: "wrld_b42b3b0e-a96b-4421-b9b2-dd41b88c9a1a", #Comfy Cave
        12: "wrld_3d892cf2-cd4a-4322-9e7e-2ec0cd7ea44c", #The Afterdark Arcade
        13: "wrld_4cf554b4-430c-4f8f-b53e-1f294eed230b", #The Black Cat
        14: "wrld_df2776a3-8c84-45e3-bbf1-30ac8422911b", #Kitchen Cooks!
        15: "wrld_cf5a728d-00df-428d-9424-64900200643d", #WDKS Horror Experience
        16: "wrld_e4908cea-023b-4749-9ad7-a898b12996e7", #Test Pilots
        17: "wrld_791ebf58-54ce-4d3a-a0a0-39f10e1b20b2", #Movie and chill
        18: "wrld_fac11e5f-1c73-4436-8936-a70b80961c5a"  #Rest and sleep
    }

    return stockWorldID[worldID - 1]



def displayWorldNames():
    """
    Return a list of all the worlds with formatting given a worldname list
    """
    world_list = ["The Great Pug", "The Great Pug - West", "Steak Meeting",
    "Rabbit Conference", "Presentation Room", "Meeting Bunker", "Avatar Testing", "Gaia Night",
    "Open Mic Night", "Void Club", "VOLT Dance Club", "Comfy Cave", "The Afterdark Arcade", "The Black Cat", 
    "Kitchen Cooks!", "WDKS Horror Experience", "Test Pilots", "Movie and Chill", "Rest and Sleep"]
    n = 1
    for world in world_list:
        print("{} - {}".format(n, world))
        n += 1


def displayInstanceTypes():
    instance_list = ["0 - Public World", "1 - Friends World", "2 - Hidden World", "3 - Private World", "4 - Private World"]
    print("\n[!] WARNING! Only public worlds are supported at this time. \n The other type of worlds will load after some minutes.")
    print("\n")
    list(map(lambda x: print("{}".format(x)), instance_list))


def displayWorldRegions():
    region_list = ["US West", "US East", "Europe", "Japan"]
    n = 1
    for world in region_list:
        print("{} - {}".format(n, world))
        n += 1

"""
Create a array of all the world instances
"""
def world_instances(instanceID):
    

    world_instances = {
        0: "public", #Public World
        1: "friends", #Friends World
        2: "hidden", #Hidden World
        3: "private", #Private World
        4: "private" #Private World

    }
    return world_instances[instanceID]


def world_region(regionID):

    world_region = {
        0: "us", #US West
        1: "use", #US East
        2: "eu", #Europe
        3: "jp" #Japan

    }
    return world_region[regionID - 1]
    
    
"""
Create a simple log manager with errors, warning and success messages with the current time
"""
def log_manager(message, message_type):
    """
    Return a message with a message type and time
    """
    from datetime import datetime
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    if message_type == "error":
        print("[{}] [ERROR]: {}".format(current_time, message))
    elif message_type == "warning":
        print("[{}] [WARNING]: {}".format(current_time, message))
    elif message_type == "success":
        print("[{}] [SUCCESS]: {}".format(current_time, message))


def main():
    """
    Main function
    """
    print("\n")
    print("[!] Welcome to the World Manager! \n")
    print("[!] Please select an option: \n")
    print("[!] 1 - Display all worlds \n")
    print("[!] 2 - Display all instance types \n")
    print("[!] 3 - Display all world regions \n")
    print("[!] 4 - Launch VRChat Instance \n")
    print("[!] 5 - Exit \n")
    print("\n")
    while True:
        try:
            option = int(input("[!] Please select an option: "))
            if option == 1:
                print("\n")
                #os.system("cls")
                displayWorldNames()
                print("\n")
            elif option == 2:
                print("\n")
                #os.system("cls")
                displayInstanceTypes()
                print("\n")
            elif option == 3:
                print("\n")
                #os.system("cls")
                displayWorldRegions()
                print("\n")
            elif option == 4:
                print("\n")
                lauchVRChat()
                print("\n")
                break
            elif option == 5:
                print("\n")
                print("[!] Goodbye!")
                print("\n")
                break
            else:
                print("\n")
                print("[!] Invalid option! Please try again. \n")
                print("\n")
                continue
        except ValueError:
            print("\n")
            print("[!] Invalid option! Please try again. \n")
            print("\n")
            continue

def lauchVRChat():
    log_manager("This is a test message", "success")
    displayInstanceTypes()
    print("\n")

    print(displayWorldNames())
    print("\n")

    print(displayWorldRegions())
    print("\n")

    instanceID = int(input("Enter the world instance type: "))

    if(instanceID == 0):
        worldURL = "vrchat://launch?id={}:{}~region({})".format(worldIDs(int(input("Enter a world ID: "))),
     random.randint(300, 1000),
      world_region(int(input("Enter a world region ID: "))))
    else:
        userID = api.getUserID(api.getAPIKey(), str(input("Enter your username: ")))
        worldURL = "vrchat://launch?id={}:{}~{}({})~region({})~nonce(314e6a52-3125-4722-b313-f2666a094c43)".format(worldIDs(int(input("Enter a world ID: "))),
     random.randint(300, 1000),
     world_instances(instanceID),
     userID,
      world_region(int(input("Enter a world region ID: "))))
      
      

    """print(world_instances(int(input("Enter a world instance ID: "))))"""

    """Create a url with the world ID and world instance ID given by the user """
    print("\n")
    print(worldURL)
    """Open the url in the default browser """
    os.system("start \"\" \"{}\"".format(worldURL))

    log_manager("Log Manager ended!", "success")

"""
Create the main function that uses the log_manager function
"""
if __name__ == "__main__":
    main()
    
    
    





