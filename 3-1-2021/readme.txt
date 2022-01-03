TERMINAL COMMANDS
-----------------
pipenv shell - launches the virtual environment
python app.py -  launches the server

python - launches the python shell
from app import db - imports the database instance from the app 
db.create_all() - creates the database file

CREATING BASIC FLASK APP 
------------------------
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    print('Hello World')

if(__name__ == '__main__'):
    app.run(debug = True)

