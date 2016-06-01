from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "MySecretKey" #necessary for session

@app.route('/')
def index():
	theNumber = 42
	session['theNumber'] = theNumber
	#print "DEBUG"*50
	print "Hit On ROOT"
	# return render_template("index.html", theNumber=session['myNumber'])
	return render_template("index.html")


@app.route('/validate', methods=['POST', 'GET'])
def validate():
	answer = ''
	theNumber = 42
	#session['theNumber'] = theNumber
	test = request.form['yourguess']
	if str(test).isdigit() and str(test) > 0:
		session['test'] = request.form['yourguess']
		
	print "Hit On VALIDATE - number is " , test
	# set to correct output
	if test == str(session['theNumber']):
		session['answer'] = "justright"
	elif test >= str(theNumber):
		session['answer'] = "toohigh"
	elif test <= str(theNumber):
		session['answer'] = "toolow"		
	else:
		session['answer'] = "borked"

	return render_template('index.html')

@app.route('/reset', methods=['POST', 'GET'])
def reset():
	print "Hit On RESET"
	session.clear()
	return redirect('/')


if __name__ == "__main__":
	app.run(debug=True)	