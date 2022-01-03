################################################################################
#                                                                              #
#                                    Modules                                   #
#                                                                              #
################################################################################

import otherUtils as otherUtils
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
    sys.tracebacklimit = 0
    otherUtils.launcherMenu()

    




