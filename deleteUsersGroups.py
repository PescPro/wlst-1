# go to %JDEV_HOME%\wlserver_10.3\common\bin and start wlst.cmd
# execfile('c:/...../createUsersGroups.py')



WL_DOMAIN=os.getenv('WL_DOMAIN')
execfile(WL_DOMAIN + '_properties.py')  # load domain specific constants


import sys
import traceback
print 'args' + str(sys.argv)
if len(sys.argv) != 4:
  print "Invalid Arguments: " + str(sys.argv)
  print " Usage deleteUsersGroups.py adminuser password adminurl"
  exit()


username=sys.argv[1]
password=sys.argv[2]
url=sys.argv[3]
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
		print 'can not delete user: ',user
		apply(traceback.print_exception, sys.exc_info())

## Administratief

# create ADF applicatie groupen

ADFgroups=['WFMUsers','WFMAdministrators','WFMManagement']
COVOGGroups=['G-COVOG-Administratief','G-COVOG-AfdHoofd','G-COVOG-FuncBeheer','G-COVOG-JuniorMedewerker','G-COVOG-Medewerker','G-COVOG-OperManage','G-COVOG-SAMR']
for group in ADFgroups:
 print 'Deleting group ' + group
 try:
   atnr.removeGroup(group)
 except:
   print 'Failed to remove group'
   apply(traceback.print_exception, sys.exc_info())

  
for group in COVOGGroups:
 print 'Deleting group ' + group
 try:
   atnr.removeGroup(group)
 except:
   print 'Failed to remove group'
   apply(traceback.print_exception, sys.exc_info())

disconnect()
