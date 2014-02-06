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
atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider('DefaultAuthenticator')

## Users

users = ['swaart','dbanarsi','akalloe','wbajnath','dweterin','tfromber']
users_admi = ['swaart','dbanarsi','akalloe']
users_junior = ['tfromber']
#users_mdw = ['dummy']
#users_samr = ['dummy']
users_fb = ['wbajnath']
users_om = ['dweterin']

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
for user in users_admi:
  print 'Add to group: ',user
  atnr.addMemberToGroup(group,user)
  
## JuniorMedewerker  
group = 'G-COVOG-JuniorMedewerker'
for user in users_junior:
  print 'Add to group: ',user
  atnr.addMemberToGroup(group,user)
  
## Medewerker  
group = 'G-COVOG-Medewerker'
for user in users_mdw:
  print 'Add to group: ',user
  atnr.addMemberToGroup(group,user)  

## SAMR  
group = 'G-COVOG-SAMR'
for user in users_samr:
  print 'Add to group: ',user
  atnr.addMemberToGroup(group,user)
  
## Functioneel Beheer  
group = 'G-COVOG-FuncBeheer'
for user in users_fb:
  print 'Add to group: ',user
  atnr.addMemberToGroup(group,user)  

## Operationeel Management  
group = 'G-COVOG-OperManage'
for user in users_om:
  print 'Add to group: ',user
  atnr.addMemberToGroup(group,user)    

disconnect()
