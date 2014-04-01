#
# Make sure you start wlst from: $MW_HOME/oracle_common/common/bin/wlst.sh
#
#  connect('whlogic','rocks','t3://adminservernode.nl:7001')
# Who: Tony van Esch
#When: Fri Feb 14 15:12:04     2014
#

listAppRoles('OracleBPMProcessRolesApp')
try:
  grantAppRole("OracleBPMProcessRolesApp","Intake.Administratie","weblogic.security.principal.WLSGroupImpl","G-COVOG-Administratief")
except:
  pass
try:
  grantAppRole("OracleBPMProcessRolesApp","BBH.Administratie","weblogic.security.principal.WLSGroupImpl","G-COVOG-Administratief")
except:
  pass
try:
  grantAppRole("OracleBPMProcessRolesApp","Opschorten.Administratie","weblogic.security.principal.WLSGroupImpl","G-COVOG-Administratief")
except:
  pass
try:
  grantAppRole("OracleBPMProcessRolesApp","Afhandelen.Administratie","weblogic.security.principal.WLSGroupImpl","G-COVOG-Administratief")
except:
  pass
try:
  grantAppRole("OracleBPMProcessRolesApp","Intake.JuniorMedewerker","weblogic.security.principal.WLSGroupImpl","G-COVOG-JuniorMedewerker")
except:
  pass
try:
  grantAppRole("OracleBPMProcessRolesApp","Beoordelen.SAMR","weblogic.security.principal.WLSGroupImpl","G-COVOG-SAMR")
except:
  pass

