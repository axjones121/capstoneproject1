#pip install psycopg2-binary
#pip install flask-sqlalchemyrom flask_sqlalchemy import SQLAlchemy
#put from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
#import bCrypt
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
    db.app = app
    db.init_app(app)


    ##models go below

class User(db.Model):
    """User in the system."""

    __tablename__ = 'users'

    id = db.Column( db.Integer, primary_key=True,autoincrement=True )

    username = db.Column( db.Text, nullable=False, unique=True)

    password = db.Column( db.Text, nullable=False )

    article_id = db.Column( db.Integer, db.ForeignKey('articles.id'))

    comments = db.relationship('Comment', backref='users')

    articles = db.relationship('Article')



    @classmethod
    def register(cls, username, pwd):
        """Register user w/hashed password & return user."""

        hashed = bcrypt.generate_password_hash(pwd)
        # turn bytestring into normal (unicode utf8) string
        hashed_utf8 = hashed.decode("utf8")

        # return instance of user w/username and hashed pwd
        return cls(username=username, password=hashed_utf8)
    # end_register

    # start_authenticate
    @classmethod
    def authenticate(cls, username, pwd):
        """Validate that user exists & password is correct.

        Return user if valid; else return False.
        """

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            # return user instance
            return u
        else:
            return False
    # end_authenticate    


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column( db.Integer, primary_key=True, autoincrement=True)

    title = db.Column( db.Text )

    description = db.Column( db.Text )

    image = db.Column( db.Text)

    url = db.Column( db.Text )

    read = db.Column( db.Boolean )

    comments = db.relationship('Comment', backref='articles')


class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column( db.Integer, primary_key=True, autoincrement=True )
    user_id = db.Column( db.Integer, db.ForeignKey('users.id'), nullable=False )
    comment = db.Column( db.Text )

    article_id = db.Column(
        db.Integer,
        db.ForeignKey('articles.id')
    )