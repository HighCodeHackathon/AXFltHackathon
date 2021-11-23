"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


import uuid

from Postin import app
from Postin import model

from Postin import db

##### Create DB #####

# db.create_all()
model.Utility.initDbUser(1,"admin","user","00000000","p@ssw0rd!")

##### Card Logic #####

@app.route('/')
@app.route('/home')
@login_required
def home():
    """Renders the card page."""
    
    cardStack = model.CardStack()

    return render_template(
        'cards.html',
        title ='POSTIN - Swipe',
        cardSet = cardStack.cardList,
        year=datetime.now().year,
    )

@app.route('/congrats')
@login_required
def congrats():
    """Renders the cards page."""
    return render_template(
        'congrats.html',
        title='POSTIN - Congrats',
        year=datetime.now().year,
        )

@app.route('/profile')
@login_required
def profile():
    """Renders the home page."""
    return render_template(
        'profile.html',
        title='Postin - Profile',
        year=datetime.now().year,
    )

@app.route("/login", methods=["GET", "POST"])
def login():
    """For GET requests, display the login form. 
    For POSTS, login the current user by processing the form.

    """
    print(model.User.query.filter_by(serviceNumber = "serviceNumber").first())
    form = LoginForm()
    if form.validate_on_submit():
        user = user.query.get(form.serviceNumber.data)
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect(url_for("app.profile"))
    """Renders the home page."""
    return render_template(
        'login.html',
        title='Postin - Login',
        year=datetime.now().year,
    )

@app.route('/init')
def init():
    """Renders the home page."""
    model.Utility.initDb(10, "HRT SAC", "RAF Leeming", "North Yorkshire", "CPL")
    
    return render_template(
    'cards.html',
    title ='POSTIN - Swipe',
    year=datetime.now().year,
    )


