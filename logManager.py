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

    current_time = now.strftime("%H:%M:%S")
    if message_type == "error":
        print("["f"{current_time}] [ERROR]: "f"{message}")
    elif message_type == "warning":
        print("["f"{current_time}] [WARNING]: "f"{message}")
    elif message_type == "success":
        print("["f"{current_time}] [SUCCESS]: "f"{message}")
    elif message_type == "info":
        print("["f"{current_time}] [INFO]: "f"{message}")