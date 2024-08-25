from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, recommended to avoid warnings

db = SQLAlchemy(app)

class Todo(db.Model):
    SNO = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.SNO}, {self.title}"

@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        # print(request.form["textplace"])
        title=request.form['title']
        desc=request.form['desc']      
        todo=Todo(title=title,desc=desc)
        db.session.add(todo)
        db.session.commit()

    todo=Todo.query.all()
    return render_template('index.html',allTodo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    allTodo=Todo.query.filter_by(SNO=sno).first()
    db.session.delete(allTodo)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:sno>',methods=['GET',"POST"])
def update(sno):
    if request.method=='POST':
        allTodo=Todo.query.filter_by(SNO=sno).first()
        allTodo.title=request.form['title']
        allTodo.desc=request.form['desc']
        db.session.add(allTodo)
        db.session.commit()
        return redirect('/')
    
    allTodo=Todo.query.filter_by(SNO=sno).first()
    return render_template('update.html',todo=allTodo)


if __name__ == "__main__":
    with app.app_context():
       db.create_all()
    app.run(debug=True, port=8000)