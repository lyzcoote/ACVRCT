"""Do a API request to a URL given by the user and print the response."""
def main():
    """Main function."""
    import json
    import requests as reqs

    # Make the HTTP request.
    response = reqs.get('https://vrchat.com/api/1/users/lyzcoote/name')

    # Use the json module to load CKAN's response into a dictionary.
    response_dict = json.loads(response.text)

    for i in response_dict:
        print("key: ", i, "val: ", response_dict[i])

