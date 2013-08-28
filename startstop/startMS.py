#### Generic Oracle WebLogic 11g Start Script
#

# Set some constants
username='nodemanager'
password='password'
#
import socket
host = socket.gethostname()
import os
domain = os.getenv('WL_DOMAIN')
domain_dir= os.getenv('WL_DOMAIN_DIR')
nmPort='5556'

#
MS1Name = 'soa_server1'
MS2Name = 'bam_server1'
#

nmConnect(username, password, host, nmPort, domain, domain_dir, 'plain')
try:
  nmStart(MS1Name)
except:
  pass

try:
  nmStart(MS2Name)
except:
  pass

nmDisconnect()

