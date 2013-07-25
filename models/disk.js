var mongoose = require('mongoose');
var diskSchema = mongoose.Schema({
	server: {
		name: String,
		ip: String,
		os: String
	},
	date: {type: Date, default: Date.now},
	total: Number,
	free: Number,
	status: String
}, {collection: 'disk'});

exports.disk = mongoose.model('disk', diskSchema);