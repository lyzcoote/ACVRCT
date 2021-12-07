import requests
from requests import api
url = 'https://api.vrchat.cloud/api/1/config'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
result = requests.get(url, headers=headers)
"""Prints the result of the request with the status code and formatted JSON"""
print(result.status_code)
print(result.json())
"""Extract the value called apiKey from the JSON and print it"""
apiKey = result.json()['apiKey']

"""Make a custom API GET Request with a custom header"""
url = 'https://api.vrchat.cloud/api/1/auth/exists?username=lyzcoote'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
 'Cookie': 'apiKey=' + apiKey}
result = requests.get(url, headers=headers)
print(result.status_code)
print(result.json())

"""
url = 'https://api.vrchat.cloud/api/1/users/lyzcoote/name'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
 'Cookie': 'apiKey=' + apiKey}
result = requests.get(url, headers=headers)
print(result.status_code)
print(result.json())
"""

"""Make a custom API GET Request with a custom header and basic HTTP authentication"""
url = 'https://api.vrchat.cloud/api/1/auth'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Cookie': 'apiKey=' + apiKey}
result = requests.get(url, headers=headers, auth=('ExtremistShip', '67PxFs5ls1'))
print(result.status_code)
print(result.content)
authToken = result.json()['token']
print(authToken)

url = 'https://api.vrchat.cloud/api/1/auth/user'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Cookie': 'auth=' + authToken}
result = requests.get(url, headers=headers, auth=('ExtremistShip', '67PxFs5ls1'))
print(result.status_code)
print(result.content)

print("API Key: "+ str(apiKey) + "\n")
print("Auth Token: "+ str(authToken) + "\n")
url = 'https://api.vrchat.cloud/api/1/users/lyzcoote/name'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Cookie': 'apiKey=' + apiKey, 'Cookie': 'auth=' + authToken}
print('URL: ' + str(url) + "\n")
print('Headers: ' + str(headers) + "\n")
result = requests.get(url, headers=headers)
print("Status Code: "+ str(result.status_code))
print(result.content)