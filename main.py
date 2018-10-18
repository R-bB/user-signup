from flask import Flask, request, redirect, render_template
import cgi
import os
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def user_signup():

    user_name = request.form["username"]
    user_password = request.form["password"]
    user_verify = request.form["verify"]
    user_email = request.form["email"]

    user_name_error = ''
    user_password_error = ''
    user_verify_error = ''
    user_email_error = ''

    if len(user_name) < 3 or len(user_name) > 20:
        user_name_error = "Not a valid name."
        return render_template('index.html', username_error = user_name_error, )

    if user_password != user_verify:
        user_password_error = "passwords do not match"
        user_verify_error = "passwords do not match"
        return render_template('index.html', password_error = user_password_error, 
                                v_password_error = user_verify_error, username = user_name)
     
    else:
        return render_template('welcome.html', name = user_name) 

@app.route("/welcome")
def welcome():
    user_name = request.form['username']
    return render_template('welcome.html', name = user_name)


app.run()