# go to %JDEV_HOME%\wlserver_10.3\common\bin and start wlst.cmd
# execfile('c:/...../linkGroup.py')
import sys
import traceback
print 'args' + str(sys.argv)
if len(sys.argv) != 6:
  print "Invalid Arguments: " + str(sys.argv)
  print " Usage linkGroup.py adminuser password adminurl username group"
  exit()


adminusername=sys.argv[1]
adminpassword=sys.argv[2]
url=sys.argv[3]
username=sys.argv[4]
group=sys.argv[5]

connect(adminusername,adminpassword,url)

serverConfig()
print 'lookup DefaultAuthenticator' 
atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider('DefaultAuthenticator')

  print 'Add ' + username + ' to group ' + group
  atnr.addMemberToGroup(group,user)
  
disconnect()
