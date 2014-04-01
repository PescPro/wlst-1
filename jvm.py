# Set some constants
username='weblogic'
password='osbacc@gdi'

import socket
localhost = socket.gethostname()
import os
domain = os.getenv('WL_DOMAIN')
domain_dir= os.getenv('WL_DOMAIN_DIR')
mwHome = os.getenv('MW_HOME')
print mwHome
url = 't3://' + localhost + ':7001'
print url

connect(username, password,url)

def monitorJVMHeapSize():
     connect(username, password, url)
     # alternate connect('user', 'passwd', 'adminurl')
     serverNames = getRunningServerNames()
     domainRuntime()

     print '                TotalJVM  FreeJVM  Used JVM' 
     print '=============================================='
     for name in serverNames:
       try:
        cd("/ServerRuntimes/"+name.getName()+"/JVMRuntime/"+name.getName())
        freejvm = int(get('HeapFreeCurrent'))/(1024*1024)
        totaljvm = int(get('HeapSizeCurrent'))/(1024*1024)
        usedjvm = (totaljvm - freejvm)
        print '%14s  %4d MB   %4d MB   %4d MB ' %  (name.getName(),totaljvm, freejvm, usedjvm)
       except WLSTException,e:
        pass

# This module for managed Servers list
def getRunningServerNames():
     domainConfig()
     return cmo.getServers()
 
if __name__== "main":
     monitorJVMHeapSize()
