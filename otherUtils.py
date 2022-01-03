################################################################################
#                                                                              #
#                                    Modules                                   #
#                                                                              #
################################################################################

import os

from requests.api import get
import worldManager as worldManager
import urlCreator as urlHandler
import apiHandler as APIHandler
import logManager as logManager
import cookieFileHandler as cookieHandler
################################################################################
#                                                                              #
#                                   Variables                                  #
#                                                                              #
################################################################################

version = "0.3.0.0Alpha"
authorGitHubUrl = "https://github.com/lyzcoote"

################################################################################
#                                                                              #
#                                   Functions                                  #
#                                                                              #
################################################################################

def getMaxStr(lst):
    """
    Return the maximum string length of a list
    Like duh?
    """
    return max(lst, key=len)


def printBox(list):
    """
    Print a box with the list of strings
    """
    print("+" + "-" * (len(getMaxStr(list)) + 3) + "+")
    for i in list:
        print("| " + i + " " * (len(getMaxStr(list)) - len(i)) + "  |")
    print("+" + "-" * (len(getMaxStr(list)) + 3) + "+")

def displayLoginDisclaimer():
    message = ["[i] A login is required for getting an Authorization Cookie ",
            "    which is necessary for converting a username into UserID ",
            "" ,
            "[!] DISCLAIMER: ",
            "    Your Username and Password will be sent to VRChat API Servers. ",
            "    They won't be sent or saved to the creator of this launcher! ",
            "    If you're not sure about logging in with your account, use a burner account. ",
            "", 
            "[i] If you want to continue, insert your credentials, otherwise feel free to exit."]
    printBox(message)

def display2FADisclaimer():
    message = ["[!] Two-Factor Authentication is enabled on this account. ",
            "    Please insert your two-factor code to continue."]
    printBox(message)

def generateRandomUUID():
    import uuid
    return uuid.uuid4()

def displayDebugMenu():
    message = ["[!] WARNING! This is a debug menu. ",
            "    Please use it only if you know what you're doing. ",
            "    If you're not sure about what you're doing, please exit. "]
    printBox(message)
    print("[i] 1 - Test User Login With 2FA")
    print("[i] 2 - Test Writing Auth Cookie to JSON File")
    print("[i] 3 - Test if Cookie File exists")
    print("[i] 4 - Test if Auth Cookie is Valid")
    print("[i] 5 - Retrive Auth Cookie from JSON File")
    print("[i] 6 - Test Writing 2FA Auth Cookie to JSON File")
    print("[i] 7 - Test UUID Generator")
    print("[i] 0 - Exit \n")
    print("\n")
    while True:
        try:
            option = int(input("[i] Please select an option: "))
            if option == 1:
                print("\n")
                APIHandler.userLoginWith2FA(APIHandler.getCachedAPIKey(), APIHandler.getAuthCookie(APIHandler.getCachedAPIKey()))
                print("\n")
                exit()
            elif option == 2:
                print("\n")
                cookieHandler.writeAuthCookie(APIHandler.getAuthCookie(APIHandler.getCachedAPIKey()))
                print("\n")
                exit()
            elif option == 3:
                print("\n")
                print(cookieHandler.checkifAuthCookieFileExists())
                print("\n")
                exit()
            elif option == 4:
                print("\n")
                print(APIHandler.checkIfAuthCookieIsValid(cookieHandler.retriveAuthCookieFromFile()))
                print("\n")
                exit()
            elif option == 6:
                print("\n")
                cookieHandler.write2FAAuthCookie(APIHandler.userLoginWith2FA(APIHandler.getCachedAPIKey(), APIHandler.getAuthCookie(APIHandler.getCachedAPIKey())))
                print("\n")
                exit()
            elif option == 7:
                print("\n")
                logManager.logger("Random UUID used for Nonce: "f"{generateRandomUUID()}", "info")
                print("\n")
                exit()
            elif option == 0:
                exit()
            else:
                print("\n")
                logManager.logger("Invalid option! Please try again. \n", "error")
                print("\n")
                continue
        except ValueError:
            print("\n")
            logManager.logger("Invalid option! Please try again. \n", "error")
            print("\n")
            continue

def launcherMenu():
    """
    Print the launcher menu
    """
    print("[i] Welcome to ACVRCT! \n")
    print("[i] You're running version: "f"{version}" + "\n")
    print("[!] Please note that this app is not 100% accurate and will contain bug/crashes. \n")
    print("[i] Please select an option: ")
    print("[i] 1 - Display author's GitHub Page")
    print("[i] 2 - Display current VRChat API Key ")
    print("[i] 3 - Display a user info ")
    print("[i] 4 - Launch custom VRChat Instance ")
    print("[i] 5 - Launch Home VRChat World ")
    print("[i] 6 - Exit \n")
    print("[i] 0 - Debug Menu \n")
    print("\n")
    while True:
        try:
            option = int(input("[i] Please select an option: "))
            if option == 1:
                print("\n")
                os.system("cls")
                os.system("start \"\" \""f"{authorGitHubUrl}\"")
                print("\n")
                os.system("cls")
                launcherMenu()
            elif option == 2:
                print("\n")
                os.system("cls")
                logManager.logger("The current VRChat API Key is: "f"{APIHandler.getCachedAPIKey()}", "info")
                os.system("pause")
                os.system("cls")
                launcherMenu()
            elif option == 3:
                print("\n")
                os.system("cls")
                APIHandler.getUserInfo(APIHandler.getCachedAPIKey(), str(input("[i] Please enter a username: ")))
                os.system("pause")
                os.system("cls")
                launcherMenu()
            elif option == 4:
                os.system("cls")
                urlHandler.createCustomSession()
                break
            elif option == 5:
                os.system("cls")
                worldManager.lauchHomeWorld()
                break
            elif option == 6:
                print("\n")
                logManager.logger("Goodbye!", "info")
                print("\n")
                exit()
            elif option == 0:
                os.system("cls")
                displayDebugMenu()
                os.system("cls")
                launcherMenu()
            else:
                print("\n")
                logManager.logger("Invalid option! Please try again. \n", "error")
                print("\n")
                continue
        except ValueError:
            print("\n")
            logManager.logger("Invalid option! Please try again. \n", "error")
            print("\n")
            continue