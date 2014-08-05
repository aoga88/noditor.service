import psutil, json, requests
memory = psutil.virtual_memory()
swap = psutil.swap_memory()
disk = {'part': [], 'usage': {}}

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

r = requests.post('https://10.110.103.52:8080/api/serverdata')

print json.JSONEncoder().encode(data)
