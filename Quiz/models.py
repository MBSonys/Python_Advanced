from app import db

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True)
    score = db.relationship("HighScore", backref='users', lazy=True)

class Tests(db.Model):
    __tablename__ = 'tests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    questions = db.relationship('Questions', backref='tests', lazy=True)
    highscore = db.relationship("HighScore", backref='tests', lazy=True)
    
class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('tests.id'))
    question = db.Column(db.String(300))
    answer_1 = db.Column(db.String(300), nullable=True)
    answer_2 = db.Column(db.String(300), nullable=True)
    answer_3 = db.Column(db.String(300), nullable=True)
    answer_4 = db.Column(db.String(300), nullable=True)
    right_answer = db.Column(db.String(10))

class HighScore(db.Model):
    __tablename__ = 'highscore'
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id")) 
    test_id = db.Column(db.Integer, db.ForeignKey('tests.id'))
