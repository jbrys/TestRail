# If you use a hosted account
HOSTED_ACC = True
HOSTED_ACC_NAME = ''
# If you use a local/server installation
DOMAIN = ''

if HOSTED_ACC == True:
    URL = 'https://' + HOSTED_ACC_NAME + '.testrail.com/index.php?/api/v2/'
else:
    URL = DOMAIN + '/index.php?/api/v2/'

# Logon details needed for each request
USR = ''
PWD = ''
