from flask import render_template
from app import app
from app.ping import ping

@app.route('/')
@app.route('/index')
def index():
	result = {}
	ipads = {
                'iPad1': '10.10.122.101',
                'iPad2': '10.10.122.102',
                'iPad3': '10.10.122.103',
                'iPad4': '10.10.122.104',
                'iPad5': '10.10.122.105',
                'iPad6': '10.10.122.106',
                'iPad7': '10.10.122.107',
                'iPad8': '10.10.122.108',
                'iPad9': '10.10.122.109',
                'iPad10': '10.10.122.110',
                'iPad11': '10.10.122.111',
                'iPad12': '10.10.122.112',
                'iPad13': '10.10.122.113',
                'iPad14': '10.10.122.114',
                'iPad15': '10.10.122.115',
                'iPad16': '10.10.122.116',
                'iPad17': '10.10.122.117',
                'iPad18': '10.10.122.118',
                'iPad19': '10.10.122.119',
                'iPad20': '10.10.122.120'
        }

	for name, ip in ipads.iteritems():
		result[name] = ping(ip)

	return render_template("index.html",
		title = 'Home',
		results = result)