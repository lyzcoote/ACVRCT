import os
import requests
from requests import api
from requests.models import CaseInsensitiveDict
import getpass
import otherUtils as utils
import logManager as logManager

version = "0.2.1.1Alpha"
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
    print("\n[i] Getting API key...")
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
        print("[!] Error: " + str(e))
        return None
        
apiKey = getAPIKey()

def getCachedAPIKey():
    return apiKey

def getUserInfo(apiKey, username):
    """
        Get user info from VRChat APIs
    """
    if(doesUserExists(username)):
        print("\n[i] Getting user info...")
        headers["Cookie"] = "apiKey=" + apiKey +str(";")+ "auth=" + getAuthCookie(apiKey)
        url = 'https://api.vrchat.cloud/api/1/users/{}/name'.format(username)
        try:
            result = requests.get(url, headers=headers)
            if result.status_code == 200:
                if(result.json()['username']) != None:
                    userInfo = [result.json()['id'], result.json()['username'], result.json()['displayName'], result.json()['currentAvatarImageUrl'], result.json()['state']]
                    print("[i] Loading {} details...".format(username)+"\n")
                    print("[i] User ID: {}".format(userInfo[0]+"\n"))
                    print("[i] Username: {}".format(userInfo[1]+"\n"))
                    print("[i] Display Name: {}".format(userInfo[2]+"\n"))
                    print("[i] Avatar Image URL: {}".format(userInfo[3]+"\n"))
                    print("[i] State: {}".format(userInfo[4]+"\n"))
                    return userInfo
                else:
                    raise APIKeyError("[!] API key not found in VRChat APIs")
                return userInfo
            else:
                raise InvalidResponse("\n[!] Invalid response from VRChat APIs\n[!] Status Code: "+ str(result.status_code))
        except requests.exceptions.RequestException as e:
            print("[!] Error: " + str(e))
            return None
    else:
        return None


def getUserID(apiKey, username):
    """
        Get user ID from VRChat APIs
    """
    print("\n[i] Getting user info...")
    headers["Cookie"] = "apiKey=" + apiKey +str(";")+ "auth=" + getAuthCookie(apiKey)
    url = 'https://api.vrchat.cloud/api/1/users/{}/name'.format(username)
    try:
        result = requests.get(url, headers=headers)
        if result.status_code == 200:
            if(result.json()['username']) != None:
                userInfo = result.json()['id']
                print("[i] User ID: {}".format(userInfo+"\n"))
                return userInfo
            else:
                raise APIKeyError("[!] API key not found in VRChat APIs")
            return userInfo
        else:
            raise InvalidResponse("\n[!] Invalid response from VRChat APIs\n[!] Status Code: "+ str(result.status_code))
    except requests.exceptions.RequestException as e:
        print("[!] Error: " + str(e))
        return None



def doesUserExists(username):
    """"Asks for the user to insert the username of the user to check if exists"""
    print("\n[i] Checking if user exists...")
    url = 'https://api.vrchat.cloud/api/1/auth/exists?username={}'.format(username)
    try:
        result = requests.get(url, headers=headers, params={'apiKey': apiKey})
        if result.status_code == 200:
            if(result.json()['userExists']) != False:
                print("\n[i] User called: '"+ str(username) +"' DOES exists")
                return str(username)
            else:
                logManager.logger("[!] User called: '"+ str(username) +"' DOES NOT exists\n[!] Exiting...", "error")
                return False
        else:
            raise InvalidResponse("\n[!] Invalid response from VRChat APIs\n[!] Status Code: "+ str(result.status_code))
    except requests.exceptions.RequestException as e:
        print("[!] Error: " + str(e))
        return None


def getAuthCookie(apiKey):
        #Get auth cookie from VRChat APIs
    print("\n[i] Getting auth cookie...")
    url = 'https://api.vrchat.cloud/api/1/auth'
    try:
        headers["Cookie"] = "apiKey=" + apiKey
        message = ["[i] A login is required for getting an Authorization Cookie ",
            "    which is necessary for converting a username into UserID ",
            "" ,
            "[!] DISCLAIMER: ",
            "[!] Your Username and Password will be sent to VRChat API Servers. ",
            "[!] They won't be sent or saved to the creator of this launcher! ",
            "[!] If you're not sure about logging in with your account, use a burner account. ",
            "", 
            "[i] If you want to continue, insert your credentials, otherwise feel free to exit."]
        
        utils.printBox(message)
        username = input("[i] Username: ")
        password = getpass.getpass("[i] Password: ")
        if(doesUserExists(username)):
            print("\n[i] Logging in...")
            result = requests.get(url, headers=headers, auth=(str(username),str(password)))
            if result.status_code == 200:
                if(result.json()['token']) != None:
                    authToken = result.json()['token']
                    print("[i] Auth token: {}".format(authToken))
                    return authToken
                else:
                    raise APIKeyError("[!] API key not found in VRChat APIs")
            elif result.status_code == 401:
                if(result.json()['error']['message'] == '"Requires Two-Factor Authentication"'):
                    # When 2FA code is ready, uncomment this code
                    """message = ["[!] Two-Factor Authentication is enabled on this account. ",
                        "    Please insert your two-factor code to continue."]"""
                    message = ["[!] Two-Factor Authentication is enabled on this account, ",
                        "    but this launcher doesn't support it yet. ",
                        "    If you have a burner/other account, please use it."]
                    os.system('cls')
                    utils.printBox(message)
                elif (result.json()['error']['message'] == '"Invalid Username/Email or Password"'):
                    message = ["[!] Invalid credentials. ", "    Please try again."]
                    os.system('cls')
                    utils.printBox(message)
                    return False
                else:
                    logManager.logger("[!] Error: " + str(result.json()['error']['message']), "error")
                    return False
            else:
                raise InvalidResponse("\n[!] Invalid response from VRChat APIs\n[!] Status Code: "+ str(result.status_code)
                 +"\n[!] Content: "+ str(result.content))
        else:
            message = ["[!] The username you entered does not match any created account, ",
                        "    If you belive that username exits, please try again."]
            os.system('cls')
            utils.printBox(message)
            return False
    except requests.exceptions.RequestException as e:
        print("[!] Error: " + str(e))
        return None


def getWorldNamebyID(worldID):
    print("\n[i] Checking world name...")
    url = 'https://api.vrchat.cloud/api/1/worlds/{}'.format(worldID)
    try:
        result = requests.get(url, headers=headers, params={'apiKey': apiKey})
        if result.status_code == 200:
            if(result.json()['id']) != None:
                return result.json()['name']
            else:
                logManager.logger("[!] World by ID: '"+ str(worldID) +"' DOES NOT exists\n[!] Exiting...", "error")
                return False
        else:
            raise InvalidResponse("\n[!] Invalid response from VRChat APIs\n[!] Status Code: "+ str(result.status_code))
    except requests.exceptions.RequestException as e:
        print("[!] Error: " + str(e))
        return None



    




