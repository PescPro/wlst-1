#### Create Nm boot paarameters
####
#### By L.J. van der Starre
#### Y
#
# Set some constants
username='weblogic'
password='osbo@justis'

import socket
host = socket.gethostname()
import os
domain = os.getenv('WL_DOMAIN')
domain_dir= os.getenv('WL_DOMAIN_DIR')
nmPort='5558'

url = 't3://' + host + ':6001'

adminServerName = 'AdminServer'
osbServer1Name = 'osb_server1'
osbServer2Name = 'osb_server2'


#nmConnect(username, password, host, nmPort, domain, domain_dir, 'plain')
connect(username, password, url)
nmGenBootStartupProps(adminServerName)
nmGenBootStartupProps(osbServer1Name)
nmGenBootStartupProps(osbServer2Name)
#nmDisconnect()
disconnect()
