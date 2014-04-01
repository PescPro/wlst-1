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
servers = domainRuntimeService.getServerRuntimes();
for server in servers:
        print 'SERVER: ' + server.getName();
        print '**************************************************'
        print  serverName
        print '**************************************************'
	
        print('JDBC RUNTIME INFORMATION');
        jdbcRuntime = server.getJDBCServiceRuntime();
        datasources = jdbcRuntime.getJDBCDataSourceRuntimeMBeans();
        for datasource in datasources:
                print('-Data Source: ' + datasource.getName() + ', Active Connections: ' + repr(datasource.getActiveConnectionsCurrentCount()) + ', Waiting for Connections: ' + repr(datasource.getWaitingForConnectionCurrentCount()));

	print('JMS RUNTIME INFORMATION');
	jmsRuntime = server.getJMSRuntime();
	connections = jmsRuntime.getConnections();
	for connection in connections:
		print('-Connection Name: ' + connection.getName());
		sessions = connection.getSessions();
		for session in sessions:
			print(' -Session Name: ' + session.getName());
			consumers = session.getConsumers();
			for consumer in consumers:
				print('  -Consumer Name: ' + consumer.getName() + ', Bytes Received: ' + repr(consumer.getBytesReceivedCount()));
			producers = session.getProducers();
			for producer in producers:
				print('  -Producer Name: ' + producer.getName() + ', Bytes Send: ' + repr(producer.getBytesSentCount()));
	jmsServers = jmsRuntime.getJMSServers();
	for jmsServer in jmsServers:
		print('-JMSServer: ' + jmsServer.getName());
		destinations = jmsServer.getDestinations();
		for destination in destinations:
			print(' -Destination: ' + destination.getName() + ', ' + repr(destination.getMessagesHighCount()) + ', ' + repr(destination.getConsumersHighCount()));


