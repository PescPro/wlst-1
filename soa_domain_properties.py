AdminServerHost='gdisx1110'
AdminServerListenPort='7001'
AdminServerName='AdminServer'
AdminUser='weblogic'
AdminUserPW='geheim'
OiDAccount='cn=orcladmin,cn=Users, dc=gdi,dc=minvenj,dc=nl'
OiDAccountPW='geheim'
# needed for initial serverStart
jvmProps='-XX:MaxPermSize=150m,-Xmx512m'

AdminServerUrl='t3://'+AdminServerHost+':'+AdminServerListenPort


# add some env-vars
from socket import gethostname
hostname = gethostname()

from os import getenv
ORACLE_BASE=getenv ('ORACLE_BASE')
WL_DOMAIN=getenv ('WL_DOMAIN')
WL_DOMAIN_DIR= ORACLE_BASE+'/domains/'+WL_DOMAIN
DOMAIN_HOME=WL_DOMAIN_DIR #set in WL_DOMAIN_DIR/startWeblogic.sh
MW_HOME= getenv ('MW_HOME')
WL_HOME= getenv ('WL_HOME')

# SOA props

Machines=[AdminServerHost]+["gdisx1111"]

SOACluster=["wfmsoa_cluster"]
BAMCluster=["wfmbam_cluster"]
Clusters=BAMCluster + SOACluster


#get env specific props for NM

NMAdminUser=AdminUser #NodeManager gets same credentials as wls domain
NMAdminUserPW=AdminUserPW #NodeManager gets same credentials as wls domain

NM_HOME = WL_HOME + '/common/nodemanager'
NM_PROPFILE =  NM_HOME + '/nodemanager.properties'

# setup nodemanager properties file
from java.io import FileInputStream
propInputStream = FileInputStream(WL_HOME + "/common/nodemanager/nodemanager.properties")
configProps = Properties()
configProps.load(propInputStream)

#get env specific props for NM
nmPort=configProps.get('ListenPort')
SSL=configProps.get('SecureListener').lower()

if SSL == 'false':
    nmType='plain'
else:
    nmType='ssl'

