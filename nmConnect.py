# Set some constants
username='weblogic'
password='WFMJustisa1'
#
import socket
host = socket.gethostname()
import os
domain = os.getenv('WL_DOMAIN')
domain_dir= os.getenv('WL_DOMAIN_DIR')
nmPort='5556'
url = 't3://' + host + ':7001'
#
nmConnect(username, password, host, nmPort, domain, domain_dir, 'plain')

