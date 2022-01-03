################################################################################
#                                                                              #
#                                    Modules                                   #
#                                                                              #
################################################################################

import worldManager as worldManager
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
    """Display the custom session creation menu
    Starting with the Instance Types"""
    worldManager.displayInstanceTypes()
    print("\n")
    """Get the user's choice"""
    instanceType = worldManager.getInstanceType(int(input("[i] Enter the world instance type: ")))
    """If the user choice is not valid, return to the menu"""
    if(instanceType == False):
        logManager.logger("Invalid instance type.", "error")
        exit()
    os.system("cls")
    """Display the world names list"""
    print(worldManager.displayWorldNames())
    print("\n")
    """Get the user's choice"""
    worldID = worldManager.getWorldID(int(input("[i] Enter a world ID: ")))
    os.system("cls")
    """Display the world regions list"""
    print(worldManager.displayWorldRegions())
    print("\n")
    """Get the user's choice"""
    regionID = worldManager.getWorldRegion(int(input("[i] Enter a world region: ")))
    os.system("cls")

    """Elaborate the user's choices of the world instance type, world name and world region"""
    if(instanceType == "public"):
        """"If the user choice is public, the userID of the Session Owner, Nonce  and Instance ID are not needed, using only the world name and world region"""
        """Creating the world URL"""
        worldURL = "vrchat://launch?id="f"{worldID}:"f"{random.randint(300, 1000)}""~region("f"{regionID})"

    elif(instanceType == "private"):
        """If the user choice is private, first of, we need the worldID,
        secondly, we need a random SessionID, the IstanceType, after that,
        we need the userID of the Session Owner, 
        which is calculated by the getUserID() of the APIHandler, 
        after that (again), we need the Region Type and the NonCE"""
        userID = APIHandler.getUserID(APIHandler.getCachedAPIKey(), str(input("[i] Enter the username of the session owner: ")))
        """Finally, we create the world URL"""
        worldURL = "vrchat://launch?id="f"{worldID}"":"f"{random.randint(300, 1000)}""~"f"{instanceType}""("f"{userID}"")~region("f"{regionID}"")~nonce("f"{otherUtils.generateRandomUUID()}"")"

    elif(instanceType == False):
        """If the user choice is invalid, return False"""
        return False
    else:
        """If the user choice is invalid, dsiplay and error and returns False"""
        logManager.logger("Invalid instance type.", "error")
        return False

    os.system("cls")
    print("\n")

    """Printing the Instance Details"""
    message = ["[i] Launching world... ","    Name: "f"{APIHandler.getWorldNamebyID(worldID)}",
        "    Region: "f"{regionID.upper()}",
        "    Instance type: "f"{instanceType}"]
    otherUtils.printBox(message)

    """Launching VRChat with the world URL"""
    os.system("start \"\" \""f"{worldURL}\"")