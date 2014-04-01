# go to %JDEV_HOME%\wlserver_10.3\common\bin and start wlst.cmd
# execfile('c:/...../createUsersGroups.py')
import sys
import traceback
print 'args' + str(sys.argv)
if len(sys.argv) != 5:
  print "Invalid Arguments: " + str(sys.argv)
  print " Usage createUsersGroups.py adminuser password adminurli defaultpassword"
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

users = ['aabdoel','aboss','akalloe','bbosch','cniet','cvishnu','dbanarsi','dcharan','dpronk','edoes','fbuitela','gbark','iveenstr','alangkru','jkruk','jpater','mroeplal','msinteur','myeung','nabdoelr','nskakni','pbohemen','rbiharie','rklomp','rvreeswi','sbaysalo','sbholana','smulder','ssewgobi','swaart','vchaudro','wbajnath','wburg','ahuldy','dweterin','mwiel']
users_admi = ['akalloe','dbanarsi','dcharan','dpronk','gbark','jpater','nabdoelr','nskakni','sbaysalo','swaart']
users_junior = ['alangkru']
users_mdw = ['fbuitela','myeung','vchaudro']
users_samr = ['aabdoel','aboss','bbosch','cniet','jkruk','mroeplal','msinteur','pbohemen','rbiharie','rvreeswi','sbholana','smulder','ssewgobi','wburg']
users_fb = ['cvishnu','edoes','iveenstr','rklomp','wbajnath']
users_om = ['ahuldy','dweterin','mwiel']

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

## Administratief

# create ADF applicatie groupen

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

# add mebers to groups
print 'Add members to groups'

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

## COVOG groepen toevoegen aan de ADF WFM groepen om in te kunnen loggen in de applicatie
print 'Add groups to ADF WFM groups'
atnr.addMemberToGroup('WFMUsers','G-COVOG-Administratief')
atnr.addMemberToGroup('WFMUsers','G-COVOG-JuniorMedewerker')
atnr.addMemberToGroup('WFMUsers','G-COVOG-Medewerker')
atnr.addMemberToGroup('WFMUsers','G-COVOG-SAMR')
atnr.addMemberToGroup('WFMAdministrators','G-COVOG-FuncBeheer')
atnr.addMemberToGroup('WFMAdministrators','G-COVOG-OperManage')
atnr.addMemberToGroup('WFMManagement','G-COVOG-OperManage')
  
disconnect()
