import os
import json
from flask_login import login_required
from flask import *
from sqlalchemy.orm import joinedload
from sqlalchemy.sql import text
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc, null
from server import app, login_manager, db #get app,login_manager,db
from datetime import datetime
from User import * #need to implement user class
from functools import wraps
import os,sys,ldap


Server = "ldap://192.168.1.115:389"


def login_required(f): #user need to log in first in order to access home page
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("YOU NEED TO LOG IN FIRST")
            return redirect(url_for('login'))
    return wrap


def check_password(username,password): #verify
    #if User.get_password_from_email(email,password):
    #    session['email'] = email
    #    session['password'] = password
    #    return True
    #return False

    baseDN = "dc=example,dc=com"
    searchScope = ldap.SCOPE_SUBTREE
    if username != "admin":
        username = "uid=" + username + ",ou=people," + baseDN #expected form
    else:
        username = "cn=admin,dc=example,dc=com"
    #username = "cn=admin,dc=example,dc=com"
    searchFilter = "sAMAccountName" + username
    re_Attribute = None
    
    try:
        c = ldap.initialize(Server)
        c.simple_bind_s(username,password)
        print("CAN LOGIN!")
        return True
    except ldap.LDAPError as error_message:
        flash("Invalid credentials")
        print("CAN NOT LOGIN")
        return False


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        #get user inputs (email,password)
        email = request.form['email']
        password = request.form['password']
        if check_password(email,password): #verify succeed
            session['logged_in'] = True #let user login
            #session['userID'] = User.find_user_id(email,password) #set user id
            return redirect(url_for('index')) #redirect to index page

        return render_template('login.html',auth=False,error_message="invaild credentials,please try again!")

    return render_template('login.html',auth=None) #no input from ui

@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if User.new_User(email,password):
            session['email'] = email
            session['password'] = password
            session['logged_in'] = True
            session['userID'] = User.max_user_id()
            return redirect(url_for('index')) #if register succeed, redirect user to index page
        flash("The email you just entered has already been used!")
        return render_template('register.html',auth=False,error_message="Invaild credentials/reused user name,please try again!")
        #TODO this part might be wrong!!!
    return render_template('register.html',auth=None)

@app.route('/logout')
def logout():
    if session.get('email'):
        session.pop('email')
    if session.get('password'):
        session.pop('password')
    if session.get('logged_in'):
        session.pop('logged_in')
    return redirect(url_for('login')) #redirect user to login page

import simplejson as json
def ok_json(data, msg = None):
    try:
        s =  json.dumps({"ok":True,"data":data, "msg":msg})
        return s
    except Exception as e:
        print e
        return None

def fail_json(errmsg,data = None):
    try:
        s =  json.dumps({"ok":False,"data":data,"error":errmsg})
        return s
    except Exception as e:
        print e
        return None
		
@app.route('/user/api/login',methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
	if username and password:
	    is_login = True
	    # please add login code here.  and please set is_login = true if succeeded. 
		.... here is code for login ..... 
		......
		....
		
		
		if is_login:
			user_data = {'username':username, 'uid':xxxx,  .... }  		# please provide the user info.  
		    return  Response(ok_json(user_data), mimetype='application/json')
		else:
		    return  Response(fail_json("CANNOT Login. something error!"), mimetype='application/json')
	else
        return  Response(fail_json("username or password not found!"), mimetype='application/json')
	    