from flask import Flask, jsonify, request, redirect, url_for

app = Flask(__name__)
@app.route('/')
def index():
	return "<h1>Welcome to Hriday's website</h1>"

@app.route('/home', methods=['GET','POST'])
def home():
	return "<h1>Welcome To Home Page</h1>"

@app.route('/person', methods=['GET','POST'], defaults={'name': 'Hriday'})
@app.route('/person/<string:name>', methods=['GET','POST'])
def person(name):
	return "<h1>Hi, {}. Welcome to Person Page</h1>".format(name)

@app.route('/json')
def json():
	return jsonify({"key1":"Value1", "key2":[10,20,30,40]})

@app.route('/query', methods=['GET','POST'])
def query():
	name = request.args.get('name')
	location = request.args.get('location')
	return "<h1>Hi {}. You are from {}. You are on the query page.</h1>".format(name, location)

@app.route('/theform', methods=['GET','POST'])
def theform():
	if request.method == 'GET':
		return '''<form method="POST" action="/theform">
					<input type="text" name="name">
					<input type="text" name="location">
					<input type="submit" value="Submit">
				</form>'''
	else:
		name = request.form['name']
		location = request.form['location']
		return "<h1>Hi {}. You are from {}. You Have Submitted The Form Successfully.</h1>".format(name, location)

# @app.route('/process', methods=["POST"])
# def process():
# 	name = request.form['name']
# 	location = request.form['location']
# 	return "<h1>Hi {}. You are from {}. You Have Submitted The Form Successfully.</h1>".format(name, location)

@app.route('/requestjson', methods=["POST"])
def requestjson():
	data = request.get_json()
	name = data['name']
	location = data['location']
	randomlist = data['randomlist']
	return jsonify({'result':'Successful', "name":name, "location":location, "randomlist":randomlist})


if __name__ == '__main__':
	app.run(debug=True)