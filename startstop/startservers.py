####
# Set some constants

# Set some constants
username='weblogic'
password='password1'

import socket
host = socket.gethostname()
import os
domain = os.getenv('WL_DOMAIN')
domain_dir= os.getenv('WL_DOMAIN_DIR')
nmPort='5556'


MS1Name = 'soa_server2'
MS2Name = 'bam_server2'

nmConnect(username, password, host, nmPort, domain, domain_dir, 'plain')


nmStart(MS1Name)

nmStart(MS2Name)

nmDisconnect()

exit()
