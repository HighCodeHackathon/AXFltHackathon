"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
import uuid

from Postin import app
from Postin import model

from Postin import db

##### Create DB #####

# db.create_all()

##### Card Logic #####

@app.route('/')
@app.route('/home')

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
def congrats():
    """Renders the cards page."""
    return render_template(
        'congrats.html',
        title='POSTIN - Congrats',
        year=datetime.now().year,
        )

@app.route('/profile')
def profile():
    """Renders the home page."""
    return render_template(
        'profile.html',
        title='Postin - Profile',
        year=datetime.now().year,
    )

@app.route('/login')
def login():
    """Renders the home page."""
    return render_template(
        'login.html',
        title='Postin - Login',
        year=datetime.now().year,
    )

@app.route('/init')
def init():
    """Renders the home page."""
    #model.Utility.initDb(10, "HRT SAC", "RAF Leeming", "North Yorkshire", "CPL")
    #model.Utility.initDbUser(0, "admin", "user", "30146824", "P@ssw0rd")
    db.session.commit()
    return render_template(
    'cards.html',
    title ='POSTIN - Swipe',
    year=datetime.now().year,
)

