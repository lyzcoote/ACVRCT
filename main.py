import random
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
	    0: "0", #Default Selection
	    1: "1", #Custom World ID
	    2: "wrld_6caf5200-70e1-46c2-b043-e3c4abe69e0f",  #The Great Pug
	    3: "wrld_1917b43c-7d1b-4734-87db-2956c2069059",  #The Great Pug - West
	    4: "wrld_26b9df81-32de-48aa-af1a-fcfaac1ee221",  #Steak Meeting
	    5: "wrld_6c66441c-dc59-414a-8fb5-3ede903a1373",  #Rabbit Conference
	    6: "wrld_78373831-0109-4808-9b63-27382f4c6975",  #Presentation Room
	    7: "wrld_126db47b-55a1-47a0-a268-26261b66f614",  #Meeting Bunker
	    8: "wrld_8ef393c0-a985-4d7e-90f0-33ab10d41ee3",  #Avatar Testing
	    9: "wrld_d945fde1-987a-45f9-998c-a081fad71ba1",  #Gaia Night
	    10: "wrld_94ef6736-f998-4099-b456-b3a444734013", #Open Mic Night
	    11: "wrld_7e10376a-29b6-43af-ac5d-6eb72732e90c", #Void Club
	    12: "wrld_eb29da5f-a3db-4a35-be57-9bc993d8d156", #VOLT Dance Club
	    13: "wrld_b42b3b0e-a96b-4421-b9b2-dd41b88c9a1a" #Comfy Cave
    }

    return stockWorldID[worldID - 1]



def displayWorldNames():
    """
    Return a list of all the worlds with formatting given a worldname list
    """
    world_list = ["Default Selection", "Custom World ID", "The Great Pug", "The Great Pug - West", "Steak Meeting",
    "Rabbit Conference", "Presentation Room", "Meeting Bunker", "Avatar Testing", "Gaia Night",
    "Open Mic Night", "Void Club", "VOLT Dance Club", "Comfy Cave"]
    n = 1
    for world in world_list:
        print("{} - {}".format(n, world))
        n += 1


def displayInstanceTypes():
    instance_list = ["Public World", "Friends World", "Hidden World", "Private World"]
    n = 1
    print("[!] WARNING! Only public worlds are supported at this time. \n The other type of worlds will load after some minutes.")
    for world in instance_list:
        print("{} - {}".format(n, world))
        n += 1


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
    return world_instances[instanceID - 1]


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

"""
Create the main function that uses the log_manager function
"""
if __name__ == "__main__":
    """
    Return the system architecture and OS
    """
    print("System Architecture: {}".format(os_platform()) + "\nSystem OS: {}".format(get_arch_os()))
    log_manager("Log Manager started!", "success")
    
    userID = "usr_ea452a01-b107-41a5-a7ec-ce419542772d"

    print(displayWorldNames())
    print("\n")

    print(displayInstanceTypes())
    print("\n")

    print(displayWorldRegions())
    print("\n")

    """print(world_instances(int(input("Enter a world instance ID: "))))"""

    """Create a url with the world ID and world instance ID given by the user """
    worldURL = "vrchat://launch?id={}:{}~{}({})~region({})".format(worldIDs(int(input("Enter a world ID: "))),
     random.randint(300, 1000),
      world_instances(int(input("Enter a world instance ID: "))),
      userID,
      world_region(int(input("Enter a world region ID: "))))
    print("\n")
    print(worldURL)
    """Open the url in the default browser """
    import os
    os.system("start \"\" \"{}\"".format(worldURL))

    log_manager("Log Manager ended!", "success")
    
    





