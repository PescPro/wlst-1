# go to %JDEV_HOME%\wlserver_10.3\common\bin and start wlst.cmd
# execfile('c:/...../createUser.py')
import sys
import traceback
print 'args' + str(sys.argv)
if len(sys.argv) != 6:
  print "Invalid Arguments: " + str(sys.argv)
  print " Usage createUser.py adminuser adminpassword adminurl username password"
  print " password should be at least 8 characters and contain a number,punctuation mark"
  exit()


adminusername=sys.argv[1]
adminpassword=sys.argv[2]
url=sys.argv[3]
username=sys.argv[4]
password=sys.argv[5]

connect(adminusername,adminpassword,url)

serverConfig()
print 'lookup DefaultAuthenticator' 
atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider('DefaultAuthenticator')

try:
  atnr.removeUser(username)
except:
  pass

print 'creating user ', username
try:
  atnr.createUser(username,password,username)
  print 'created user: ',username
except:
  print 'can not create user: ',username
  apply(traceback.print_exception, sys.exc_info())

disconnect()
