from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import dateTime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer(),primary_key = True)
    name = db.Column(db.String())
    date = db.Column(db.String())
    time = db.Column(db.String())

@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        form = request.form
        if form["name"] == "":
            pass
        else:
            task_to_add = Task(name = form["name"], date = dateTime.get_date(), time = dateTime.get_time())
            db.session.add(task_to_add)
            db.session.commit()
            redirect(url_for("home"))
    
    all_tasks = Task.query.all()
    return render_template("main.html", tasks = all_tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Task.query.get_or_404(id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/update/<int:id>',methods=['GET', 'POST'])
def update(id):
    task_to_update = Task.query.get_or_404(id)
    if request.method == "POST":
        task_to_update.name = request.form["name"]
        task_to_update.date = dateTime.get_date()
        task_to_update.time = dateTime.get_time()
        db.session.commit()
        return redirect(url_for("home"))
    
    return render_template('update.html', task = task_to_update)

if __name__ == '__main__':
    app.run(debug=True)