import os
import requests
from requests import api
from requests.models import CaseInsensitiveDict
import getpass
import otherUtils as utils
import logManager as logManager
import cookieFileHandler as cookieFileHandler

version = "0.4.1.0Alpha"
authorGitHubUrl = "https://github.com/lyzcoote"

################################################################################
#                                                                              #
#                                    Classes                                   #
#                                                                              #
################################################################################

class APIKeyError(Exception):
    """Returning exception for API key error"""
    pass

class InvalidResponse(Exception):
    """Returning exception for invalid response"""
    pass

################################################################################
#                                                                              #
#                              Constant Variables                              #
#                                                                              #
################################################################################

""" Headers for API requests """
headers = CaseInsensitiveDict()
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"

################################################################################
#                                                                              #
#                                   Functions                                  #
#                                                                              #
################################################################################


def getAPIKey():
    """
        Get API key from VRChat APIs
    """
    print("\n")
    logManager.logger("Getting API key...", "info")
    url = 'https://api.vrchat.cloud/api/1/config'
    try:
        result = requests.get(url, headers=headers)
        if result.status_code == 200:
            if(result.json()['apiKey']) != None:
                os.system('cls')
                apiKey = result.json()['apiKey']
            else:
                raise APIKeyError("[!] API key not found in VRChat APIs")
            return apiKey
        else:
            raise InvalidResponse("\n[!] Invalid response from VRChat APIs\n[!] Status Code: "+ str(result.status_code))
    except requests.exceptions.RequestException as e:
        logManager.logger(str(e), "error")
        return None
        
""" Saving API Key to a variable """        
apiKey = getAPIKey()

def getCachedAPIKey():
    """ 
        Cache API key 
    """
    return apiKey

