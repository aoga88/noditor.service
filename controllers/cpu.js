var mongoose = require('mongoose');
var CpuModel = require('../models/cpu.js');
var libCpuUsage = require( 'cpu-usage' );

exports.saveActual = function(server){
	libCpuUsage( 1000, function( load ) {
	    var actualValue = new CpuModel.cpu({
			server: server,
			load: load
		});
		actualValue.save(function(err, object){
			if(err)
				console.log(err);
		});
	} );
}