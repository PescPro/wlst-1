# Who: Tony van Esch
#what: Assign SOA appication roles to user defined groups.
#When: Tue Jan 21 14:18:15     2014
#


# Grant SOA Desinger to func beheer.
grantAppRole("soa-infra","SOADesigner","weblogic.security.principal.WLSGroupImpl","G-COVOG-FuncBeheer")
