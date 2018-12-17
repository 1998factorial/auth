from sqlalchemy import null, exc
from server import login_manager,db
from flask_login import LoginManager, login_user, UserMixin
import csv
from flask_sqlalchemy import SQLAlchemy
#from flask import *

"""
def Filter_by_email(input_list, email):
    match_list = []
    i = 0
    while i < len(input_list):
        if input_list[i].email == email:
            match_list.append(input_list[i])
        i += 1
    return match_list


def Filter_by_email_and_password(input_list, email, password):
    match_list = []
    i = 0
    while i < len(input_list):
        if input_list[i].email == email and input_list[i].password == password:
            match_list.append(input_list[i])
        i += 1
    return match_list
"""

class User(db.Model):
    _tablename_ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), index=True)
    password = db.Column(db.String(128))

    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password

    # @staticmethod
    def show_all_users():
        q = User.query.all()
        return q

    def query_user(email, password):
        input_list = User.show_all_users()
        print(input_list[0].email)
        match = None
        i = 0
        while i < len(input_list):
            if input_list[i].email == email and input_list[i].password == password:
                match = input_list[i]
                break
            i += 1
        return match

    # @staticmethod
    def get_password_from_email(email, password):
        #input_list = User.show_all_users()
        q = User.query_user(email, password)
        # print (q.first())
        if q == None:
            return None
        else:
            return q;


    # @staticmethod
    def new_User( email, password):  # add a new user info to db
        try:
            if not User.find_user(email):
                id = User.max_user_id()
                one = User(id,email=email,password=password)
                db.session.add(one)
                db.session.commit()
                return True;
            else:
                return False;
        except (exc.SQLAlchemyError) as e:
            print(e)
            print("Unable to create and add new User")

    def find_user(email):
        q = User.show_all_users()
        i = 0
        while i < len(q):
            if q[i].email == email:
                return True
            i += 1
        return False

    def max_user_id():
        max = 0
        i = 0
        q = User.query.all()
        while i<len(q):
            if q[i].id > max:
                max = q[i].id
            i += 1
        return max + 1

    def find_user_id(email,password):
        q = User.get_password_from_email(email, password)
        if q:
            return q.id
        else:
            return null



db.create_all()