from flask import Flask, redirect, render_template, flash, session, request
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, User, Comment, Article
from forms import RegisterForm, LoginForm, CommentForm

from sqlalchemy.exc import IntegrityError
# from forms import 
import requests, random, datetime
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','postgresql:///newsapp_capstone')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'helloworld2')
# debug = DebugToolbarExtension(app)

#connect db should go last
connect_db(app)

API_URL = "https://newsapi.org/v2/everything"

#time setup for most recent articles
tday = datetime.date.today()
yday = tday - datetime.timedelta(days = 1)
rando = random.randint(0, 1)
todayyesterday = [tday, yday]
# -------

########!!!!!!https://pythonbasics.org/flask-tutorial-routes/




@app.route("/")
def root():
    """main page"""
    return render_template("welcome.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        name = form.username.data
        pwd = form.password.data

        # authenticate will return a user or False
        user = User.authenticate(name, pwd)

        if user:
            session["user_id"] = user.id  # keep logged in
            return redirect("/article")

        else:
            form.username.errors = ["Bad name/password"]


    return render_template("login.html", form=form )

@app.route("/logout")
def logout():
    """Logs user out and redirects to homepage."""

    session.pop("user_id")

    return redirect("/")

@app.route("/signup", methods=["GET", "POST"])
def signup():

    form = RegisterForm()

    if form.validate_on_submit():
        name = form.username.data
        pwd = form.password.data
    
        user = User.register(name, pwd)
        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.id
        return redirect("/article")
    
    else:
        return render_template("signup.html", form=form)

@app.route("/article")
def globalnews():

    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/signup")

    else:
        randonum = random.randint(1, 15)
        resp = requests.get("https://newsapi.org/v2/everything", params={"q":"international", "from": todayyesterday[rando], "apiKey": "d2fc5fadf24b456db9bdd392a2249d65"})
        # print(resp.json())
        data = resp.json()
        globalnews = data['articles'][randonum]
        gtitle = globalnews['title']
        gcontent = globalnews['content']
        gimage = globalnews['urlToImage']
        gurl = globalnews['url']
        return render_template("global.html", gtitle=gtitle, gcontent=gcontent, gimage=gimage, gurl=gurl)


@app.route("/article/<category>")
def articlecategory(category):
    
    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/signup")

    else:
        randonum = random.randint(1, 15)
        resp = requests.get("https://newsapi.org/v2/everything", params={"q":category, "from": todayyesterday[rando], "apiKey": "d2fc5fadf24b456db9bdd392a2249d65"})
        # print(resp.json())
        data = resp.json()
        catnews = data['articles'][randonum]
        cattitle = catnews['title']
        catcontent = catnews['content']
        catimage = catnews['urlToImage']
        caturl = catnews['url']
        return render_template("category.html", cattitle=cattitle, catcontent=catcontent, catimage=catimage, caturl=caturl, category=category)


@app.route("/articletitle/<articlet>", methods=["GET", "POST"])
def showtitle(articlet):

    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/signup")

    else:
        
        randonum = random.randint(1, 6)
        resp = requests.get("https://newsapi.org/v2/everything", params={"qInTitle":articlet, "from": tday, "apiKey": "d2fc5fadf24b456db9bdd392a2249d65"})

        
        data = resp.json()
        titlenews = data['articles'][randonum]

        titletitle = titlenews['title']
        titledescription = titlenews['description']

        #comments
        #user mark as read or unread

        return render_template('articletitle.html', titletitle=titletitle, titledescription=titledescription )


@app.route("/profile")
def getprofile():

    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/signup")
    
    else:

        user = User.query.get_or_404(session["user_id"])
        comments = Comment.query.all()
        articles = Article.query.all()
        
        

        return render_template("profile.html", user=user, comments=comments, articles=articles)



@app.route("/comment/<int:articleid>", methods=["GET", "POST"])
def postcomments(articleid):

    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/signup")
    
    else:

        article = Article.query.get_or_404(articleid)
        




        form = CommentForm(obj=article)
        if form.validate_on_submit():

            article.read = form.read.data
            
            ####CREATE ADDING USERID TO EACH ARTICLE!!

            comment = Comment(user_id=session["user_id"], comment=form.comment.data, article_id=articleid)

            db.session.add(comment)
            
            db.session.commit()

            comments = Comment.query.all()
            
            

            return render_template('commentpost.html', comments=comments, article=article)
        
        return  render_template('comment.html', form=form, article=article)
        

