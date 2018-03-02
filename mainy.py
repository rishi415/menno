from flask import Flask, flash, redirect, render_template, request, session, abort
from pymongo import MongoClient
from flask_restful import Resource, Api
import os, werkzeug
#packages: dnspython, certifi
app = Flask(__name__)


client = MongoClient("mongodb+srv://root:root@cluster0menno-nwqqf.mongodb.net/test")
db = client.test


app = Flask(__name__)
api = Api(app)
todos = {}

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!  <a href='/logout'>Logout</a>"


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'basant' and request.form['username'] == 'rishi':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/fixing', methods=['POST', 'GET'])
def fixing():
    a = request.form['username']
    b = request.form['password']
    c = request.form['achternaam']
    d = request.form['adres']
    e = request.form['aanhef']
    return a + b + c + d + e

    # content = request.get_json(silent=True)
    # print(content)
    # return content

# class TodoSimple(Resource):
#     def get(self, todo_id):
#         return {todo_id: todos[todo_id]}
#
#     def put(self, todo_id):
#         todos[todo_id] = request.form['data']
#         return {todo_id: todos[todo_id]}
#
# api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=80)
