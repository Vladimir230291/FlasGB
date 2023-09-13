from flask import Flask
from lesson3_SQL.models import db, User, Post, Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route("/")
def index():
    return "Hello World!"


@app.cli.command('init_db')
def init_db():
    db.create_all()
    print("Database initialized!")


@app.cli.command('add_user')
def add_user():
    user = User(username="admin", email="admin@localhost")
    db.session.add(user)
    db.session.commit()
    print("User added!")


