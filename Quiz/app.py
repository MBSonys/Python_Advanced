
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
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
        answer_count = request.form['count_of_answers']
        all_questions = request.form.getlist('test_question')
        all_answers = request.form.getlist('test_answer')
        all_right_answers = request.form.getlist('right_answer')
        if Users.query.filter_by(username = user).first() != '':
            new_test = Tests(name = test_name)
            db.session.add(new_test)
            db.session.commit()
            new_test_id = Tests.query.filter_by(name = test_name).first_or_404()
            for i in range(int(question_count)):
                answer_start_number = 0
                if int(answer_count) == 2:
                    new_question = Questions(
                        test_id = new_test_id.id, 
                        question = all_questions[i], 
                        answer_1 = all_answers[answer_start_number], 
                        answer_2 = all_answers[answer_start_number + 1],
                        answer_3 = '', 
                        answer_4 = '', 
                        right_answer = all_right_answers[i])
                    answer_start_number += 2
                    db.session.add(new_question)
                    db.session.commit()
                elif int(answer_count) == 3:
                    new_question = Questions(
                        test_id = new_test_id.id, 
                        question = all_questions[i], 
                        answer_1 = all_answers[answer_start_number], 
                        answer_2 = all_answers[answer_start_number + 1], 
                        answer_3 = all_answers[answer_start_number + 2], 
                        answer_4 = '',
                        right_answer = all_right_answers[i])
                    answer_start_number += 3
                    db.session.add(new_question)
                    db.session.commit()
                else:
                    new_question = Questions(
                        test_id = new_test_id.id, 
                        question = all_questions[i], 
                        answer_1 = all_answers[answer_start_number], 
                        answer_2 = all_answers[answer_start_number + 1], 
                        answer_3 = all_answers[answer_start_number + 2], 
                        answer_4 = all_answers[answer_start_number + 3],
                        right_answer = all_right_answers[i])
                    answer_start_number += 4
                    db.session.add(new_question)
                    db.session.commit()
        flash("Testas sekmingai pridetas")
        return redirect(url_for('index'))
    return render_template("add_test.html")



if __name__ == '__main__':
    app.run(debug=True)


