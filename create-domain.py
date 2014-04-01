import traceback

import os
import java

#=======================================================================================
# Get domain directory
#=======================================================================================
def getDomainDirectory():
    return domainsDirectory + '/' + domainName  

#=======================================================================================
# Get node manager home
#=======================================================================================
def getNmHomeDirectory():
    wlsHome = str(java.lang.System.getProperty('pineapple.weblogic.home.path'))
    return wlsHome + '/common/nodemanager'
        
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
# Set System User
#=======================================================================================
def setSystemUser():
    cd('/')
    sysUser = cd('/Security/%s/User/weblogic' % domainName)
    sysUser.setName(systemUser)
    sysUser.setPassword(systemPassword)

#=======================================================================================
# Configure adm server
#=======================================================================================
def configureAdmServer():
    cd('/')
    cd('Servers/AdminServer')
    set('ListenAddress',adminListenAddress)
    set('ListenPort', adminListenPort)

                
#=======================================================================================
# create managed server
#=======================================================================================
def createManagedServer(serverName, listenAddress, listenPort):
    cd('/')
    server = create(serverName, 'Server')
    server.setListenAddress(listenAddress)
    server.setListenPort(int(listenPort))

#=======================================================================================
# Create Machine
# - creates also node manager for machine
#=======================================================================================
def createMachine(machineName, machineListenAddress):
    cd('/')
    machine = create(machineName, getMachineCreateType())
    cd('/Machine/' + machineName)
    nodeMgr = create(machineName, 'NodeManager')
    nodeMgr.setListenAddress(machineListenAddress)
    nodeMgr.setListenPort(int(nmPort))
    nodeMgr.setDebugEnabled(True)
    nodeMgr.setNodeManagerHome(getNmHomeDirectory())
    return machine

#=======================================================================================
# Map server to machine
#=======================================================================================
def setMachine(machineName, serverName):
    cd('/')
    cd('/Servers/')
    cd(serverName)
    currentServer = cmo;
    cd('/Machine/' + machineName)
    currentServer.setMachine(cmo)

def main():   

    try:
       pineappleModulePath = java.lang.System.getProperty('pineapple.module.path')
       templateFile = str(pineappleModulePath) + '/bin/' + templateName

       # configure domain               
       readTemplate(templateFile)
       domain = create(domainName, 'Domain')
       setSystemUser()    
       domainDirectory = domainsDirectory + '/' + domainName
       setOption('OverwriteDomain', 'true')
                
       # create servers
       createManagedServer('server1',managedServer1_listenAddress,managedServer1_listenPort)
       createManagedServer('server2',managedServer1_listenAddress,managedServer2_listenPort)
                
       # create machine
       createMachine('machine1',adminListenAddress)

       # bind to machine
       setMachine('machine1', adminServerName)
       setMachine('machine1', 'server1')
       setMachine('machine1', 'server2')

       setOption('OverwriteDomain', 'true')
       writeDomain(domainDirectory)
       closeTemplate()

    except:
       dumpStack()

main()
</pre></div><p>The content of the <tt>start-and-configure-admserver.py</tt> script:</p><div class="source"><pre class="prettyprint linenums">
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
</pre></div><p>The content of the <tt>enroll-admserver.py</tt> script:</p><div class="source"><pre class="prettyprint linenums">
import os
import java

#=======================================================================================
# Get WebLogic home
#=======================================================================================        
def getWeblogicHome():
   return str(java.lang.System.getProperty('pineapple.weblogic.home.path'))

   
#=======================================================================================
# Get domain directory
#=======================================================================================
def getDomainDirectory():
    return domainsDirectory + '/' + domainName
        
#=======================================================================================
# Get node manager home
#=======================================================================================
def getNmHomeDirectory():
    return getWeblogicHome() + '/common/nodemanager'

#=======================================================================================
# start and connect to adm server outside node manager process
#=======================================================================================
def startAdmServer():
    url = 't3://' + adminListenAddress + ':' + adminListenPort
    block = 'true'
    timeout = 60000
    startServer(serverName, domainName, url, systemUser, systemPassword, getDomainDirectory(), block, timeout)
    connect(systemUser, systemPassword, url)

def main():   

    try:

        # BUG, if domainName is used then is NONE by the time nmConnect is invoked??
        name=domainName
        domainDirectory=getDomainDirectory() 

        # start amdserver
        startAdmServer()

        # enroll server
        nmEnroll(domainDirectory, getNmHomeDirectory())

        # shutdown adm server outside node manager process
        shutdown()

        # connect to node manager
        nmConnect(nmUserName,nmPassword,adminListenAddress,nmPort,name,domainDirectory)

        # start amdserver in nm process
        nmStart(adminServerName, domainDirectory)

    except:
        dumpStack()

main()
exit()
