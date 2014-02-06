#
# change password of account accross all weblogic domains (or only one domain)
# wlst.cmd passwd.py adminuser password changepwUser newPassword [adminurl]
# Who: Tony van Esch

import sys
import traceback

# default targetlist
targetList=['gdisx1105:6001','gdisx1105:7001','gdisx1105:16001','gdisx1106:6001','gdisx1106:7001','gdisx1106:16001','gdisx1110:7001','gdisx1112:6001','gdisx1110:16001','gdisx1113:7001','gdisx1115:6001','gdisx1113:16001','gdisw0100:7001','gdisw0101:7001','gdisw0099.testad.minjus.nl:7001']

print 'args' + str(sys.argv)
if len(sys.argv) < 5:
  print "Invalid Arguments: " + str(sys.argv)
  print " Usage: wlst.cmd passwd.py adminuser password changepwUser newPassword [adminurl]"
  print " Password should be at least 8 characters and contain a number,punctuation mark"
  print " If no adminurl is given, the password will be reset on a predefined targetlist: " + str(targetList)
  exit()

# explicit url.
if len(sys.argv) == 6:
  targetList=[sys.argv[5]]
  

username=sys.argv[1]
password=sys.argv[2]
user=sys.argv[3]
newpw=sys.argv[4]


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

 ## Users
 try:
   atnr.resetUserPassword(user,newpw)
   print 'Changed password for ',user
 except:
   print 'Change password failed for ' + user + '@' + target
   apply(traceback.print_exception, sys.exc_info())
 
disconnect()

