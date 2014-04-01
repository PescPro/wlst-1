
# Set some constants
from os import getenv
WL_DOMAIN=os.getenv('WL_DOMAIN')
execfile(WL_DOMAIN + '_properties.py')  # load domain specific constants

try:
  connect(AdminUser,AdminUserPW,AdminServerUrl)
  for cluster in Clusters:
    try:
      print "Starting Cluster %s" %cluster
      start(cluster,'Cluster',block="true")
    except:
      print " ERROR: Starting cluster %s failed" %cluster
except:
  print "ERROR: connecting to %s failed" %AdminServerUrl

