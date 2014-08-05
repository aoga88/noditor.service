#!/usr/bin/python
import psutil, json, requests, getpass, hashlib
memory = psutil.virtual_memory()
swap = psutil.swap_memory()
disk = {'part': [], 'usage': {}}
server_id = '2'
noditor_url = 'http://10.110.103.52:8080'

def configure_app():
        print "The application should be configured."
        print "Please login in your noditor account:"
        email = raw_input("Email:")
        print email
	password = getpass.getpass("Password:")
	print password
	m = hashlib.sha1()
	m.update(password)
	m.hexdigest()
	userObj = {
		'email': email,
		'password': m.hexdigest()
	}
	requestUrl = noditor_url + '/api/user/login'
	print requestUrl
	login = requests.post(requestUrl, userObj)
	print login.json()

for index in psutil.disk_partitions():
	disk['part'].append(index)
	usage = psutil.disk_usage(index.device)
	disk['usage'][index.device] = {
		'total': usage[0],
		'used': usage[1],
		'free': usage[2],
		'percent': usage[3]
	}

data = {'server_id': server_id,
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
	'disk': disk
	}

#r = requests.post('https://10.110.103.52:8080/api/serverdata')

try:
	config = open('noditor.conf', 'r')
except IOError:
	configure_app()

#print json.JSONEncoder().encode(data)
