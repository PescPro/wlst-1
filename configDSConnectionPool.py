edit()
startEdit()
cd('/JDBCSystemResources/zms_adf/JDBCResource/zms_adf/JDBCDriverParams/zms_adf/Properties/zms_adf')
cmo.destroyProperty(getMBean('/JDBCSystemResources/zms_adf/JDBCResource/zms_adf/JDBCDriverParams/zms_adf/Properties/zms_adf/Properties/oracle.jdbc.ReadTimeout'))
cmo.destroyProperty(getMBean('/JDBCSystemResources/zms_adf/JDBCResource/zms_adf/JDBCDriverParams/zms_adf/Properties/zms_adf/Properties/user'))
cmo.destroyProperty(getMBean('/JDBCSystemResources/zms_adf/JDBCResource/zms_adf/JDBCDriverParams/zms_adf/Properties/zms_adf/Properties/oracle.net.CONNECT_TIMEOUT'))
cmo.createProperty('oracle.jdbc.ReadTimeout')

cd('/JDBCSystemResources/zms_adf/JDBCResource/zms_adf/JDBCDriverParams/zms_adf/Properties/zms_adf/Properties/oracle.jdbc.ReadTimeout')
cmo.setValue('60000')

cd('/JDBCSystemResources/zms_adf/JDBCResource/zms_adf/JDBCDriverParams/zms_adf/Properties/zms_adf')
cmo.createProperty('user')

cd('/JDBCSystemResources/zms_adf/JDBCResource/zms_adf/JDBCDriverParams/zms_adf/Properties/zms_adf/Properties/user')
cmo.setValue('zms')

cd('/JDBCSystemResources/zms_adf/JDBCResource/zms_adf/JDBCDriverParams/zms_adf/Properties/zms_adf')
cmo.createProperty('oracle.net.CONNECT_TIMEOUT')

cd('/JDBCSystemResources/zms_adf/JDBCResource/zms_adf/JDBCDriverParams/zms_adf/Properties/zms_adf/Properties/oracle.net.CONNECT_TIMEOUT')
cmo.setValue('10000')



cd('/JDBCSystemResources/zms_adf/JDBCResource/zms_adf/JDBCConnectionPoolParams/zms_adf')
cmo.setMaxCapacity(50)
save()
activate()

