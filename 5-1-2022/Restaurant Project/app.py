from flask import Flask, render_template, request
from database import db_session, init_db

app = Flask(__name__)

@app.before_first_request
def init():
    init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route("/")
def root():
    return render_template('create_restaurant.html')

@app.route('/add_restaurant', methods = ['GET', 'POST'])
def create_restaurant():
    if request.method == 'POST':
        name = request.form.get('resname')
        desc = request.form.get('resdesc')
        email = request.form.get('resemail')
        phno = request.form.get('resphno')
        return (f'RESTAURANT CREATED \n Name = {name} \n Description = {desc} \n Email = {email} \n Phone = {phno}')

if(__name__ == '__main__'):
    app.run(port = 8000, debug = True)
