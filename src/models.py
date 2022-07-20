from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80),nullable=False)
    last_name = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nickname = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favoritos_pj = db.relationship('Tag', secondary=tags, lazy='subquery',
        backref=db.backref('pages', lazy=True))

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


favoritos_pj = db.Table('favpj',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('planeta_id', db.Integer, db.ForeignKey('planetas.id'), primary_key=True)
)

class FavoritosPj(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    personaje_id = db.Column(db.Integer, db.ForeignKey('Personajes.id') )
    users_id = db.Column(db.Integer, db.ForeignKey('Users.id') ) 

    def __repr__(self):
        return '<Personaje Fav %r>' % self.personaje_id

    def serialize(self):
        return {
            "id": self.id,
            "personaje" : self.personaje_id,
            "user": self.users_id,
        }

class FavoritosPl(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    planeta_id = db.Column(db.Integer, db.ForeignKey('Planetas.id') )
    users_id = db.Column(db.Integer, db.ForeignKey('Users.id') )

    def __repr__(self):
        return '<Planeta Fav %r>' % self.planeta_id

    def serialize(self):
        return {
            "id": self.id,
            "planeta": self.planeta_id,
            "user": self.users_id,
        }