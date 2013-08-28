#Refactored: Tony

# Set some constants
username='nodemanager'
password='password'


import socket
host = socket.gethostname()
import os
domain = os.getenv('WL_DOMAIN')
wl_home = os.getenv('WL_HOME')
domain_dir= os.getenv('WL_DOMAIN_DIR')
nmPort='5556'


#
# generic code
#

nmhome = wl_home + '/common/nodemanager'
nmpfile = nmhome + '/nodemanager.properties'

#Start the nodemanager
startNodeManager(NodeManagerHome=nmhome,PropertiesFile=nmpfile)

