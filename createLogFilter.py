edit()
startEdit()

# create LogFilter
cd('/')
cmo.createLogFilter('SupressMessages')
cd('/LogFilters/SupressMessages')

# set expression
cmo.setFilterExpression('NOT(MSGID = \'BEA-050007\')')
cmo.setNotes('Suppress bogus messages: JNDI')

# assign Filter for all destinations on a WLS server

cd('/')
servers=getMBean("Servers").getServers()
for server in servers:
    serverName=server.getName()
    if serverName != 'AdminServer':
		path='/Servers/%s/Log/%s' %(serverName,serverName)
        cd(path)
        cmo.setLogFileFilter(getMBean('/LogFilters/SupressMessages'))
        cmo.setStdoutFilter(getMBean('/LogFilters/SupressMessages'))
        cmo.setDomainLogBroadcastFilter(getMBean('/LogFilters/SupressMessages'))
        cmo.setMemoryBufferFilter(getMBean('/LogFilters/SupressMessages'))
#save()
#activate()
