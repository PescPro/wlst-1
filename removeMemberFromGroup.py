
serverConfig()
print 'lookup DefaultAuthenticator'
atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider('DefaultAuthenticator')

## Users

users = ['aabdoel','aboss','akalloe','bbosch','cniet','cvishnu','dbanarsi','dcharan','dpronk','edoes','fbuitela','gbark','iveenstr','alangkru','jkruk','jpater','mroeplal','msinteur','myeung','nabdoelr','nskakni','pbohemen','rbiharie','rklomp','rvreeswi','sbaysalo','sbholana','smulder','ssewgobi','swaart','vchaudro','wbajnath','wburg','ahuldy','dweterin','mwiel']
users_admi = ['akalloe','dbanarsi','dcharan','dpronk','gbark','jpater','nabdoelr','nskakni','sbaysalo','swaart']
users_junior = ['alangkru']
users_mdw = ['fbuitela','myeung','vchaudro']
users_samr = ['aabdoel','aboss','bbosch','cniet','jkruk','mroeplal','msinteur','pbohemen','rbiharie','rvreeswi','sbholana','smulder','ssewgobi','wburg']
users_fb = ['cvishnu','edoes','iveenstr','rklomp','wbajnath']
users_om = ['ahuldy','dweterin','mwiel']
users_admi_temp_20140214 = ['aabdoel','aboss','bbosch','cniet','cvishnu','edoes','fbuitela','iveenstr','jkruk','mroeplal','msinteur','myeung','pbohemen','rbiharie','rklomp','rvreeswi','sbholana','smulder','ssewgobi','vchaudro','wbajnath','wburg','ahuldy','dweterin','mwiel']


group ='G-COVOG-Administratief'

for user in users_admi_temp_20140214:
  print 'remove user %s from group %s.' %(user,group)
  try:
    atnr.removeMemberFromGroup(group,user)
    print 'user %s has been removed' %(user)
  except:
    pass

print 'Done'
