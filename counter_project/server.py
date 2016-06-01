from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "MySecretKey" #necessary for session

def sumSessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1


@app.route('/')
def index():
	sumSessionCounter()
	return render_template("index.html", count=session['counter'])

@app.route('/reset')
def reset():
	session.clear()
	return redirect('/')

if __name__ == "__main__":
	app.run(debug=True)	