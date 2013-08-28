#refactored: Tony

username='weblogic'
password='password1'
#

import socket
host = socket.gethostname()
import os
domain = os.getenv('WL_DOMAIN')
domain_dir= os.getenv('WL_DOMAIN_DIR')
nmPort='5556'
#

nmType='plain'
nmConnect(username, password, host, nmPort, domain, domain_dir, nmType)

nm()

exit()