def getUserInfo(apiKey, username):
    """
        Get user info from VRChat APIs
        Given a username, returns the user info in a dictionary via JSON obtained from the VRChat APIs using the API key and Auth cookie
    """
    if(doesUserExists(username)):
        """
            Checks if the username given by the users exists, if it does, it returns the user info
            Otherwise, it returns None
        """
        os.system('cls')
        print("\n")
        logManager.logger("Getting user info...", "info")

        """Creating headers for the request, including the API key and the Auth cookie"""
        headers["Cookie"] = "apiKey=" + apiKey +str(";")+ "auth=" + getAuthCookie(apiKey)

        url = "https://api.vrchat.cloud/api/1/users/"f"{username}""/name"
        try:
            """Sending the request to the VRChat APIs"""
            result = requests.get(url, headers=headers)

            """Checking if the response code is 200 OK"""
            if result.status_code == 200:
                """Checking if the response is not empty"""
                if(result.json()['username']) != None:
                    """Creating a dictionary with the user info"""
                    userInfo = [
                        result.json()['id'], # User ID | 0
                        result.json()['username'], # Username (used to login) | 1
                        result.json()['displayName'], # Display name (what the other users see) | 2
                        result.json()['last_login'], # Date of the aprox last login | 3
                        result.json()['state'], # State (online/offline/active) | 4
                        result.json()['allowAvatarCopying'], # Allow avatar copying | 5
                        result.json()['date_joined'], # Date of join | 6
                        result.json()['last_platform'], # Last platform used (Windows/Android) | 7
                        result.json()['currentAvatarImageUrl'], # Current avatar image URL | 8
                        result.json()['tags'] # Tags (Ranks and VRC+) | 9
                        ]

                    """Doing some formatting and checks of the previous obtained dictionary"""

                    """Checking the aprox date of the last login"""
                    if(userInfo[3] == ""):
                        userInfo[3] = "Unknown"

                    """Checking the state of the user"""
                    if(userInfo[4] == "online"):
                        userInfo[4] = "Online (VRChat)"
                    elif(userInfo[4] == "offline"):
                        userInfo[4] = "Offline"
                    elif(userInfo[4] == "active"):
                        userInfo[4] = "Online (Non-VRChat)"
                    else:
                        userInfo[4] = "Unknown"

                    """Checking if the user does allow avatar copying"""
                    if(userInfo[5] == True):
                        userInfo[5] = "Yes"
                    elif(userInfo[5] == False):
                        userInfo[5] = "No"
                    else:
                        userInfo[5] = "Unknown"
                    
                    """Checking the user last platform"""
                    if(userInfo[7] == "standalonewindows"):
                        userInfo[7] = "Windows"
                    elif(userInfo[7] == "android"):
                        userInfo[7] = "Quest"
                    
                    os.system('cls')
                    logManager.logger("Loading user info of user: "f"{username}", "info")
                    """Printing the obtained user info"""
                    message = [
                        "[i] User ID: "f"{userInfo[0]}",
                        "[i] Username: "f"{userInfo[1]}", 
                        "[i] Display Name: "f"{userInfo[2]}",
                        "[i] Is Avatar copying enabled?: "f"{userInfo[5]}", 
                        "[i] Last Login: "f"{userInfo[3]}", 
                        "[i] State: "f"{userInfo[4]}",
                        "[i] Date Joined: "f"{userInfo[6]}",
                        "[i] Last Platform: "f"{userInfo[7]}",
                        "[i] Current Avatar Image URL: "f"{userInfo[8]}",
                        "[i] Current User Ranks: "
                        ]

                    """Adding the Rank Tags to the User Info message"""
                    if(userInfo[9]):
                        for tag in userInfo[9]:
                            if(tag == "system_trust_basic"):
                                message.append("    "+"Basic User")
                                message.append("    "+"Can Upload Avatars and Worlds")
                            if(tag == "system_supporter"):
                                message.append("    "+"System Supporter")
                            if(tag == "system_trust_veteran"):
                                message.append("    "+"Veteran User")
                            if(tag == "system_trust_trusted"):
                                message.append("    "+"Trusted User")
                            if(tag == "system_early_adopter"):
                                message.append("    "+"Early Adopter")
                            if(tag == "system_trust_legend"):
                                message.append("    "+"Legend User")
                    """Printing the obtained user info"""            
                    utils.printBox(message)
                    return message
                else:
                    """If the response is empty or smh, it means that the user does not exist or something went wrong"""
                    raise InvalidResponse("\n[!] Invalid response from VRChat APIs\n[!] Status Code: "+ str(result.status_code))
            elif result.status_code == 401:
                """
                    Error response due to missing apiKey or auth cookie.
                """
                logManager.logger("Invalid API key or AuthCookie", "error")
            else:
                """ If response from the API is not 200 or 401 """
                raise InvalidResponse("\n[!] Invalid response from VRChat APIs\n[!] Status Code: "+ str(result.status_code))
        except requests.exceptions.RequestException as e:
            logManager.logger(str(e), "error")
            return None
    else:
        """The user does not exist or the username given by the user is invalid or wrong"""
        return None


def getUserID(apiKey, username):
    """
        Get user ID from VRChat APIs
    """
    logManager.logger("Getting user ID...", "info")

    """Creating headers for the request, including the API key and the Auth cookie"""
    headers["Cookie"] = "apiKey=" + apiKey +str(";")+ "auth=" + getAuthCookie(apiKey)
    url = "https://api.vrchat.cloud/api/1/users/"f"{username}/name"
    try:
        """Sending the request to the VRChat APIs"""
        result = requests.get(url, headers=headers)
        
        """Checking if the response code is 200 OK"""
        if result.status_code == 200:
            """Checking if the response is not empty"""
            if(result.json()['username']) != None:
                """Returning the user ID"""
                userID = result.json()['id']
                return userID
            else:
                """If the response is empty or smh, it means that the user does not exist or something went wrong"""
                raise InvalidResponse("\n[!] Invalid response from VRChat APIs\n[!] Status Code: "+ str(result.status_code))
        elif result.status_code == 401:
            """
                Error response due to missing apiKey or auth cookie.
            """
            logManager.logger("Invalid API key or AuthCookie", "error")
        else:
            """ If response from the API is not 200 or 401"""
            raise InvalidResponse("\n[!] Invalid response from VRChat APIs\n[!] Status Code: "+ str(result.status_code))
    except requests.exceptions.RequestException as e:
        logManager.logger(str(e), "error")
        return None



