
from weblogic.management.security.authentication import UserLockoutManagerMBeanserverRuntime()
ulm=cmo.getServerSecurityRuntime().getDefaultRealmRuntime().getUserLockoutManagerRuntime()
#note1 : You can only manage user lockouts for the default realm starting from when the server was booted (versus other non-active realms).
#note2 : If the default realm's user lockout manager's LockoutEnabled attribute is false, then the user lockout managers runtime MBean will be null.
#That is, you can only manage user lockouts in the default realm if its user lockout manager is enabled.
if ulm != None:
ulm.clearLockout("tesch")
