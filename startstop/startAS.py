#

# Set some constants
# !!need to remove u/p
username='nodemanager'
password='password'
nmPort='5556'
ASName = 'AdminServer'


import socket
host = socket.gethostname()
import os
domain = os.getenv('WL_DOMAIN')
domain_dir= os.getenv('WL_DOMAIN_DIR')
nmType='ssl' # nmType='plain'

 
nmConnect(username, password, host, nmPort, domain, domain_dir, nmType)
try:
  nmStart(adminServerName)
except:
  pass

nmDisconnect()

