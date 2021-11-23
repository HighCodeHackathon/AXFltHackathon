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

@app.route('/card0')
def card0():
    """Renders the cards page."""
    return render_template(
        'card0.html',
        title='card0',
        year=datetime.now().year,
        )

@app.route('/cards1')
def cards1():
    """Renders the cards page."""
    return render_template(
        'cards1.html',
        title='cards1',
        year=datetime.now().year,
        )

@app.route('/cards2')
def cards2():
    """Renders the cards page."""
    return render_template(
        'cards2.html',
        title='cards2',
        year=datetime.now().year,
        )

@app.route('/cards3')
def cards3():
    """Renders the cards page."""
    return render_template(
        'cards3.html',
        title='cards3',
        year=datetime.now().year,
        )

@app.route('/cm')
def cm():
    """Renders the cards page."""
    return render_template(
        'cm.html',
        title='Career Manager',
        year=datetime.now().year,
        )

@app.route('/notification')
def notification():
    """Renders the cards page."""
    return render_template(
        'notification.html',
        title='Notification',
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

@app.route('/cardspriority')
def cardspriority():
    """Renders the home page."""
    return render_template(
        'cardspriority.html',
        title='Postin - Priority Card',
        year=datetime.now().year,
    )

@app.route('/notifcation')
def notifcation():
    """Renders the notificaiton page."""
    return render_template(
        'notifcation.html',
        title='Postin - Notification',
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