var mongoose = require('mongoose');
var cpuSchema = mongoose.Schema({
	server: {
		name: String,
		ip: String,
		os: String
	},
	date: {type: Date, default: Date.now},
	load: Number
},{collection: 'cpu'});

exports.cpu = mongoose.model('cpu', cpuSchema);