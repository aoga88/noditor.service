var os = require('os');
var async = require('async');
var usage = require('os-utils');
var diskspace = require('diskspace');
var request = require('request');


var api = 'http://192.168.0.4:8080/api';
//var api = 'http://noditor-turimovil.rhcloud.com/api';

var server = {
	name: os.hostname(),
	ip: '108.166.92.61',
	os: os.type()
}

this.state = {
	id_servidor: '52fd9cfc8ec7900e15823c42'
};
var parent = this;

async.series({
	one: function(callback) {
		 usage.cpuUsage(function(v){
                       parent.state.cpu = v;
                 });
		 
                 setTimeout(function(){
                       callback(null, '1');
                 },1000);                
 	},
	two: function(callback) {
		var memoryController = require('./controllers/memory.js');
		parent.state.memory = memoryController.getActual();
		callback(null, 'two');
	},
	three: function(callback) {
		diskspace.check('/', function (total, free, status)
                {
                    parent.state.disk = {
                                total: total,
                                free: free,
                                status: status
                        };

                });
		setTimeout( function() {
			callback(null, 'three');
		}, 1000);
	}
}, function(err, results){
	request.post( api + '/state').form(parent.state);
});
