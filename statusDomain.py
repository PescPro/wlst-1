
# Set some constants
from os import getenv
WL_DOMAIN=os.getenv('WL_DOMAIN')
execfile(WL_DOMAIN + '_properties.py')  # load domain specific constants
try:
  print "Connecting to %s" %AdminServerName
  connect(AdminUser,AdminUserPW,AdminServerUrl)
  for cluster in Clusters:
    try:
      print "Checking state of Cluster %s" %cluster
      state(cluster,'Cluster',block="true")
    except:
      print " ERROR: Checking cluster %s failed" %cluster
except:
  print "ERROR: %s not running @ %s !" %(AdminServerName,AdminServerUrl)

