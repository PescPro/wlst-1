# Who: Tony van Esch
#What: create datasources
#When: friday. Hackday


# to do: abstract SOA part to make it domain generic


import sys
import traceback
from java.io import FileInputStream

# get commandline args
print "Usage crDS_balbla.py adminuser adminpassword env"
print 'args:' + str(sys.argv)
if len(sys.argv) != 5:
  print "ERROR. Invalid Arguments: " + str(sys.argv)
  print " Usage crDS_zms.py adminuser adminpassword env DatasourceName schemaName"
  print " env=[dev|tst|acc|prd]"
  print " env-var is used to get $env.properties file"
  exit()

username=sys.argv[1]
password=sys.argv[2]
env=sys.argv[3]
DatasourceName=sys.argv[4]
schemaName=sys.argv[5]


# setup properties file

propInputStream = FileInputStream(env + ".properties")
configProps = Properties()
configProps.load(propInputStream)

#get connect url and connect
DomainURL=configProps.get("SOADomainURL")
connect(username,password,DomainURL)


#get env specific props for DS
DBPassword=configProps.get(schemaName + "Password")
DatabaseServiceName=configProps.get(schemaName + "DatabaseServiceName")
DatabaseHost=configProps.get(schemaName + "DatabaseHost")
Targets=configProps.get(schemaName + "Targets")
TargetType=configProps.get(schemaName + "TargetType")

edit()
startEdit()
cd('/')
cmo.createJDBCSystemResource(DatasourceName)

cd('/JDBCSystemResources/' + DatasourceName + '/JDBCResource/'+ DatasourceName)
cmo.setName(DatasourceName)

cd('/JDBCSystemResources/' + DatasourceName + '/JDBCResource/' + DatasourceName + '/JDBCDataSourceParams/' + DatasourceName)
set('JNDINames',jarray.array([String('jdbc/' + DatasourceName)], String))

cd('/JDBCSystemResources/' + DatasourceName + '/JDBCResource/' + DatasourceName + '/JDBCDriverParams/' + DatasourceName)

cmo.setUrl('jdbc:oracle:thin:@(description=(RETRY_COUNT=20)(CONNECT_TIMEOUT=15)(TRANSPORT_CONNECT_TIMEOUT=10)(ADDRESS_LIST=(FAILOVER=on)(ADDRESS=(PROTOCOL=tcp)(HOST=' + databaseHost + ')(PORT=1521)(PROTOCOL=tcp)(HOST=' + databaseHost + ')(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME=' + databaseServiceName + ')(failover=yes)(FAILOVER_MODE=(TYPE=session)(METHOD=basic)(RETRIES=20)(DELAY=15))))')
cmo.setDriverName('oracle.jdbc.OracleDriver')

cmo.setPassword(DBPassword)

cd('/JDBCSystemResources/' + DatasourceName + '/JDBCResource/' + DatasourceName + '/JDBCConnectionPoolParams' + DatasourceName)
cmo.setTestTableName('SQL SELECT 1 FROM DUAL\r\n')

cd('/JDBCSystemResources/' + DatasourceName + '/JDBCResource/' + DatasourceName + '/JDBCDriverParams/' + DatasourceName + '/Properties' + DatasourceName)
cmo.createProperty('oracle.jdbc.ReadTimeout')

cd('/JDBCSystemResources/' + DatasourceName + '/JDBCResource/' + DatasourceName + '/JDBCDriverParams/' + DatasourceName + '/Properties/' + DatasourceName + '/Properties/oracle.jdbc.ReadTimeout')
cmo.setValue('10000')

cd('/JDBCSystemResources/' + DatasourceName + '/JDBCResource/' + DatasourceName + '/JDBCDriverParams/' + DatasourceName + '/Properties' + DatasourceName)
cmo.createProperty('user')

cd('/JDBCSystemResources/' + DatasourceName + '/JDBCResource/' + DatasourceName + '/JDBCDriverParams/' + DatasourceName + '/Properties/' + DatasourceName + '/Properties/user')
cmo.setValue('zms')

cd('/JDBCSystemResources/' + DatasourceName + '/JDBCResource/' + DatasourceName + '/JDBCDriverParams/' + DatasourceName + '/Properties' + DatasourceName)
cmo.createProperty('oracle.net.CONNECT_TIMEOUT')

cd('/JDBCSystemResources/' + DatasourceName + '/JDBCResource/' + DatasourceName + '/JDBCDriverParams/' + DatasourceName + '/Properties/' + DatasourceName + '/Properties/oracle.net.CONNECT_TIMEOUT')
cmo.setValue('10000')

cd('/JDBCSystemResources/' + DatasourceName + '/JDBCResource/' + DatasourceName + '/JDBCDataSourceParams' + DatasourceName)
cmo.setGlobalTransactionsProtocol('None')

cd('/SystemResources' + DatasourceName)
set('Targets',jarray.array([ObjectName('com.bea:Name=' + Targets + ',Type=' + TargetType )], ObjectName))
save()
activate()
