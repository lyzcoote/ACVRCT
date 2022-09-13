################################################################################
#                                                                              #
#                                    Modules                                   #
#                                                                              #
################################################################################

import otherUtils as otherUtils
import logManager as logManager
import sys
import os

################################################################################
#                                                                              #
#                                  Functions                                   #
#                                                                              #
################################################################################

def override_where():
    """ overrides certifi.core.where to return actual location of cacert.pem"""
    return os.path.abspath("cacert.pem")

if hasattr(sys, "frozen"):
    import certifi.core
    os.environ["REQUESTS_CA_BUNDLE"] = override_where()
    certifi.core.where = override_where
    import requests.utils
    import requests.adapters
    requests.utils.DEFAULT_CA_BUNDLE_PATH = override_where()
    requests.adapters.DEFAULT_CA_BUNDLE_PATH = override_where()

################################################################################
#                                                                              #
#                                   Main App                                   #
#                                                                              #
################################################################################

if __name__ == "__main__":
    #sys.tracebacklimit = 0
    sys.argv.pop(0)
    print('Argument List:', str(sys.argv))
    print('Number of arguments:', len(sys.argv), 'arguments.')
    if(len(sys.argv) == 0):
        logManager.logger("Gli argv presenti sono come Dio, non esistono :3", "debug")
        otherUtils.launcherMenu()
    else:
        if(str(sys.argv[0]) == "--debug"):
            otherUtils.displayDebugMenu()
        elif(str(sys.argv[0]) == "--help"):
            logManager.logger("Help message here bruv", "debug")
        else:
            logManager.logger("Option not valid!", "error")

    



    




