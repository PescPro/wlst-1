# go to %JDEV_HOME%\wlserver_10.3\common\bin and start wlst.cmd
# execfile('c:/...../groups_zms.py')
import sys
import traceback
print 'args' + str(sys.argv)
if len(sys.argv) != 4:
  print "Invalid Arguments: " + str(sys.argv)
  print " Usage: groups_zms.py adminuser password adminurl"
  exit()


username=sys.argv[1]
password=sys.argv[2]
url=sys.argv[3]

connect(username,password,url)

serverConfig()
print 'lookup DefaultAuthenticator' 
atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider('DefaultAuthenticator')

# create ADF application groups

ADFgroups=['WFMUsers','WFMAdministrators','WFMManagement']
for group in ADFgroups:
 print 'Creating group ' + group
 try:
   atnr.createGroup(group,group)
 except:
   apply(traceback.print_exception, sys.exc_info())

# create COVOG groups

groups=['G-COVOG-Administratief','G-COVOG-JuniorMedewerker','G-COVOG-Medewerker','G-COVOG-SAMR','G-COVOG-FuncBeheer','G-COVOG-OperManage','WFMAdministrators','WFMUSers']
for group in groups:
 print 'Creating group ' + group
 try:
   atnr.createGroup(group,group)
 except:
   apply(traceback.print_exception, sys.exc_info())

## Add Usergroups(COVOG) to Application groups
print 'Add groups ZMS to COVOG groups'
atnr.addMemberToGroup('WFMUsers','G-COVOG-Administratief')
atnr.addMemberToGroup('WFMUsers','G-COVOG-JuniorMedewerker')
atnr.addMemberToGroup('WFMUsers','G-COVOG-Medewerker')
atnr.addMemberToGroup('WFMUsers','G-COVOG-SAMR')
atnr.addMemberToGroup('WFMAdministrators','G-COVOG-FuncBeheer')
atnr.addMemberToGroup('WFMAdministrators','G-COVOG-OperManage')
atnr.addMemberToGroup('WFMManagement','G-COVOG-OperManage')
  
disconnect()
