import os
from time import sleep
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from matplotlib.style import use
from models import *


app = Flask(__name__, static_url_path='/static')
app.config["SECRET_KEY"] = 'blablabla123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/add-user", methods=["GET", "POST"])
def user():
    if request.method == 'POST':
        try:
            username = request.form["username"]
            new_user = Users(username = username)
            db.session.add(new_user)
            db.session.commit()
            flash("Vartotojas sekmingai pridetas")
            return redirect(url_for('user'))
        except:
            flash("Toks vartotojas jau egzistuoja")
    return render_template("add_user.html")

@app.route("/add-test", methods=["GET", "POST"])
def creating_test():
    if request.method == 'POST':
        user = request.form['username']
        test_name = request.form['test_name']
        question_count = request.form['count_of_questions']
        answer_count = request.form['count_of_answers"']
        all_questions = request.form.getlist('test_question')
        all_answers = request.form.getlist('test_answer')
        all_right_answers = request.form.getlist('right_answer')
        return redirect(url_for('index'))
    return render_template("add_test.html")



if __name__ == '__main__':
    app.run(debug=True)