def doesUserExists(username):
    """"
        Asks for the user to insert the username of the user to check if exists
    """
    logManager.logger("Checking if user exists...", "info")
    url = "https://api.vrchat.cloud/api/1/auth/exists?username="f"{username}"
    try:
        """Sending the request to the VRChat APIs"""
        result = requests.get(url, headers=headers, params={'apiKey': apiKey})
        """Checking if the response code is 200 OK"""
        if result.status_code == 200:
            """Checking if the response is not empty"""
            if(result.json()['userExists']) != False:
                """Printing that the user exists and return True"""
                logManager.logger("User called: '"f"{username}' exists", "success")
                return True
            elif (result.json()['userExists']) == False:
                """Printing that the user does not exists and return False"""
                logManager.logger("User called: '"f"{username}' DOES NOT exists", "error")
                return False
            else:
                """If the response is empty or smh, it means that the user does not exist or something went wrong"""
                raise InvalidResponse("\n[!] Invalid response from VRChat APIs\n[!] Status Code: "+ str(result.status_code))
        elif result.status_code == 400:
            """
                Error response due to missing apiKey or auth cookie.
            """
            logManager.logger("Invalid given username", "error")
        else:
            """ If response from the API is not 200 or 400"""
            raise InvalidResponse("\n[!] Invalid response from VRChat APIs\n[!] Status Code: "+ str(result.status_code))
    except requests.exceptions.RequestException as e:
        logManager.logger(str(e), "error")
        return None

def getAuthCookie(apiKey):
    """
        Get auth cookie from VRChat APIs
    """
    try:
        """Checking if the AuthCookie is already cached in the Cookies file"""
        if(cookieFileHandler.retriveAuthCookieFromFile() != None and cookieFileHandler.retriveAuthCookieFromFile() == False):
            """If the AuthCookie is not cached, send the request to the VRChat APIs"""
            logManager.logger("Auth cookie not found in Cookies file.\nSending API Request...", "info")
            url = 'https://api.vrchat.cloud/api/1/auth'
            try:
                """Setting the headers for the request using only the API key"""
                headers["Cookie"] = "apiKey=" + apiKey
                """Displaying the Login Disclaimer"""
                utils.displayLoginDisclaimer()
                """Asking the user to input the username and password 
                Note: The password is NOT displayed on the console"""
                username = input("[i] Username: ")
                password = getpass.getpass("[i] Password: ")
                if(doesUserExists(username)):
                    """Sending the request to the VRChat APIs if the username exists"""
                    logManager.logger("Sending API Request...", "info")
                    """Sending the request to the VRChat APIs"""
                    result = requests.get(url, headers=headers, auth=(str(username),str(password)))
                    """Collecting the AuthCookie even tho the user can have 2FA enabled, which prevents the API from doing a full request/login"""
                    if result.cookies['auth']:
                        """If the AuthCookie response is not empty, print the result and return it"""
                        logManager.logger("Auth Cookie found!", "success")
                        return result.cookies['auth']
                    """If the users doesn't have 2FA enabled, but a login is successful (Code 200 OK), print the result and return it"""
                    if result.status_code == 200:
                        logManager.logger("Login successful!", "success")    
                    elif result.status_code == 401:
                        """If the response is 401 Unauthorized, print the result and return it"""
                        if (result.json()['error']['message'] == '"Missing Credentials"'):
                            logManager.logger("Missing APIKey or AuthCookie", "error")
                            return None
                    else:
                        """If the response is empty or smh, it means that the user does not exist or something went wrong"""
                        raise InvalidResponse("\n[!] Invalid response from VRChat APIs\n[!] Status Code: "f"{result.status_code}"" \n[!] Content: "f"{result.json()}")
                else:
                    """If the username does not exists, print the username not found error message and return it"""
                    utils.displayUsernameNotFound()
                return None
            except requests.exceptions.RequestException as e:
                logManager.logger(str(e), "error")
                return None
        else:
            """If the AuthCookie is cached, print the result and return it"""
            logManager.logger("Auth cookie found in Cookies file, avoiding API Request.", "info")
            return cookieFileHandler.retriveAuthCookieFromFile()
    except FileNotFoundError:
        """If the Cookies file is not found, print the error message and return None"""
        logManager.logger("Something went wrong while loading the Cookies File!", "error")
        logManager.logger("Error: " + str(e), "error")
        return None

