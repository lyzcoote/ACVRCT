import requests
from requests import api
from requests.models import CaseInsensitiveDict
import getpass

class APIKeyError(Exception):
    """Returning exception for API key error"""
    pass

class InvalidResponse(Exception):
    """Returning exception for invalid response"""
    pass

"""
    Constant variables
"""
headers = CaseInsensitiveDict()
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"




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


def getAPIKey():
    """
        Get API key from VRChat APIs
    """
    print("\n[i] Getting API key...")
    url = 'https://api.vrchat.cloud/api/1/config'
    try:
        result = requests.get(url, headers=headers)
        if result.status_code == 200:
            """Prints the result of the request with the status code and formatted JSON"""
            print("Status Code from VRChat API Server: "+ str(result.status_code))
            """Extract the value called apiKey from the JSON and print it"""
            if(result.json()['apiKey']) != None:
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
                """Prints the result of the request with the status code and formatted JSON"""
                print("Status Code from VRChat API Server: "+ str(result.status_code))
                """Extract the value called apiKey from the JSON and print it"""
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
        Get user info from VRChat APIs
    """
    if(doesUserExists(username)):
        print("\n[i] Getting user info...")
        headers["Cookie"] = "apiKey=" + apiKey +str(";")+ "auth=" + getAuthCookie(apiKey)
        url = 'https://api.vrchat.cloud/api/1/users/{}/name'.format(username)
        try:
            result = requests.get(url, headers=headers)
            if result.status_code == 200:
                """Prints the result of the request with the status code and formatted JSON"""
                print("Status Code from VRChat API Server: "+ str(result.status_code))
                """Extract the value called apiKey from the JSON and print it"""
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
    else:
        return None


def doesUserExists(username):
    """"Asks for the user to insert the username of the user to check if exists"""
    print("\n[i] Checking if user exists...")
    url = 'https://api.vrchat.cloud/api/1/auth/exists?username={}'.format(username)
    try:
        result = requests.get(url, headers=headers, params={'apiKey': apiKey})
        if result.status_code == 200:
            """Prints the result of the request with the status code and formatted JSON"""
            print("Status Code from VRChat API Server: "+ str(result.status_code))
            """Extract the value called apiKey from the JSON and print it"""
            if(result.json()['userExists']) != False:
                print("\n[i] User called: '"+ str(username) +"' DOES exists")
                return str(username)
            else:
                log_manager("[!] User called: '"+ str(username) +"' DOES NOT exists\n[!] Exiting...", "error")
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
        print("[!] DISCLAIMER:\n[!] Your Username and Password will be sended to VRChat API Servers,\n[!] they won't be send or saved to the creator of this launcher!")
        result = requests.get(url, headers=headers, auth=(str(input("[i] Username: ")), str(getpass.getpass("[i] Password: "))))
        if result.status_code == 200:
            #Prints the result of the request with the status code and formatted JSON
            print("Status Code from VRChat API Server: "+ str(result.status_code))
            #Extract the value called apiKey from the JSON and print it
            if(result.json()['token']) != None:
                authToken = result.json()['token']
                print("[i] Auth token: {}".format(authToken))
                return authToken
            else:
                raise APIKeyError("[!] API key not found in VRChat APIs")
        else:
            raise InvalidResponse("\n[!] Invalid response from VRChat APIs\n[!] Status Code: "+ str(result.status_code) +"\n[!] Content: "+ str(result.content))
    except requests.exceptions.RequestException as e:
        print("[!] Error: " + str(e))
        return None


#getUserInfo(apiKey, "btangent")
#getAuthCookie(str(input("[i] Username: ")), str(input("[i] Password: ")), apiKey)
