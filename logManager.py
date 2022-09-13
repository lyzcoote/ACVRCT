from colorama import init, Fore, Back, Style

# Initializes Colorama
init(autoreset=True)


################################################################################
#                                                                              #
#                                   Functions                                  #
#                                                                              #
################################################################################

def logger(message, message_type):
    """
    Return a message with a message type and time
    """
    from datetime import datetime
    now = datetime.now()

    """Gets the current time"""
    current_time = now.strftime("%H:%M:%S")
    
    if message_type == "error":
        print(Style.BRIGHT + Fore.RED + "["f"{current_time}] [ ERROR ] "f"{message}")
    elif message_type == "warning":
        print(Style.BRIGHT + Fore.YELLOW + "["f"{current_time}] [WARNING] "f"{message}")
    elif message_type == "success":
        print(Style.BRIGHT + Fore.GREEN + "["f"{current_time}] [SUCCESS] "f"{message}")
    elif message_type == "info":
        print(Style.BRIGHT + Fore.CYAN + "["f"{current_time}] [ INFOR ] "f"{message}")
    elif message_type == "debug":
        print(Style.BRIGHT + Fore.MAGENTA + "["f"{current_time}] [ DEBUG ] "f"{message}")