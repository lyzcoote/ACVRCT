import requests
from requests import api
from requests.models import CaseInsensitiveDict

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
authToken = "authcookie_95026c0c-0c80-4cea-ac49-a05de84bce33" #result.json()['token']



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
        
        
def getUserInfo(apiKey, username):
    """
        Get user info from VRChat APIs
    """
    if(doesUserExists(username, apiKey)):
        print("\n[i] Getting user info...")
        headers["Cookie"] = "apiKey=" + apiKey +str(";")+ "auth=" + authToken
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




def doesUserExists(username, apiKey):
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
                userExistsData = result.json()['userExists']
                return userExistsData
            else:
                log_manager("[!] User called: '"+ str(username) +"' DOES NOT exists\n[!] Exiting...", "error")
                return False
        else:
            raise InvalidResponse("\n[!] Invalid response from VRChat APIs\n[!] Status Code: "+ str(result.status_code))
    except requests.exceptions.RequestException as e:
        print("[!] Error: " + str(e))
        return None


getUserInfo(getAPIKey(), "btangentndjsndjs")

"""url = 'https://api.vrchat.cloud/api/1/auth/exists?username={}'.format(username)
    headers["Cookie"] = "apiKey=" + apiKey
    result = requests.get(url, headers=headers)
    print(result.status_code)
    print(result.json())    


url = 'https://api.vrchat.cloud/api/1/users/lyzcoote/name'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
 'Cookie': 'apiKey=' + apiKey}
result = requests.get(url, headers=headers)
print(result.status_code)
print(result.json())

#Make a custom API GET Request with a custom header and basic HTTP authentication
url = 'https://api.vrchat.cloud/api/1/auth'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Cookie': 'apiKey=' + getAPIKey()}
result = requests.get(url, headers=headers, auth=('ExtremistShip', '67PxFs5ls1'))
print(result.status_code)
print(result.content)
authToken = "authcookie_95026c0c-0c80-4cea-ac49-a05de84bce33" #result.json()['token']
print(authToken)

url = 'https://api.vrchat.cloud/api/1/auth/user'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Cookie': 'auth=' + authToken}
result = requests.get(url, headers=headers, auth=('ExtremistShip', '67PxFs5ls1'))
print(result.status_code)
print(result.content)

print("API Key: "+ str(getAPIKey()) + "\n")
print("Auth Token: "+ str(authToken) + "\n")
url = 'https://api.vrchat.cloud/api/1/users/lyzcoote/name'
headers["Cookie"] = "apiKey=" + getAPIKey() +str(";")+ "auth=" + authToken
print('URL: ' + str(url) + "\n")
print('Headers: ' + str(headers) + "\n")
result = requests.get(url, headers=headers)
print("Status Code: "+ str(result.status_code))
print(result.content)
userID = result.json()['id']
userUsername = result.json()['username']
userDisplayName = result.json()['displayName']
userState = result.json()['state']

print("User found! Logging information...\n")
print("User ID: "+ str(userID) + "\n")
print("User Username: "+ str(userUsername) + "\n")
print("User Display Name: "+ str(userDisplayName) + "\n")
print("User State: "+ str(userState) + "\n")



"""
