from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')

def hello_world():
	print "I'm a server side return"	
	return render_template('index.html', name="Bob")	
	

app.run(debug=True)

