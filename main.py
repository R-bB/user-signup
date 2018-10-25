from flask import Flask, request, redirect, render_template
import cgi
import os
import re #regex for bonus

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

    username_space = len(re.findall("\s", user_name)) #regex used to find whitespace
    password_space = len(re.findall("\s", user_password)) #regex used to find whitespace

    if len(user_name) < 3 or len(user_name) > 20 or username_space > 0:
        user_name_error = "Not a valid user-name."
        return render_template('index.html', username_error = user_name_error, email = user_email)

    if user_password != user_verify or len(user_password) < 3 or len(user_password) > 20 or password_space > 0:
        user_password_error = "passwords must match, be between 3 and 20 characters, and not contain spaces"
        user_verify_error = "passwords must match, be between 3 and 20 characters, and not contain spaces"
        return render_template('index.html', password_error = user_password_error, 
                                v_password_error = user_verify_error, username = user_name,
                                email = user_email)
     
    if not re.match("[^@ ]+@[^@ ]+\.[^@ ]+", user_email) and user_email != '' or len(user_email) > 20: #regex used to check for valid email
        user_email_error = "not a valid email"
        return render_template('index.html', email_error = user_email_error)

    else:
        return render_template('welcome.html', name = user_name) 

@app.route("/welcome")
def welcome():
    user_name = request.form['username']
    return render_template('welcome.html', name = user_name)


app.run()