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
        print("[{}] [ERROR]: {}".format(current_time, message))
    elif message_type == "warning":
        print("[{}] [WARNING]: {}".format(current_time, message))
    elif message_type == "success":
        print("[{}] [SUCCESS]: {}".format(current_time, message))
    elif message_type == "info":
        print("[{}] [INFO]: {}".format(current_time, message))