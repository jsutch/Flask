from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html", phrase="Hello", times=5, name="Bob")
@app.route('/test')
def test():
	return render_template("test.html", phrase="Hello", times=5, name="Bob")

app.run(debug=True)	

