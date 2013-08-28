

#
# Set some constants
username='nodemanager'
password='password1'
#
import socket
host = socket.gethostname()
import os
domain = os.getenv('WL_DOMAIN')
domain_dir= os.getenv('WL_DOMAIN_DIR')
wl_home = os.getenv('WL_HOME')
nmPort='5556'

MS1Name = 'soa_server1'
MS2Name = 'bam_server1'
 

nmhome = wl_home + '/common/nodemanager'
nmpfile = nmhome + '/nodemanager.properties'
nmType='plain'

#
#
nmConnect(username, password, host, nmPort, domain, domain_dir, nmType)

try:
 nmKill(MS1Name)
except:
 pass
try:
 nmKill(MS2Name)
except:
 pass

disconnect()

