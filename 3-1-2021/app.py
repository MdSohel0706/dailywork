from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) #creating app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' #storing the database path in the URI
db = SQLAlchemy(app) #the database is being initialized from the settings from our app

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)
    completed = db.Column(db.Boolean, default = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task {self.id} created>'


@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content = task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
        except:
            'There was a problem creating your task'
        return redirect('/')
    
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks = tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:    
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        'There was a problem deleting your task'

@app.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    task_to_update = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task_to_update.content = request.form['content']
        db.session.commit()
        return redirect('/')
    else:
        return render_template('update_task.html', task = task_to_update)

if(__name__ == '__main__'):
    app.run(debug = True, use_reloader = True)