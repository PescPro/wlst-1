#### Create Nm boot paarameters
####
#### By L.J. van der Starre
#### Y
#
# Set some constants
username='weblogic'
password='WFMJustisa1'

import socket
host = socket.gethostname()
import os
domain = os.getenv('WL_DOMAIN')
domain_dir= os.getenv('WL_DOMAIN_DIR')
nmPort='5556'

url = 't3://' + host + ':6001'

adminServerName = 'AdminServer'
MS1Name = 'soa_server1'
MS2Name = 'bam_server1'


#nmConnect(username, password, host, nmPort, domain, domain_dir, 'plain')
connect(username, password, url)
nmGenBootStartupProps(adminServerName)
nmGenBootStartupProps(MS1Name)
nmGenBootStartupProps(MS2Name)
#nmDisconnect()
disconnect()
