################################################################################
#                                                                              #
#                                    Modules                                   #
#                                                                              #
################################################################################

import os
from sqlite3 import enable_shared_cache
import apiHandler as APIHandler
import logManager as logManager
import json

################################################################################
#                                                                              #
#                                   Variables                                  #
#                                                                              #
################################################################################

data = {}
data['cookies'] = []

################################################################################
#                                                                              #
#                                   Functions                                  #
#                                                                              #
################################################################################

def writeAuthCookie(cookieString):
    """
    Write the AuthCookie to the file
    """
    # Setting up the new data to append to existing data
    newData = {
    'name': 'AuthCookie',
    'value': ''f'{cookieString}',
    'description': 'VRChat API Auth Cookie',
    'domain': 'vrchat.com'
    }
    # Checking if the file exists
    if(checkifCookieFileExists() == True):
        if(retriveAuthCookieFromFile() == False):
            with open('cookies.json' ,'r+') as file:
                # First we load existing data into a dict.
                fileData = json.load(file)
                # Join newData with fileData inside cookies
                fileData['cookies'].append(newData)
                # Sets file's current position at offset.
                file.seek(0)
                # convert back to json.
                json.dump(fileData, file, ensure_ascii=False, indent = 4)
    else:
        return False

            

def write2FAAuthCookie(cookieString):
    """
    Write the 2FAAuthCookie to the file
    """
    data['cookies'].append({
    'name': '2FAAuthCookie',
    'value': ''f'{cookieString}',
    'description': 'VRChat API 2FA Auth Cookie',
    'domain': 'vrchat.com'
    })

    with open('cookies.json', 'w') as outfile:
        json.dump(data, outfile)

def checkifCookieFileExists():
    """
    Check if the AuthCookie file exists
    """
    if os.path.isfile('cookies.json'):
        return True
    else:
        return False

def checkifAuthCookieExists():
    """
    Check if the cookie is valid
    """
    if checkifCookieFileExists() == True:
        cookieFile = open('cookies.json', 'r')
        data = json.load(cookieFile)
        if data['cookies'] != []:
            return True
        return None
    else:
        return False

def retriveAuthCookieFromFile():
    """
    Retrive the AuthCookie from the file
    """
    if checkifCookieFileExists() == True:
        cookieFile = open('cookies.json', 'r')
        data = json.load(cookieFile)
        for item in data['cookies']:
            if item['name'] == 'AuthCookie':
                print("FOUND!")
                return item['value']
            else:
                print("Key not found :(")
    else:
        return False


def writeAPIKey(apiKey):
    """
    Writes the APIKey to the file
    """
    data['cookies'].append({
    'name': 'APIKey',
    'value': ''f'{apiKey}',
    'description': 'VRChat API Key',
    'domain': 'vrchat.com'
    })

    with open('cookies.json', 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

def retriveAPIKeyFromFile():
    """
    Retrive the APIKey from the file
    """


def showCookieData():
    if checkifCookieFileExists() == True:
        cookieFile = open('cookies.json', 'r')
        data = json.load(cookieFile)
        cookieJsonData = json.dumps(data)
        print(cookieJsonData)
    else:
        return False

def listCookie():
    if checkifCookieFileExists() == True:
        cookieFile = open('cookies.json', 'r')
        data = json.load(cookieFile)
        for item in data['cookies']:
            print(item)
            if item['name'] == 'AuthCookie':
                print("FOUND!")
                print(item['value'])
            else:
                print("Key not found :(")
    else:
        return False
