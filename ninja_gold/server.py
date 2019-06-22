rom flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = "MySecretKey" #necessary for session

@app.route('/')
def index():
	# if gold not in session:
	# 	session['gold'] = 0
	# 	session['activity'] = []
	# return render_template('index.html', activity_log=reversed(session['activity']))
	return render_template('index.html')

@app.route('/process', methods=['POST', 'GET'])
def process():
	print "PROCESSING"
	activity_log = []
	gold = 0
	if not session['gold']:
		session['gold'] = gold
	else:	
		if request.form['location'] == 'farm':
			add_gold = random.randrange(10,20)
		if request.form['location'] == 'cave':
			add_gold = random.randrange(5,10)
		if request.form['location'] == 'house':
			add_gold = random.randrange(2,5)	
		if request.form['location'] == 'casino':
			add_gold = random.randrange(-50,50)	
		print request.form['location'] , "added" , add_gold		

	session['gold']	+= add_gold
	return render_template("index.html")


@app.route('/reset', methods=['POST', 'GET'])
def reset():
	print "RESET"
	session.clear()
	return redirect('/')


if __name__ == "__main__":
app.run(debug=True) 
