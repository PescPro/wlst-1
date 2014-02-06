# Who: Tony van Esch
#What: create zms_adf datasource
#
edit()
startEdit()
cd('/')
cmo.createJDBCSystemResource('zms_adf')

cd('/JDBCSystemResources/zms_adf/JDBCResource/zms_adf')
cmo.setName('zms_adf')

cd('/JDBCSystemResources/zms_adf/JDBCResource/zms_adf/JDBCDataSourceParams/zms_adf')
set('JNDINames',jarray.array([String('jdbc/zms_adf')], String))

cd('/JDBCSystemResources/zms_adf/JDBCResource/zms_adf/JDBCDriverParams/zms_adf')
## env
cmo.setUrl('jdbc:oracle:thin:@(description=(RETRY_COUNT=20)(CONNECT_TIMEOUT=15)(TRANSPORT_CONNECT_TIMEOUT=10)(ADDRESS_LIST=(FAILOVER=on)(ADDRESS=(PROTOCOL=tcp)(HOST=wfmsoaa-ota.testad.minjus.nl)(PORT=1521)(PROTOCOL=tcp)(HOST=wfmsoaa-ota.testad.minjus.nl)(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME=ZMSA)(failover=yes)(FAILOVER_MODE=(TYPE=session)(METHOD=basic)(RETRIES=20)(DELAY=15))))')
cmo.setDriverName('oracle.jdbc.OracleDriver')

## env
cmo.setPassword('zmsa')

cd('/JDBCSystemResources/zms_adf/JDBCResource/zms_adf/JDBCConnectionPoolParams/zms_adf')
cmo.setTestTableName('SQL SELECT 1 FROM DUAL\r\n')

cd('/JDBCSystemResources/zms_adf/JDBCResource/zms_adf/JDBCDriverParams/zms_adf/Properties/zms_adf')
cmo.createProperty('oracle.jdbc.ReadTimeout')

cd('/JDBCSystemResources/zms_adf/JDBCResource/zms_adf/JDBCDriverParams/zms_adf/Properties/zms_adf/Properties/oracle.jdbc.ReadTimeout')
cmo.setValue('10000')

cd('/JDBCSystemResources/zms_adf/JDBCResource/zms_adf/JDBCDriverParams/zms_adf/Properties/zms_adf')
cmo.createProperty('user')

cd('/JDBCSystemResources/zms_adf/JDBCResource/zms_adf/JDBCDriverParams/zms_adf/Properties/zms_adf/Properties/user')
cmo.setValue('zms')

cd('/JDBCSystemResources/zms_adf/JDBCResource/zms_adf/JDBCDriverParams/zms_adf/Properties/zms_adf')
cmo.createProperty('oracle.net.CONNECT_TIMEOUT')

cd('/JDBCSystemResources/zms_adf/JDBCResource/zms_adf/JDBCDriverParams/zms_adf/Properties/zms_adf/Properties/oracle.net.CONNECT_TIMEOUT')
cmo.setValue('10000')

cd('/JDBCSystemResources/zms_adf/JDBCResource/zms_adf/JDBCDataSourceParams/zms_adf')
cmo.setGlobalTransactionsProtocol('None')

cd('/SystemResources/zms_adf')
set('Targets',jarray.array([ObjectName('com.bea:Name=wfmsoa_cluster,Type=Cluster')], ObjectName))
save()
activate()
