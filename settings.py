PROMS_LABEL = 'A PROMS Server'
HOME_DIR = '/var/log/proms'
STATIC_DIR = 'static/'
LOGFILE = "../" + 'proms.log'
HOST = '0.0.0.0'
PORT = 9000
DEBUG = True
SCHEMA = 'http://'+HOST+':'+str(PORT)
FUSEKI_SCHEMA = 'http://127.0.0.1:3030'

PROMS_INSTANCE_NAMESPACE_URI = SCHEMA+"/"

FUSEKI_QUERY_URI = SCHEMA +'/tdb/data/query'
FUSEKI_UPDATE_URI = SCHEMA +'/tdb/data/update'

FUSEKI_SECURE_QUERY_URI = SCHEMA +'/tdb/data'
FUSEKI_SECURE_UPDATE_URI = SCHEMA +'/tdb/data'

FUSEKI_SECURE_USR = ''
# Make sure this password matches the one entered during Fuseki installation
FUSEKI_SECURE_PWD = ''
# Request Timeout in seconds
FUSEKI_TIMEOUT = 5

# Pingback strategies to be tried (in order)
PINGBACK_CONFIG = {
	'pingback_strategies': ['known_stores', 'follow_linked_data']
}
# Comma separated list of known PROMS instances that receive pingback
KNOWN_PROMS_INSTANCES = []

DPN_BASE_URI = HOST+':'+str(PORT)
CHARSET = 'utf-8'
