#!/usr/bin/python
import psutil, json, requests, getpass, hashlib
memory = psutil.virtual_memory()
swap = psutil.swap_memory()
disk = {'part': {}, 'usage': {}}
noditor_url = 'http://noditor.me'

def configure_app():
        print "\n\nThe application should be configured."
        print "Please login in your noditor account:"
        email = raw_input("Email:")
	password = getpass.getpass("Password:")
	m = hashlib.sha1()
	m.update(password)
	m.hexdigest()
	userObj = {
		'email': email,
		'password': m.hexdigest()
	}
	requestUrl = noditor_url + '/api/user/login'
	login = requests.post(requestUrl, userObj)
	user = login.json()
	
	try:
		user_id = user['_id']
		serverObj = {
			'user': user_id
		}
		servers = requests.post(noditor_url + '/api/server/find', serverObj, auth=(email, user_id))
		serversArray = servers.json()
		print "\n\nSelect the server you are seting up:"
		indexServer = 1
		for server in serversArray:
			print '\t' + str(indexServer) + '. ' + server['name']
			indexServer = indexServer + 1
		selectedServer = raw_input("Type the server digit: ")
		configuration = {
			'user': email,
			'password': userObj['password'],
			'server_id': serversArray[int(selectedServer) - 1]['_id']
		}
		configurationFile = open('noditor.conf', 'w+')
		configurationFile.write(json.JSONEncoder().encode(configuration))
		
		print "The noditor script has been configured successfuly\n"
		
	except KeyError:
		print "The email or password are incorrect. Please try again"



def putData(configFile):
	for index in psutil.disk_partitions():
		disk['part'][index.device] = index
		usage = psutil.disk_usage(index.device)
		disk['usage'][index.device] = {
			'total': usage[0],
			'used': usage[1],
			'free': usage[2],
			'percent': usage[3]
		}

	data = {
		'cpu': {
			'count': psutil.cpu_count(False), 
	 		'count_logical': psutil.cpu_count(True),
		 	'per': psutil.cpu_percent(1, True)
		},
		'memory': {
			'total': memory[0],
			'avail': memory[1],
			'per': memory[2],
			'used': memory[3],
			'free': memory[4]
		},
		'swap': {
			'total': swap[0],
			'used': swap[1],
			'free': swap[2],
			'per': swap[3],
			'sin': swap[4],
			'sout': swap[5]
		},
		'disk': disk,
		'users': psutil.users(),
		'boot_time': psutil.boot_time()
		}
	configStr  = configFile.read()
        config = json.JSONDecoder().decode(configStr)
        data['server_id'] = config['server_id']
        serverdata = json.dumps(data)
        headers = {'content-type': 'application/json'}
        r = requests.put(noditor_url + '/api/serverdata', data=serverdata, auth=(config['user'],config['password']), headers=headers)
try:
	configFile = open('noditor.conf', 'r')
	putData(configFile)
except IOError:
	configure_app()
	configFile = open('noditor.conf', 'r')
	putData(configFile)

