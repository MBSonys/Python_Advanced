from app import db

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True)
    score = db.relationship("HighScore", backref='users', lazy=True)

    def __repr__(self):
        return self.username 

class Tests(db.Model):
    __tablename__ = 'tests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    questions = db.relationship('Questions', backref='tests', lazy=True)
    highscore = db.relationship("HighScore", backref='tests', lazy=True)

    def __repr__(self):
        return f'{self.id} - {self.name}'
    
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

    def __repr__(self):
        return f'{self.id} - {self.test_id} - {self.question} - {self.answer_1} - {self.answer_2} - {self.answer_3} - {self.answer_4} - {self.right_answer}'

class HighScore(db.Model):
    __tablename__ = 'highscore'
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id")) 
    test_id = db.Column(db.Integer, db.ForeignKey('tests.id'))

    def __repr__(self):
        return f'{self.user_id} - {self.test_id} - {self.score}'