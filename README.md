# THIS PROJECT IS DEPRECATED DUE TO VRCHAT API CHANGES!

# Welcome to ACVRCT!

  

Hi! This is ACVRCT (**A**nother **C**ustom **VRC**hat **T**oolkit), a small custom VRChat World and Instance Toolkit made in Python.

  

## Features

These are the main features about ACVRCT:

- Create a Custom Instance:

- Choose a custom World given by a list (user-editable)

- Choose the Instance Type (Public, Friends+, Friends, Invite+ and Invite)

- Choose the Owner of the created instance (If you choose the Instance Type to be anything other than Public)

- Choose the Instance Region (Europe, United States West, United States East and Japan)

- Launch into your Default Home in a Private Session (No Invite)

- See some details about a specific user given his Username

  
  
  

# How does this work?

  

Well, it is both simple and difficult to answer this question, for a few reasons:

- If you want to create a simple Home Instance Launcher, you can basically create a Shortcut to your desktop to the default [VRChat Protocol](vrchat://launch).

- But, if you want to create custom instances, you need to use the [VRChat API](https://vrchatapi.github.io/) and learn about various things, from easy (WorldID, InstanceID, Region, etc..) to kinda difficult at first glance (using both the APIKey and AuthCookie on the same request)

  

But to keep it simple, ACVRCT does a bunch of API requests to the official VRChat APIs for creating a custom URL that will launch you into the custom Instance you created.

> **Note:** The **Friends+, Friends, Private+ and Private** instance types does prompt for an account login.

  

Just to clarify, the account login prompt is needed for converting an username to UserID and other API calls.

As already stated in the ACVRCT prompt:

> Your Username and Password will be sent **only to VRChat API Servers**.

> They won't be sent or saved to the creator of this launcher!

> If you're not sure about logging in with your account, use a burner account or just dont use ACVRCT

  

You can always check the source code to be absolutely sure that your credentials are only sent to VRChat API Servers.

  

# Can I contribue?

  

Yes!

Pull requests or DMs to my [Discord](https://discordapp.com/users/441641373775691778) are welcome.

For major changes, please open an issue first to discuss what you would like to change.

  

Just please make sure your changes/contributions are in line with [VRChat TOS](https://hello.vrchat.com/legal) and [Community Guidelines](https://hello.vrchat.com/community-guidelines)

  

Also, the source code is available to anyone that wants to create their custom launcher or anything else!

  
  

## ToDo

  

There are a few things to do:

- A GUI Version of ACVRCT

- ~~Implement 2FA Account Login~~ (still needs a **ton** of work)

- A World List based on an online MySQL DB (instead of hard-coding the world list)

- Implement Friends+, Friends and Private+ Instace Types correctly

> **Note:** The **Friends+, Friends and Private+** instance types are current disabled due to the lack of time available to the main dev.

- Implement user input check for UNICODE Characters or wrong input

- See current online Friends

- Implement a JSON file to store all of the cachable Cookies

  
  
  

## License

ACVRCT uses the [MIT](https://choosealicense.com/licenses/mit/) license

>**Note:** I am **not responsible** for any damage/malicious use made through the use of my code.

  

>**ACVRCT is not sponsored** by, affiliated with or endorsed by **Unity Technologies, VRChat Inc. or its affiliates**.

"Unity" is a trademark or a [registered trademark](https://unity.com/legal/trademarks) of **Unity Technologies** or its affiliates in the U.S. and elsewhere.

"VRChat Inc." is a trademark or a [registered trademark](https://tmsearch.uspto.gov/bin/showfield?f=doc&state=4802:yugmvk.2.2) of **VRChat Inc. Corporation** or its affiliates in the U.S. and elsewhere.
