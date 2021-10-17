from flask import Flask, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, User
from forms import RegisterForm, LoginForm

from sqlalchemy.exc import IntegrityError
# from forms import 
import requests, random, datetime
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','postgresql:///newsapp_capstone')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'helloworld2')
#debug = DebugToolbarExtension(app)

#connect db should go last
connect_db(app)

API_URL = "https://newsapi.org/v2/everything"

#time setup for most recent articles
tday = datetime.date.today()
yday = tday - datetime.timedelta(days = 1)
rando = random.randint(0, 1)
todayyesterday = [tday, yday]
# -------


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
            return redirect("/global")

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
        return redirect("/global")
    
    else:
        return render_template("signup.html", form=form)

@app.route("/global")
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

@app.route("/national")
def national():

    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/signup")

    else:
        randonum = random.randint(1, 15)

        resp = requests.get("https://newsapi.org/v2/everything", params={"q":"usa", "from": todayyesterday[rando], "apiKey": "d2fc5fadf24b456db9bdd392a2249d65"})

        # print(resp.json())
        data = resp.json()
        natnews = data['articles'][randonum]
        ###-------###
        ntitle = natnews['title']
        ncontent = natnews['content']
        nimage = natnews['urlToImage']
        nurl = natnews['url']

        return render_template("national.html", ntitle=ntitle, ncontent=ncontent, nimage=nimage, nurl=nurl)

@app.route("/technology")
def technology():

    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/signup")

    else:
        randonum = random.randint(1, 15)

        resp = requests.get("https://newsapi.org/v2/everything", params={"q":"tech", "from": todayyesterday[rando], "apiKey": "d2fc5fadf24b456db9bdd392a2249d65"})

        # print(resp.json())
        data = resp.json()
        technews = data['articles'][randonum]
        #####
        ttitle = technews['title']
        tcontent = technews['content']
        timage = technews['urlToImage']
        turl = technews['url']
        return render_template("technology.html", ttitle=ttitle, tcontent=tcontent, timage=timage, turl=turl)

@app.route("/science")
def science():

    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/signup")

    else:

        randonum = random.randint(1, 15)

        resp = requests.get("https://newsapi.org/v2/everything", params={"q":"science", "from": todayyesterday[rando], "apiKey": "d2fc5fadf24b456db9bdd392a2249d65"})

        # print(resp.json())
        data = resp.json()
        sciencenews = data['articles'][randonum]
        ###
        stitle = sciencenews['title']
        scontent = sciencenews['content']
        simage = sciencenews['urlToImage']
        surl = sciencenews['url']
        
        return render_template("science.html", stitle=stitle, scontent=scontent, simage=simage, surl=surl)

@app.route("/economic")
def economic():

    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/signup")

    else:
        randonum = random.randint(1, 15)

        resp = requests.get("https://newsapi.org/v2/everything", params={"q":"economy", "from": todayyesterday[rando], "apiKey": "d2fc5fadf24b456db9bdd392a2249d65"})

        # print(resp.json())
        data = resp.json()
        economicnews = data['articles'][randonum]
        ###
        etitle = economicnews['title']
        econtent = economicnews['content']
        eimage = economicnews['urlToImage']
        eurl = economicnews['url']


        return render_template("economic.html", etitle=etitle, econtent=econtent, eimage=eimage, eurl=eurl)

@app.route("/entertainment")
def entertainment():

    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/signup")

    else:
        randonum = random.randint(1, 15)

        resp = requests.get("https://newsapi.org/v2/everything", params={"q":"entertainment", "from": todayyesterday[rando], "apiKey": "d2fc5fadf24b456db9bdd392a2249d65"})

        # print(resp.json())
        data = resp.json()
        entertainmentnews = data['articles'][randonum]
        ###
        ettitle = entertainmentnews['title']
        etcontent = entertainmentnews['content']
        etimage = entertainmentnews['urlToImage']
        eturl = entertainmentnews['url']

        return render_template("entertainment.html", ettitle=ettitle, etcontent=etcontent, etimage=etimage, eturl=eturl)


@app.route("/travel")
def travel():
    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/signup")

    else:
        randonum = random.randint(1, 15)

        resp = requests.get("https://newsapi.org/v2/everything", params={"q":"travel", "from": todayyesterday[rando], "apiKey": "d2fc5fadf24b456db9bdd392a2249d65"})

        # print(resp.json())
        data = resp.json()
        travelnews = data['articles'][randonum]
        ###
        trtitle = travelnews['title']
        trcontent = travelnews['content']
        trimage = travelnews['urlToImage']
        trurl = travelnews['url']


        return render_template("travel.html", trtitle=trtitle, trcontent=trcontent, trimage=trimage, trurl=trurl)



