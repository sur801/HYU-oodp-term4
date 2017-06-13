from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite::///'

db = SQLAlchemy(app)

class addressbook(app):
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    number = db.Column(db.String(20))
    email = db.Column(db.String(50))

def __init__(self, name, number, email):
    self.name = name
    self.number = number
    self.email = email

db.create_all()