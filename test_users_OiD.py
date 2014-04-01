# go to %JDEV_HOME%\wlserver_10.3\common\bin and start wlst.cmd
# execfile('c:/...../users.py')
import sys
import traceback
print 'args' + str(sys.argv)
if len(sys.argv) != 5:
  print "Invalid Arguments: " + str(sys.argv)
  print " Usage createUsersGroups.py adminuser password adminurl defaultpassword"
  print " defaultpassword should be at least 8 characters and contain a number,punctuation mark"
  exit()


username=sys.argv[1]
password=sys.argv[2]
url=sys.argv[3]
standaard_password=sys.argv[4]

connect(username,password,url)

serverConfig()
print 'lookup DefaultAuthenticator' 
atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider('OiDAuthenticator')

## Users

users_admi = ['t_admin1','t_admin2']
users_junior = ['t_jrmed1','t_jrmed2']
users_mdw = ['t_mdw1','t_mdw2']
users_samr = ['t_samr1','t_samr2']
users_fb = ['t_fb1','t_fb2']
users_om = ['t_om1','t_om2']
users_ah = ['t_ah1','t_ah2']
users = users_admi + users_junior + users_mdw + users_samr + users_fb + users_om + users_ah

for user in users:
        try:
		atnr.removeUser(user)
	except:
	  pass
        try:
		atnr.createUser(user,standaard_password,user)
		print 'created user: ',user
	except:
		print 'can not create user: ',user
		apply(traceback.print_exception, sys.exc_info())

# add mebemrs to groups
print 'Add members to groups'

# Administratief
group = 'G-COVOG-Administratief'
if users_admi:
  for user in users_admi:
    print 'Add to group: ',user
    atnr.addMemberToGroup(group,user)
  
## JuniorMedewerker  
group = 'G-COVOG-JuniorMedewerker'
if users_junior:
  for user in users_junior:
    print 'Add to group: ',user
    atnr.addMemberToGroup(group,user)
  
## Medewerker  
group = 'G-COVOG-Medewerker'
if users_mdw:
  for user in users_mdw:
    print 'Add to group: ',user
    atnr.addMemberToGroup(group,user)  

## SAMR  
group = 'G-COVOG-SAMR'
if users_samr:
  for user in users_samr:
    print 'Add to group: ',user
    atnr.addMemberToGroup(group,user)
  
## Functioneel Beheer  
group = 'G-COVOG-FuncBeheer'
if users_fb:
  for user in users_fb:
    print 'Add to group: ',user
    atnr.addMemberToGroup(group,user)  

## Operationeel Management  
group = 'G-COVOG-OperManage'
if users_om:
  for user in users_om:
    print 'Add to group: ',user
    atnr.addMemberToGroup(group,user)    

disconnect()
