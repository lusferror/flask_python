import os
from flask import Flask, jsonify, request, render_template
from model import db, User
from flask_cors import CORS
from flask_migrate import Migrate

BASEDIR = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+\
    os.path.join(BASEDIR,"db.db")

Migrate(app,db)
db.init_app(app)
CORS(app)

@app.route('/users',methods=['GET'])
def get_user():
    print(db)
    return jsonify({"msg":"ok"}),200
    # users=db.session.query(User).all()
    # if user is None:
    #     return jsonify({"msg":"no hay usuario"}),404
    # else:
    #     list_users=list()
    #     for user in users:
    #         print("user ",user)
    #         print("user name ",user.name)
    #         print("user email",user.email)
    #         list_users.append({"name":user.name, "email":user.email})
    #     print(users)
    #     return jsonify({"users":list_users})
