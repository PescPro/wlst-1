#

# Set some constants
username='nodemanager'
password='password1'
nmPort='5556'
ASName = 'AdminServer'

#
##
## generic code
#
import socket
host = socket.gethostname()
import os
domain = os.getenv('WL_DOMAIN')
domain_dir= os.getenv('WL_DOMAIN_DIR')
nmType='ssl'
 
nmConnect(username, password, host, nmPort, domain, domain_dir, nmType)

try:
  nmKill(ASName)
except:
  pass

nmDisconnect()

