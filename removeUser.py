#
# remove users from domain
# wlst.cmd removeUser.py adminuser password removeUser [adminurl]
# Who: Tony van Esch

import sys
import traceback

# default targetlist
targetList=['gdisx1105:6001','gdisx1105:7001','gdisx1105:16001','gdisx1106:6001','gdisx1106:7001','gdisx1106:16001','gdisx1110:7001','gdisx1112:6001','gdisx1110:16001','gdisx1113:7001','gdisx1115:6001','gdisx1113:16001']

print 'args' + str(sys.argv)
if len(sys.argv) < 4:
  print "Invalid Arguments: " + str(sys.argv)
  print " Usage: wlst.cmd removeUser.py adminuser password removeUser [adminurl]"
  print " If no adminurl is given, the user will be created on a predefined targetlist: " + str(targetList)
  exit()

# explicit url.
if len(sys.argv) == 5:
  targetList=[sys.argv[4]]
  

username=sys.argv[1]
password=sys.argv[2]
user=sys.argv[3]


for target in targetList:

 try:
   connect(username,password,'t3://' + target)
 except:
   print "error connecting to adminserver"
   apply(traceback.print_exception, sys.exc_info())
 try:
   atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider('DefaultAuthenticator')
 except:
   print "Error getting defaultAuthenticator" 
   apply(traceback.print_exception, sys.exc_info())

 try:
   atnr.removeUser(user)
 except:
   print 'Remove user failed. ' + user + '@' + target
   #apply(traceback.print_exception, sys.exc_info())

disconnect()

