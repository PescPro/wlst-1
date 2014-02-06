# Who: Tony van Esch
#What: create zms_audit datasource
#
edit()
startEdit()
cd('/')
cmo.createJDBCSystemResource('zms_audit')

cd('/JDBCSystemResources/zms_audit/JDBCResource/zms_audit')
cmo.setName('zms_audit')

cd('/JDBCSystemResources/zms_audit/JDBCResource/zms_audit/JDBCDataSourceParams/zms_audit')
set('JNDINames',jarray.array([String('jdbc/zms_audit')], String))

cd('/JDBCSystemResources/zms_audit/JDBCResource/zms_audit/JDBCDriverParams/zms_audit')
## env
cmo.setUrl('jdbc:oracle:thin:@(description=(RETRY_COUNT=20)(CONNECT_TIMEOUT=15)(TRANSPORT_CONNECT_TIMEOUT=10)(ADDRESS_LIST=(FAILOVER=on)(ADDRESS=(PROTOCOL=tcp)(HOST=wfmsoaa-ota.testad.minjus.nl)(PORT=1521)(PROTOCOL=tcp)(HOST=wfmsoaa-ota.testad.minjus.nl)(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME=ZMSA)(failover=yes)(FAILOVER_MODE=(TYPE=session)(METHOD=basic)(RETRIES=20)(DELAY=15))))')
cmo.setDriverName('oracle.jdbc.OracleDriver')

## env
cmo.setPassword('zmsa')

cd('/JDBCSystemResources/zms_audit/JDBCResource/zms_audit/JDBCConnectionPoolParams/zms_audit')
cmo.setTestTableName('SQL SELECT 1 FROM DUAL\r\n')

cd('/JDBCSystemResources/zms_audit/JDBCResource/zms_audit/JDBCDriverParams/zms_audit/Properties/zms_audit')
cmo.createProperty('oracle.jdbc.ReadTimeout')

cd('/JDBCSystemResources/zms_audit/JDBCResource/zms_audit/JDBCDriverParams/zms_audit/Properties/zms_audit/Properties/oracle.jdbc.ReadTimeout')
cmo.setValue('10000')

cd('/JDBCSystemResources/zms_audit/JDBCResource/zms_audit/JDBCDriverParams/zms_audit/Properties/zms_audit')
cmo.createProperty('user')

cd('/JDBCSystemResources/zms_audit/JDBCResource/zms_audit/JDBCDriverParams/zms_audit/Properties/zms_audit/Properties/user')
cmo.setValue('zms')

cd('/JDBCSystemResources/zms_audit/JDBCResource/zms_audit/JDBCDriverParams/zms_audit/Properties/zms_audit')
cmo.createProperty('oracle.net.CONNECT_TIMEOUT')

cd('/JDBCSystemResources/zms_audit/JDBCResource/zms_audit/JDBCDriverParams/zms_audit/Properties/zms_audit/Properties/oracle.net.CONNECT_TIMEOUT')
cmo.setValue('10000')

cd('/JDBCSystemResources/zms_audit/JDBCResource/zms_audit/JDBCDataSourceParams/zms_audit')
cmo.setGlobalTransactionsProtocol('None')

cd('/SystemResources/zms_audit')
set('Targets',jarray.array([ObjectName('com.bea:Name=wfmsoa_cluster,Type=Cluster')], ObjectName))
save()
activate()
