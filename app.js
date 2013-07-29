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

var express = require('express'),
  cons = require('consolidate'),
  swig = require('swig');
app = express();

app.engine('.html', cons.swig);
app.set('view engine', 'html');
swig.init({
    root: './views/webapp/',
    allowErrors: true
});
app.set('views', './views/webapp/');
app.use(express.static(__dirname + '/public'));

var webapp = require('./controllers/webapp.js');
app.get('/', webapp.app.home);

app.listen(3000);