from flask import Flask,request,render_template
app = Flask(__name__)
names= {}
profile = {}
def pass_c():
	print(request.data)


@app.route("/")
def base_start():
	return"<html><body><h1>Welcom to the <em>Digatle<em> world.<body><html>"
@app.route("/setup_term",methods=['GET','POST'])
def setup_term():
	if request.method == 'POST':
		profile = {}
		sent = request.form
		print("sent",sent)
		username = request.form.get('username')
		password = request.form.get('pass')
		mess = request.form.get('mess')
		print('pro',username)
		print('names',names)
		if username not in names:
			profile['username'] = username
			profile["password"] = password
			profile["mess"] = mess
			names[username]=profile
			print(names)
		else:
			print('username taken')
			return'username taken'
		print(names)
		return('profile saved')
	else:
		return "<html><body><h1s>please use a <em>post<em> request<body><html>"
@app.route("/setup",methods=['GET'])
def setup():
	if request.method == 'GET':
		return render_template('setup.html')


@app.route("/user/<username>",methods=['GET','POST'])
def user_page(username):
	if request.method == 'GET':
		if username in names:
			print (names[username])

			return render_template('user.html',username = names[username]['username'],password = names[username]['password'],mess = names[username]['mess'])
			#return names[username]["password"]+'\n'+names[username]["username"]+'\n'+names[username]["mess"]
		else:
			return render_template('404_pro.html')


	if request.method == 'POST':
		if username in names:
			print (names[username])
			return names[username]
if __name__ == "__main__":
	app.run('127.0.0.1')

















	#app.run('192.168.0.41')
#	names[profile] = request.form.get('data')
		#	names[profile]['data'] = request.form.get('data')
