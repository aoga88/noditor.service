var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/noditor');
var os = require('os');

var server = {
	name: os.hostname(),
	ip: '108.166.92.61',
	os: os.type()
}

var refreshInterval = 10000;

var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error: '))
db.once('open', function callback(){
	var cpuController = require('./controllers/cpu.js');
	var memoryController = require('./controllers/memory.js');
	var diskController = require('./controllers/disk.js');
	cpuController.saveActual(server);
	memoryController.saveActual(server);
	diskController.saveActual(server);
})
