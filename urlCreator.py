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
    if(instanceID == False):
        logManager.logger("Invalid instance type.", "error")
        exit()
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
        worldURL = "vrchat://launch?id="f"{worldID}:"f"{random.randint(300, 1000)}""~region("f"{regionID})"
    elif(instanceID == "private"):
        userID = APIHandler.getUserID(APIHandler.getCachedAPIKey(), str(input("[i] Enter the username of the session owner: ")))
        worldURL = "vrchat://launch?id="f"{worldID}"":"f"{random.randint(300, 1000)}""~"f"{instanceID}""("f"{userID}"")~region("f"{regionID}"")~nonce("f"{otherUtils.generateRandomUUID()}"")"
    elif(instanceID == False):
        return False
    else:
        logManager.logger("Invalid instance type.", "error")
        return False

    """Create a url with the world ID and world instance ID given by the user """
    os.system("cls")
    print("\n")
    message = ["[i] Launching world... ","    Name: "f"{APIHandler.getWorldNamebyID(worldID)}",
        "    Region: "f"{regionID.upper()}",
        "    Instance type: "f"{instanceID}"]
    otherUtils.printBox(message)
    #print(worldURL)
    """Open the url in the default browser """
    os.system("start \"\" \""f"{worldURL}\"")

    logManager.logger("Log Manager ended!", "success")