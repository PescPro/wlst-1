#### Created by Michel Schildmeijer

#
# Set some constants

MS1Name = 'soa_server1'
MS2Name = 'bam_server1'
 

# generic code
# Set some constants
from os import getenv
WL_DOMAIN=os.getenv('WL_DOMAIN')
execfile(WL_DOMAIN + '_properties.py')  # load domain specific constants

nmConnect(NMAdminUser, NMAdminUserPW, hostname, nmPort, WL_DOMAIN, WL_DOMAIN_DIR, nmType)

try:
 nmKill(MS1Name)
except:
 pass
try:
 nmKill(MS2Name)
except:
 pass


disconnect()

