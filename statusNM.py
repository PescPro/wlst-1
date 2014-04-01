#refactored: Tony

# Set some constants
from os import getenv
WL_DOMAIN=os.getenv('WL_DOMAIN')
execfile(WL_DOMAIN + '_properties.py'  # load domain specific constants

nmConnect(NMAdminUser, NMAdminUserPW, hostname, nmPort, WL_DOMAIN, WL_DOMAIN_DIR, nmType)

nm()

exit()

