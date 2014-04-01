#Refactored: Tony

# Set some constants
from os import getenv
WL_DOMAIN=os.getenv('WL_DOMAIN')
execfile(WL_DOMAIN + '_properties.py')  # load domain specific constants

#
# generic code
#

#Start the nodemanager
startNodeManager(NodeManagerHome=NM_HOME,PropertiesFile=NM_PROPFILE)

