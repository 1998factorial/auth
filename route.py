import os
import json as json
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
import subprocess


Server = "ldap://192.168.1.115:389" 
is_admin = False

def login_required(f): #user need to log in first in order to access home page
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("YOU NEED TO LOG IN FIRST")
            return redirect(url_for('login'))
    return wrap
"""
def change_password_as_admin(username,old_password,new_password):
    baseDN = "dc=example,dc=com"
    searchScope = ldap.SCOPE_SUBTREE
    if username != "admin":
        username = "uid=" + username + ",ou=people," + baseDN #expected form
    else:
        username = "cn=admin,dc=example,dc=com"
    c = ldap.initialize(Server)
    try:
        c.simple_bind_s(username,old_password)
    except ldap.LDAPError as e:
        flash("invalid credentials")
        return False

    try:
        adpw = new_password.encode("utf-8") #有待商榷
        c.simple_bind_s("cn=admin,dc=example,dc=com","test123456")
        c.modify_s(username,[(ldap.MOD_REPLACE, "userPassword", adpw)])
        c.modify_s(username,[(ldap.MOD_REPLACE, "sambaLMPassword", adpw)])
        c.modify_s(username,[(ldap.MOD_REPLACE, "sambaNTPassword", adpw)])
        flash("CHANGED PASSWORD")
        return True
    except ldap.LDAPError as error_message:
        flash("CANNOT CHANGE PASSWORD")
        print(error_message)
        return False
"""

def change_password(username,old_password,new_password):
    baseDN = "dc=example,dc=com"
    searchScope = ldap.SCOPE_SUBTREE
    if session['username'] != username and username != 'admin':
        return False
    if is_admin:
        print("change password as admin")
    if username != "admin":
        username = "uid=" + username + ",ou=people," + baseDN #expected form
    else:
        username = "cn=admin,dc=example,dc=com"
    c = ldap.initialize(Server)
    try:
        c.simple_bind_s(username,old_password)
    except ldap.LDAPError as e:
        flash("invalid credentials")
        return False
    try:
        adpw = new_password.encode("utf-8")
        out1 = subprocess.run(['./mkntpwd','-N',new_password],stdout=subprocess.PIPE)
        out2 = subprocess.run(['./mkntpwd','-L',new_password],stdout=subprocess.PIPE)
        pwd_N = out1.stdout
        pwd_L = out2.stdout
        print("____________")
        c.modify_s(username,[(ldap.MOD_REPLACE, "userPassword", adpw)])
        c.simple_bind_s("cn=admin,dc=example,dc=com","test123456")#bind admin
        c.modify_s(username,[(ldap.MOD_REPLACE, "sambaLMPassword", pwd_L[0:len(pwd_L)-1])])
        c.modify_s(username,[(ldap.MOD_REPLACE, "sambaNTPassword", pwd_N[0:len(pwd_N)-1])])
        flash("CHANGED PASSWORD")
        return True
    except ldap.LDAPError as error_message:
        flash("CANNOT CHANGE PASSWORD")
        print(error_message)
        return False


def check_password(username,password): #verify
    baseDN = "dc=example,dc=com"
    searchScope = ldap.SCOPE_SUBTREE
    log_in_as_admin = False
    if username != "admin":
        username = "uid=" + username + ",ou=people," + baseDN #expected form
    else:
        log_in_as_admin = True
        username = "cn=admin,dc=example,dc=com"
    #username = "cn=admin,dc=example,dc=com"
    searchFilter = "sAMAccountName" + username
    re_Attribute = None
    
    try:
        c = ldap.initialize(Server)
        c.simple_bind_s(username,password)
        print("IS VALID!")
        if log_in_as_admin:
            session['is_admin'] = True
        else:
            session['is_admin'] = False
        return True
    except ldap.LDAPError as error_message:
        flash("Invalid credentials\n")
        print("IS INVALID!")
        return False


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/change password', methods=['POST','GET'])
@login_required
def change_password_route():
    if request.method == 'POST':
        username = request.form['username']
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        if change_password(username,old_password,new_password):
            print("successfully changed password")
            redirect(url_for('index'))
        else:
            print("can not change password")
    return render_template('change_password.html')



@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        #get user inputs (username,password)
        username = request.form['username']
        password = request.form['password']
        if check_password(username,password): #verify succeed
            session['logged_in'] = True #let user login
            session['username'] = username
            session['password'] = password
            if session['is_admin']:
                print("log in as admin")
            #session['userID'] = User.find_user_id(username,password) #set user id
            return redirect(url_for('index')) #redirect to index page

        return render_template('login.html',auth=False,error_message="invaild credentials,please try again!")

    return render_template('login.html',auth=None) #no input from ui

@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.new_User(username,password):
            session['username'] = username
            session['password'] = password
            session['logged_in'] = True
            session['userID'] = User.max_user_id()
            return redirect(url_for('index')) #if register succeed, redirect user to index page
        flash("The username you just entered has already been used!")
        return render_template('register.html',auth=False,error_message="Invaild credentials/reused user name,please try again!")
        #TODO this part might be wrong!!!
    return render_template('register.html',auth=None)

@app.route('/logout')
def logout():
    if session.get('username'):
        session.pop('username')
    if session.get('password'):
        session.pop('password')
    if session.get('logged_in'):
        session.pop('logged_in')
    session['is_admin'] = False
    return redirect(url_for('login')) #redirect user to login page
"""
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
"""