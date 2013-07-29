var mongoose = require('mongoose');
var memoryModel = require('../models/memory.js');
var os = require('os');

exports.saveActual = function(server){
    setInterval(function(){
	    	var actualValue = new memoryModel.memory({
			server: server,
			freemem: os.freemem(),
			totalmem: os.totalmem(),
			load: os.freemem() / os.totalmem()
		});
		actualValue.save(function(err, object){
			if(err)
				console.log(err);
		});
    }, 3000);
}