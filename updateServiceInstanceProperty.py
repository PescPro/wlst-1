

# call: wlst.sh updateServiceInstanceProperty.py -si idstore.ldap  -key "virtualize" -value "true"

WL_DOMAIN=os.getenv('WL_DOMAIN')
execfile(WL_DOMAIN + '_properties.py')  # load domain specific constants

connect(AdminUser,AdminUserPW,AdminServerUrl)

import sys

domainRuntime()

val = None
key = None
si = None
for  i in range(len(sys.argv)):
    if sys.argv[i] == "-si":
        si = sys.argv[i+1]
    if sys.argv[i] == "-key":
        key  = sys.argv[i+1]
    if sys.argv[i] == "-value":
        val = sys.argv[i+1]
 
on = ObjectName("com.oracle.jps:type=JpsConfig")
sign = ["java.lang.String","java.lang.String","java.lang.String"]
params = [si,key,val]
mbs.invoke(on, "updateServiceInstanceProperty", params, sign)
mbs.invoke(on, "persist", None, None)
