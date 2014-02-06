# Who: Tony van Esch
#What: create ZMS datasources
#


import sys
import traceback
from java.io import FileInputStream

# get commandline args
print "Usage crDS_balbla.py adminuser adminpassword env"
print 'args:' + str(sys.argv)
if len(sys.argv) != 5:
  print "ERROR. Invalid Arguments: " + str(sys.argv)
  print " Usage crDS_balbla.py adminuser adminpassword env"
  print " env=[dev|tst|acc|prd]"
  print " env-var is used to get $env.properties file"
  exit()

username=sys.argv[1]
password=sys.argv[2]
env=sys.argv[3]



# setup properties file

propInputStream = FileInputStream("acc.properties")
configProps = Properties()
configProps.load(propInputStream)

#get connect url and connect
domainURL=configProps.get("domainURL")
connect(username,password,domainURL)


#get env specific props for DS
zmsPassword=configProps.get("zmsPassword")
databaseServiceName=configProps.get("databaseServiceName")
databaseHost=configProps.get("databaseHost")

edit()
startEdit()
cd('/')
cmo.createJDBCSystemResource('zms_fouten')

cd('/JDBCSystemResources/zms_fouten/JDBCResource/zms_fouten')
cmo.setName('zms_fouten')

cd('/JDBCSystemResources/zms_fouten/JDBCResource/zms_fouten/JDBCDataSourceParams/zms_fouten')
set('JNDINames',jarray.array([String('jdbc/zms_fouten')], String))

cd('/JDBCSystemResources/zms_fouten/JDBCResource/zms_fouten/JDBCDriverParams/zms_fouten')

cmo.setUrl('jdbc:oracle:thin:@(description=(RETRY_COUNT=20)(CONNECT_TIMEOUT=15)(TRANSPORT_CONNECT_TIMEOUT=10)(ADDRESS_LIST=(FAILOVER=on)(ADDRESS=(PROTOCOL=tcp)(HOST=' + databaseHost + ')(PORT=1521)(PROTOCOL=tcp)(HOST=' + databaseHost + ')(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME=' + databaseServiceName + ')(failover=yes)(FAILOVER_MODE=(TYPE=session)(METHOD=basic)(RETRIES=20)(DELAY=15))))')
cmo.setDriverName('oracle.jdbc.OracleDriver')

cmo.setPassword(zmsPassword)

cd('/JDBCSystemResources/zms_fouten/JDBCResource/zms_fouten/JDBCConnectionPoolParams/zms_fouten')
cmo.setTestTableName('SQL SELECT 1 FROM DUAL\r\n')

cd('/JDBCSystemResources/zms_fouten/JDBCResource/zms_fouten/JDBCDriverParams/zms_fouten/Properties/zms_fouten')
cmo.createProperty('oracle.jdbc.ReadTimeout')

cd('/JDBCSystemResources/zms_fouten/JDBCResource/zms_fouten/JDBCDriverParams/zms_fouten/Properties/zms_fouten/Properties/oracle.jdbc.ReadTimeout')
cmo.setValue('10000')

cd('/JDBCSystemResources/zms_fouten/JDBCResource/zms_fouten/JDBCDriverParams/zms_fouten/Properties/zms_fouten')
cmo.createProperty('user')

cd('/JDBCSystemResources/zms_fouten/JDBCResource/zms_fouten/JDBCDriverParams/zms_fouten/Properties/zms_fouten/Properties/user')
cmo.setValue('zms')

cd('/JDBCSystemResources/zms_fouten/JDBCResource/zms_fouten/JDBCDriverParams/zms_fouten/Properties/zms_fouten')
cmo.createProperty('oracle.net.CONNECT_TIMEOUT')

cd('/JDBCSystemResources/zms_fouten/JDBCResource/zms_fouten/JDBCDriverParams/zms_fouten/Properties/zms_fouten/Properties/oracle.net.CONNECT_TIMEOUT')
cmo.setValue('10000')

cd('/JDBCSystemResources/zms_fouten/JDBCResource/zms_fouten/JDBCDataSourceParams/zms_fouten')
cmo.setGlobalTransactionsProtocol('None')

cd('/SystemResources/zms_fouten')
set('Targets',jarray.array([ObjectName('com.bea:Name=wfmsoa_cluster,Type=Cluster')], ObjectName))
save()
activate()