def get2FAAuthCookie(apiKey, authCookie):
    """
        Get 2FA auth cookie from VRChat APIs
    """
    try:
        url = 'https://api.vrchat.cloud/api/1/auth/twofactorauth/totp/verify'

        """Asking the user to input the 2FA code"""
        twoFactorCode = input("[i] Please insert your Two-Factor Code: ")

        """Creating the JSON Data as the request body"""
        jsonData = {"code": ""f"{str(twoFactorCode)}"}

        """Setting the headers for the request using the API key and the AuthCookie and setting the Content-Type to application/json"""
        headers["Content-Type"] = "application/json"
        headers["Cookie"] = "apiKey=" + apiKey +str(";")+ "auth=" + authCookie

        """Sending the request to the VRChat APIs"""
        result = requests.post(url, headers=headers, json=jsonData)

        if result.status_code == 200:
            """If response code is 200 OK, print the result and return it"""
            logManager.logger("[i] Two-Factor Authentication successful!", "success")
            return result.cookies['twoFactorAuth']
        elif result.status_code == 400:
            """If the response code is 400 Bad Request (Incorrect 2FA Code), print the error and and return False"""
            logManager.logger("Invalid Two-Factor Code", "error")
            return False
        elif result.status_code == 401:
            """If the response code is 401 Unauthorized (Invalid APIKey or AuthCookie (Not the 2FA one)), print the error and and return False"""
            logManager.logger("Invalid API Key or Auth Cookie", "error")
            return False
        else:
            """If the response code is empty or smh, it means that the user does not exist or something went wrong"""
            raise InvalidResponse("\n[!] Invalid response from VRChat APIs\n[!] Status Code: "f"{result.status_code} \n[!] Content: "f"{result.json()}")
    except requests.exceptions.RequestException as e:
        logManager.logger(str(e), "error")
        return None
                    
                    
def getWorldNamebyID(worldID):
    """
        Get the world name by world ID
    """
    logManager.logger("Getting world name by world ID...", "info")
    url = "https://api.vrchat.cloud/api/1/worlds/"f"{worldID}"
    try:
        """Sending the request to the VRChat APIs using the standard headers and sending the APIKey as a cookie"""
        result = requests.get(url, headers=headers, params={'apiKey': apiKey})

        if result.status_code == 200:
            """If the response code is 200 OK, print the result and return it"""
            if(result.json()['id']) != None:
                return result.json()['name']
            else:
                raise InvalidResponse("\n[!] Invalid response from VRChat APIs\n[!] Status Code: "f"{result.status_code} \n[!] Content: "f"{result.json()}")
        elif result.status_code == 404:
                logManager.logger("World by ID: '"+ str(worldID) +"' DOES NOT exists", "error")
                return False
        else:
            """If the response code is empty or smh, it means that the user does not exist or something went wrong"""
            raise InvalidResponse("\n[!] Invalid response from VRChat APIs\n[!] Status Code: "+ str(result.status_code))
    except requests.exceptions.RequestException as e:
        logManager.logger(str(e), "error")
        return None

def checkIfAuthCookieIsValid(authCookie):
    """
        Check if the AuthCookie is valid
    """
    url = 'https://api.vrchat.cloud/api/1/auth'
    try:
        """Setting the headers for the request using the AuthCookie"""
        headers["Cookie"] = "auth=" + authCookie
        """Sending the request to the VRChat APIs"""
        result = requests.get(url, headers=headers)
        if result.status_code == 200:
            """If the response code is 200 OK, print the result and return it"""
            if(result.json()['ok']) == True:
                """If the response is True, print the result and return it"""
                logManager.logger("Auth Cookie is valid!", "success")
                return True
            else:
                """If the response is False, print the result and return it"""
                logManager.logger("Auth Cookie is NOT valid!", "warning")
                return False
        elif result.status_code == 401:
            """If the response code is 401 Unauthorized, print the result and return it"""
            if(result.json()['error']['message'] != ''):
                logManager.logger("Error from the API! \nError message: "f"{result.json()}", "error")
                return False
        else:
            """If the response code is empty or smh, it means that the user does not exist or something went wrong"""
            raise InvalidResponse("\n[!] Invalid response from VRChat APIs\n[!] Status Code: "+ str(result.status_code))
    except requests.exceptions.RequestException as e:
        logManager.logger(str(e), "error")
        return None



    




