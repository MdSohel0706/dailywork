from flask import Flask, render_template, request
from database import db_session, init_db
from models.restaurants import Restaurants

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
def add_restaurant():
    if request.method == 'POST':
        name = request.form.get('resname')
        desc = request.form.get('resdesc')
        site_url = request.form.get('site-url')
        
        restaurant =  Restaurants(name = name, description = desc, site_url = site_url)
        db_session.add(restaurant)
        db_session.commit()
        return render_template('creation_confirmation.html')

@app.route('/restaurants')
def show_restaurants():
    restaurants = Restaurants.query.all()
    return render_template('show_restaurants.html', restaurants = restaurants)

if(__name__ == '__main__'):
    app.run(debug = True)
