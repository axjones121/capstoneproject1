from models import db, User, Article, Comment
from app import app


db.drop_all()
db.create_all()