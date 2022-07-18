from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80),nullable=False)
    last_name = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nickname = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "nickname" : self.nickname,
            "email": self.email,
        }

class Personajes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(80),nullable=False)
    last_name = db.Column(db.String(80),nullable=False)
    planet = db.Column(db.String(80),nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Personaje %r>' % self.first_name

    def serialize(self):
        return {
            "id": self.id,
            "first_name" : self.first_name,
            "last_name": self.last_name,
        }

class Planetas(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),nullable=False)

    def __repr__(self):
        return '<Planeta %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name" : self.name,
        }

class Favoritos(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    personaje:id = db.Column(db.Integer,)