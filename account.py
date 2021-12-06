# Step 1. We begin with creating a Configuration, which contains the username and password for authentication.
import vrchatapi
from vrchatapi.api import authentication_api, users_api

configuration = vrchatapi.Configuration(
    username = 'ExtremistShip',
    password = '67PxFs5ls1',
)

# Step 2. VRChat consists of several API's (WorldsApi, UsersApi, FilesApi, NotificationsApi, FriendsApi, etc...)
# Here we enter a context of the API Client and instantiate the Authentication API which is required for logging in.

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:

    # Instantiate instances of API classes
    auth_api = authentication_api.AuthenticationApi(api_client)

    try:
        # Step 3. Calling getCurrentUser on Authentication API logs you in if the user isn't already logged in.
        current_user = auth_api.get_current_user()
        print("Logged in as:", current_user.display_name)
    except vrchatapi.ApiException as e:
        print("Exception when calling API: %s\n", e)