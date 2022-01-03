################################################################################
#                                                                              #
#                                    Modules                                   #
#                                                                              #
################################################################################

import os
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
    Write the cookie to the file
    """
    data['cookies'].append({
    'name': 'AuthCookie',
    'value': ''f'{cookieString}',
    'description': 'VRChat API Auth Cookie',
    'domain': 'vrchat.com'
    })

    with open('cookies.json', 'w') as outfile:
        json.dump(data, outfile)

def write2FAAuthCookie(cookieString):
    """
    Write the cookie to the file
    """
    data['cookies'].append({
    'name': '2FAAuthCookie',
    'value': ''f'{cookieString}',
    'description': 'VRChat API 2FA Auth Cookie',
    'domain': 'vrchat.com'
    })

    with open('cookies.json', 'w') as outfile:
        json.dump(data, outfile)

def checkifAuthCookieFileExists():
    """
    Check if the cookie file exists
    """
    if os.path.isfile('cookies.json'):
        return True
    else:
        return False

def checkifAuthCookieExists():
    """
    Check if the cookie is valid
    """
    if checkifAuthCookieFileExists():
        cookieFile = open('cookies.json', 'r')
        data = json.load(cookieFile)
        if data['cookies'] != []:
            return True
        return False

def retriveAuthCookieFromFile():
    if checkifAuthCookieFileExists():
        cookieFile = open('cookies.json', 'r')
        data = json.load(cookieFile)
        if data['cookies'] != []:
            authCookie = data['cookies'][0]['value']
            return authCookie
        return False

    