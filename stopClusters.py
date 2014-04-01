

# Set some constants
from os import getenv
WL_DOMAIN=os.getenv('WL_DOMAIN')
execfile(WL_DOMAIN + '_properties.py')  # load domain specific constants


try: 
  connect(AdminUser,AdminUserPW,AdminServerUrl)
  for cluster in Clusters:
    try:
      print "Shutting down Cluster %s" %cluster
      shutdown(cluster,'Cluster',ignoreSessions="true",timeOut=20000,force="true",block="true")
    except:
      print " ERROR: Shutting down cluster %s failed" %cluster
except:
  print " AdminServer not running @ %s ?" %AdminServerUrl

