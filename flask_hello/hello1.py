from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/success')
def success():
	return render_template('success.html')

@app.route('/test')
def test():
	return "Working!"

@app.route('/test1')
def do_test1():
	return "I am the new Test1"
	
app.run(debug=True)

