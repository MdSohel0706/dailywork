from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods = ["POST","GET"])
def hello():
    return "<h1>Hello World</h1>"

@app.route("/hello", methods = ["POST","GET"], defaults = {"name": "Developer"})
@app.route("/hello/<string:name>")
def index(name):
    return "<h1>Hello {}</h1>".format(name)

@app.route("/json")
def json():
    return jsonify({"Errors" : "Psychodynamic", "Sleep" : "like a baby"})

@app.route("/query")
def query():
    name = request.args.get("name")
    location = request.args.get("location")
    return "Hi, {} you're from {}. You're on the query page".format(name,location)

@app.route("/form")
def theform():
    return '''<form method = 'POST' action = '/process'>
                <input type = "text" placeholder = "Enter name" name = "name"/>
                <input type = "text" placeholder = "Enter location" name = "location"/>
                <input type = "submit" value = "Submit" name = "submitbtn"/>
              </form>'''

@app.route('/process', methods = ['POST'])
def theprocess():
    name = request.form['name']
    location = request.form['location']
    return "Hello {}. You're in {}. You have submitted the form successfully.".format(name,location)

@app.route('/processjson', methods = ['POST'])
def processjson():
    data = request.get_json()
    name = data['name']
    location = data['location']
    pincode = "".join(data['pincode_digits'])

    return jsonify({"data" : "Success", "name" : name, "location" : location, "pincode" : pincode})


if __name__ == "__main__":
    app.run(port = 8000, debug = True)