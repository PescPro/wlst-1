#############################################################################
#
# @author Copyright (c) 2010 - 2011 by Middleware Magic, All Rights Reserved.
#
#############################################################################

from java.io import FileInputStream
from weblogic.management.security.authentication import UserReaderMBean

print 'args' + str(sys.argv)
if len(sys.argv) < 3:
  print "Invalid Arguments: " + str(sys.argv)
  print " Usage listUsers.py adminuser password adminURL env [ont|tst|acc|prd]"
  print " env is used to parse correct properties file: acc.properties"
  exit()

  
username=sys.argv[1]
password=sys.argv[2]
adminURL=sys.argv[3]
env=sys.argv[4]


propInputStream = FileInputStream(env + ".properties")
configProps = Properties()
configProps.load(propInputStream)

#adminURL=configProps.get("SOADomainURL")
#adminUserName=configProps.get("admin.userName")
#adminPassword=configProps.get("admin.password")
#userNameWildcard=configProps.get("user.name.wildcard")
#maximumToReturn=configProps.get("maximum.to.return")
#showAllAuthenticatorUserList=configProps.get("show.all.authenticator.userlist")
showAllAuthenticatorUserList=false


connect(username, password, adminURL)

realmName=cmo.getSecurityConfiguration().getDefaultRealm()
authProvider = realmName.getAuthenticationProviders()

for i in authProvider:
	if isinstance(i,UserReaderMBean):
		userName = i
		authName= i.getName()

		if showAllAuthenticatorUserList == 'true':
			userList = i.listUsers('*',0)
			print '======================================================================'
			print 'Below are the List of USERS which are in the: "'+authName+'"'
			print '======================================================================'
			num=1
			while userName.haveCurrent(userList):
				print userName.getCurrentName(userList)
				userName.advance(userList)
				num=num+1
			print '======================================================================'
			userName.close(userList)

		else:
			if authName == 'DefaultAuthenticator':
#				userList = i.listUsers(str(userNameWildcard),int(maximumToReturn))
				userList = i.listUsers('*',0)
				print userList
				print '======================================================================'
				print 'Below are the List of USERS which are in the: "'+authName+'"'
				print '======================================================================'
				num=1
				while userName.haveCurrent(userList):
					print userName.getCurrentName(userList)
					userName.advance(userList)
					num=num+1
				print '======================================================================'
				userName.close(userList)
