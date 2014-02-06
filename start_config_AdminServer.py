import os
import java
 
#=======================================================================================
# Get domain directory
#=======================================================================================
def getDomainDirectory():
	return domainsDirectory + '/' + domainName
 
#=======================================================================================
# Return which type of machine should be created
#=======================================================================================
def getMachineCreateType():
	# On Unix, machine type is 'UnixMachine' on Windows it is 'Machine'
	if os.pathsep == ':':
		return 'UnixMachine'
	else:
		return 'Machine'
 
#=======================================================================================
# Get node manager home
#=======================================================================================
def getNmHomeDirectory():
	wlsHome = str(java.lang.System.getProperty('pineapple.weblogic.home.path'))
	return wlsHome + '/common/nodemanager'
 
#=======================================================================================
# start and connect to adm server outside node manager process
#=======================================================================================
def startAdmServer():
	url = 't3://' + adminListenAddress + ':' + adminListenPort
	block = 'true'
	timeout = 60000
	startServer(serverName, domainName, url, systemUser, systemPassword, getDomainDirectory(), block, timeout)
	connect(systemUser, systemPassword, url)
 
#=======================================================================================
# shutdown adm server outside node manager process
#=======================================================================================
def shutdownAdmServer():
	shutdown()
 
#=======================================================================================
# Configure node manager security
#=======================================================================================
def configureNodeManagerSecurity():
	cd('/')
	securityConfiguration = getMBean('/SecurityConfiguration/' + domainName)
	if securityConfiguration == None:
		securityConfiguration = create(domainName, 'SecurityConfiguration')
		cd('/SecurityConfiguration/' + domainName)
		cmo.setNodeManagerUsername(nmUserName)
		cmo.setNodeManagerPassword(nmPassword)
 
def main():
 
	try:
		startAdmServer()
		 
		# set online edit mode
		edit()
		startEdit()
		# configure node manager
		configureNodeManagerSecurity()
		 
		#store wlst online change
		showChanges()
		save()
		activate(block='true')
		 
		# shutdown admserver
		shutdownAdmServer()
		 
	except:
		dumpStack()
 
main()