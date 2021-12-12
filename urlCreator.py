################################################################################
#                                                                              #
#                                    Modules                                   #
#                                                                              #
################################################################################

import worldManager as wm
import os
import random
import apiHandler as APIHandler
import otherUtils as otherUtils
import logManager as logManager

################################################################################
#                                                                              #
#                                   Functions                                  #
#                                                                              #
################################################################################


def createCustomSession():
    """
    Creates a custom VRChat session based on the user choices.
    """
    wm.displayInstanceTypes()
    print("\n")
    instanceID = wm.getInstanceType(int(input("[i] Enter the world instance type: ")))
    os.system("cls")
    print(wm.displayWorldNames())
    print("\n")
    worldID = wm.getWorldID(int(input("[i] Enter a world ID: ")))
    os.system("cls")
    print(wm.displayWorldRegions())
    print("\n")
    regionID = wm.getWorldRegion(int(input("[i] Enter a world region: ")))
    os.system("cls")

    if(instanceID == "public"):
        worldURL = "vrchat://launch?id={}:{}~region({})".format(worldID, random.randint(300, 1000), regionID)
    else:
        userID = APIHandler.getUserID(APIHandler.getCachedAPIKey(), str(input("[i] Enter the username of the session owner: ")))
        worldURL = "vrchat://launch?id={}:{}~{}({})~region({})~nonce(314e6a52-3125-4722-b313-f2666a094c43)".format(worldID, random.randint(300, 1000), instanceID, userID, regionID)

    """Create a url with the world ID and world instance ID given by the user """
    os.system("cls")
    print("\n")
    message = ["[i] Launching world... ","    Name: {}".format(APIHandler.getWorldNamebyID(worldID)),
        "    Region: {}".format(regionID.upper()),
        "    Instance type: {}".format(instanceID)]
    otherUtils.printBox(message)
    print(worldURL)
    """Open the url in the default browser """
    os.system("start \"\" \"{}\"".format(worldURL))

    logManager.logger("Log Manager ended!", "success")