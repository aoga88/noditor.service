var WebApp = function()
{
	this.home = function(require, response)
	{
		response.render('home.html', { foo: 'bar' });
	}
}

exports.app = new WebApp();