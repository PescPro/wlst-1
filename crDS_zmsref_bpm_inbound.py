# Who: Tony van Esch
#What: create zmsref_bpm_inbound datasource
#
edit()
startEdit()
cd('/')
cmo.createJDBCSystemResource('zmsref_bpm_inbound')

cd('/JDBCSystemResources/zmsref_bpm_inbound/JDBCResource/zmsref_bpm_inbound')
cmo.setName('zmsref_bpm_inbound')

cd('/JDBCSystemResources/zmsref_bpm_inbound/JDBCResource/zmsref_bpm_inbound/JDBCDataSourceParams/zmsref_bpm_inbound')
set('JNDINames',jarray.array([String('jdbc/zmsref_bpm_inbound')], String))

cd('/JDBCSystemResources/zmsref_bpm_inbound/JDBCResource/zmsref_bpm_inbound/JDBCDriverParams/zmsref_bpm_inbound')
## env
cmo.setUrl('jdbc:oracle:thin:@(description=(RETRY_COUNT=20)(CONNECT_TIMEOUT=15)(TRANSPORT_CONNECT_TIMEOUT=10)(ADDRESS_LIST=(FAILOVER=on)(ADDRESS=(PROTOCOL=tcp)(HOST=wfmsoaa-ota.testad.minjus.nl)(PORT=1521)(PROTOCOL=tcp)(HOST=wfmsoaa-ota.testad.minjus.nl)(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME=ZMSA)(failover=yes)(FAILOVER_MODE=(TYPE=session)(METHOD=basic)(RETRIES=20)(DELAY=15))))')
cmo.setDriverName('oracle.jdbc.OracleDriver')

## env
cmo.setPassword('zms_refa')

cd('/JDBCSystemResources/zmsref_bpm_inbound/JDBCResource/zmsref_bpm_inbound/JDBCConnectionPoolParams/zmsref_bpm_inbound')
cmo.setTestTableName('SQL SELECT 1 FROM DUAL\r\n')

cd('/JDBCSystemResources/zmsref_bpm_inbound/JDBCResource/zmsref_bpm_inbound/JDBCDriverParams/zmsref_bpm_inbound/Properties/zmsref_bpm_inbound')
cmo.createProperty('oracle.jdbc.ReadTimeout')

cd('/JDBCSystemResources/zmsref_bpm_inbound/JDBCResource/zmsref_bpm_inbound/JDBCDriverParams/zmsref_bpm_inbound/Properties/zmsref_bpm_inbound/Properties/oracle.jdbc.ReadTimeout')
cmo.setValue('10000')

cd('/JDBCSystemResources/zmsref_bpm_inbound/JDBCResource/zmsref_bpm_inbound/JDBCDriverParams/zmsref_bpm_inbound/Properties/zmsref_bpm_inbound')
cmo.createProperty('user')

cd('/JDBCSystemResources/zmsref_bpm_inbound/JDBCResource/zmsref_bpm_inbound/JDBCDriverParams/zmsref_bpm_inbound/Properties/zmsref_bpm_inbound/Properties/user')
cmo.setValue('zms_ref')

cd('/JDBCSystemResources/zmsref_bpm_inbound/JDBCResource/zmsref_bpm_inbound/JDBCDriverParams/zmsref_bpm_inbound/Properties/zmsref_bpm_inbound')
cmo.createProperty('oracle.net.CONNECT_TIMEOUT')

cd('/JDBCSystemResources/zmsref_bpm_inbound/JDBCResource/zmsref_bpm_inbound/JDBCDriverParams/zmsref_bpm_inbound/Properties/zmsref_bpm_inbound/Properties/oracle.net.CONNECT_TIMEOUT')
cmo.setValue('10000')

cd('/JDBCSystemResources/zmsref_bpm_inbound/JDBCResource/zmsref_bpm_inbound/JDBCDataSourceParams/zmsref_bpm_inbound')
cmo.setGlobalTransactionsProtocol('None')

cd('/SystemResources/zmsref_bpm_inbound')
set('Targets',jarray.array([ObjectName('com.bea:Name=wfmsoa_cluster,Type=Cluster')], ObjectName))
save()
activate()
