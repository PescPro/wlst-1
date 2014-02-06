# Who: Tony van Esch
#What: create datasources
#When: friday. Hackday

#Change: Tue Jan 21 09:30:50
#what: replaced + var+ with %s for readability


# to do: abstract SOA part to make it domain generic


import sys
import traceback
from java.io import FileInputStream

# get commandline args
print "Usage crDS_balbla.py adminuser adminpassword env"
print 'args:' + str(sys.argv)
if len(sys.argv) != 5:
  print "ERROR. Invalid Arguments: " + str(sys.argv)
  print " Usage crDS_zms.py adminuser adminpassword env DatasourceName"
  print " env=[dev|tst|acc|prd]"
  print " env-var is used to get $env.properties file"
  exit()

username=sys.argv[1]
password=sys.argv[2]
env=sys.argv[3]
DatasourceName=sys.argv[4]


# setup properties file

propInputStream = FileInputStream(env + ".properties")
configProps = Properties()
configProps.load(propInputStream)


#get env specific props for schema
schemaName=configProps.get('%s.user' %DatasourceName)
DBPassword=configProps.get('%s.Password' %schemaName)
DatabaseServiceName=configProps.get("%s.DatabaseServiceName" %schemaName)
DatabaseHost=configProps.get("%s.DatabaseHost" %schemaName)

Targets=configProps.get("%s.Targets" %DatasourceName)
TargetType=configProps.get("%s.TargetType" %DatasourceName)
GlobalTransactionsProtocol=configProps.get("%s.GlobalTransactionsProtocol" %DatasourceName)

if not DatabaseServiceName:
  print "Something went wrong reading the datasource properties with prefix %s from file %s.properties" %(schemaName,env)
  exit()

print "Settings from properties file"
print "DBService=" + DatabaseServiceName
print "DBHost=" + DatabaseHost
print "Targets=" + Targets
print "TargetType=" + TargetType


#get connect url and connect
DomainURL=configProps.get("SOADomainURL")
connect(username,password,DomainURL)


edit()
startEdit()
try:
  cd('/')
  cmo.createJDBCSystemResource(DatasourceName)

  cd('/JDBCSystemResources/%s/JDBCResource/%s' %(DatasourceName,DatasourceName))
  cmo.setName(DatasourceName)

  cd('/JDBCSystemResources/%s/JDBCResource/%s/JDBCDataSourceParams/%s' %(DatasourceName,DatasourceName,DatasourceName))
  set('JNDINames',jarray.array([String('jdbc/%s' %(DatasourceName))], String))

  cd('/JDBCSystemResources/%s/JDBCResource/%s/JDBCDriverParams/%s' %(DatasourceName,DatasourceName,DatasourceName))

  cmo.setUrl('jdbc:oracle:thin:@(description=(RETRY_COUNT=20)(CONNECT_TIMEOUT=15)(TRANSPORT_CONNECT_TIMEOUT=10)(ADDRESS_LIST=(FAILOVER=on)(ADDRESS=(PROTOCOL=tcp)(HOST=%s)(PORT=1521)(PROTOCOL=tcp)(HOST=%s)(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME=%s)(failover=yes)(FAILOVER_MODE=(TYPE=session)(METHOD=basic)(RETRIES=20)(DELAY=15))))' %(DatabaseHost,DatabaseHost,DatabaseServiceName))
  cmo.setDriverName('oracle.jdbc.OracleDriver')

  cmo.setPassword(DBPassword)

  cd('/JDBCSystemResources/%s/JDBCResource/%s/JDBCConnectionPoolParams/%s' %(DatasourceName,DatasourceName,DatasourceName))
  cmo.setTestTableName('SQL SELECT 1 FROM DUAL\r\n')

  cd('/JDBCSystemResources/%s/JDBCResource/%s/JDBCDriverParams/%s/Properties/%s' %(DatasourceName,DatasourceName,DatasourceName,DatasourceName))
  cmo.createProperty('oracle.jdbc.ReadTimeout')

  cd('/JDBCSystemResources/%s/JDBCResource/%s/JDBCDriverParams/%s/Properties/%s/Properties/oracle.jdbc.ReadTimeout' %(DatasourceName,DatasourceName,DatasourceName,DatasourceName))
  cmo.setValue('10000')

  cd('/JDBCSystemResources/%s/JDBCResource/%s/JDBCDriverParams/%s/Properties/%s' %(DatasourceName,DatasourceName,DatasourceName,DatasourceName))
  cmo.createProperty('user')

  cd('/JDBCSystemResources/%s/JDBCResource/%s/JDBCDriverParams/%s/Properties/%s/Properties/user' %(DatasourceName,DatasourceName,DatasourceName,DatasourceName))
  cmo.setValue(schemaName)

  cd('/JDBCSystemResources/%s/JDBCResource/%s/JDBCDriverParams/%s/Properties/%s' %(DatasourceName,DatasourceName,DatasourceName,DatasourceName))
  cmo.createProperty('oracle.net.CONNECT_TIMEOUT')

  cd('/JDBCSystemResources/%s/JDBCResource/%s/JDBCDriverParams/%s/Properties/%s/Properties/oracle.net.CONNECT_TIMEOUT' %(DatasourceName,DatasourceName,DatasourceName,DatasourceName))
  cmo.setValue('10000')

  cd('/JDBCSystemResources/%s/JDBCResource/%s/JDBCDataSourceParams/%s' %(DatasourceName,DatasourceName,DatasourceName))
  cmo.setGlobalTransactionsProtocol(GlobalTransactionsProtocol)

  cd('/SystemResources/%s' %(DatasourceName))
  set('Targets',jarray.array([ObjectName('com.bea:Name=%s,Type=%s' %(Targets,TargetType))], ObjectName))
  save()
  activate()
except:
  undo(defaultAnswer='y', unactivatedChanges='true')
  stopEdit('y')

disconnect()
exit()

