var mongoose = require('mongoose');
var diskModel = require('../models/disk.js');
var diskspace = require('diskspace');

exports.saveActual = function(server){
    setInterval(function(){
    	diskspace.check('/', function (total, free, status)
		{
		    var actualValue = new diskModel.disk({
				server: server,
				total: total,
				free: free,
				status: status
			});
			actualValue.save(function(err, object){
				if(err)
					console.log(err);
			});
		});
    }, 3000);
}