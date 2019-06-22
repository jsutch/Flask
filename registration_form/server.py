from flask import Flask, render_template, request, session, redirect, flash
from datetime import date
import re

app = Flask(__name__)
app.secret_key = "MySecretKey" #necessary for session

NUM    = re.compile('[0-9]')
UPPERCASE = re.compile('[A-Z]')
EMAIL  = re.compile('[a-zA-Z0-9\._-]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9]+')

@app.route('/', methods=["GET"])
def deliver_form():
    #session.clear()
    if ('flash' not in session):
        session['flash'] = 0
    return render_template("index.html")

@app.route('/process', methods=["POST", "GET"])
def process_form():
    # stuff
    session['flash'] = 0
    validate_name(request.form)
    validate_email(request.form)
    validate_password(request.form)
    validate_birthdate(request.form)

    if (session['flash'] != 0):
         print("ERRORS FOUND")
         return redirect('/')
    else: 
        form_data = {}
        for key in request.form:
            form_data[key] = request.form[key]
            session['form_data'] = form_data
        return render_template("results.html", data=session['form_data'], bod=session['birthdate'])
    #return redirect('/')

def validate_name(form):
    first = form['first_name']
    last = form['last_name']

    if len(first) == 0:
        flash("First Name can't be left empty")
        session['flash'] += 1
    else: 
        if (NUM.search(first) != None):
            flash("Name field can't have numbers")
    if len(last) == 0:
        flash("Last Name can't be left empty")
        session['flash'] += 1
    else: 
        if (NUM.search(last) != None):
            flash("Name field can't have numbers")
    return

def validate_email(form):
    email = form['email']
    if len(email) == 0:
            flash("Email Address can't be left empty")
            session['flash'] += 1
    else: 
        if EMAIL.match(email) == None:
            flash("Invalid Email Address!")
            session['flash'] += 1
    return

def validate_password(form):
    passwd = form['password']
    passconf = form['confirm_password']

    if len(passwd) == 0:
        flash("Password Must Be Filled Out")
        session['flash'] += 1
    elif len(passwd) < 3:
        flash("Password must contain at least 3 characters")
        session['flash'] += 1
    elif (NUM.search(passwd) == None):
        flash("Password must contain at least 1 number")
        session['flash'] += 1
    elif (UPPERCASE.search(passwd) == None):
        flash("Password must contain at least 1 Uppercase Character")
        session['flash'] += 1

    if (passwd != passconf):
        flash("Passwords Don't Match")
        session['flash'] += 1
    return

def validate_birthdate(form):
    year = form['year']
    month = form['month']
    day = form['day']
    birthdate = ''

    try:
        birthdate = date(int(year), int(month), int(day))
        session['birthdate'] = birthdate
    except Exception as err:
        flash("Invalid date - '{}'".format(err), 'dob')
        session['flash'] += 1

    if (birthdate):
        today = date.today()
        diff = today - birthdate
        if (diff.days <= 0):
            flash("Birthday must be in the past.")
            session['flash'] += 1
    return
# Run loop:
# debug should be set to false on the open net
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888,debug=False)
