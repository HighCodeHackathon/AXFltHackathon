from Postin import db
from flask_login import LoginManager
import uuid
import json

#### App Models #####

class CardStack():
    def generateStack(self):

        # Get Data From Database and submit to new card object

        postingTable = Posting.query.filter_by(rank= "SAC" ).first()
        print(postingTable.id)

        # Test getting one card from card object
        card0 = self.Card()
        print(card0.cardJSON)

    def __init__(self):
        self.id = uuid.uuid4()
        self.maxStackHeight = 10
        self.cardList = []
        self.generateStack()

    class Card():
        def __init__(self):
            self.id = str(uuid.uuid4())
            self.title = "Blank Card"
            self.subTitle = "This is a placeholder card"
            self.imageURL = "https://via.placeholder.com/400x600?text=CardImage"
            self.cardJSON = self.generateCardJSON()

        def generateCardJSON(self):
            # Create dictionary first.
            card = [self.id, self.title, self.subTitle, self.imageURL]
            # Convert into JSON object.
            returnJSON = json.dumps(card)

            return returnJSON

#### SQL Alchemy Models ####

class User(db.Model):
    tablename = 'user'
    id = db.Column(db.CHAR(64), primary_key=True)
    firstName = db.Column(db.String(80), unique=True, nullable=False)
    lastName = db.Column(db.String(80), unique=False, nullable=False)
    serviceNumber = db.Column(db.String(80), unique = True, nullable = False)
    password = db.Column(db.String)
    trade = db.Column(db.String(80), unique=False, nullable=True)
    rank = db.Column(db.String(80), unique=False, nullable=True)
    fadEnd = db.Column(db.DateTime)
    locationPref1 = db.Column(db.String(80), unique=False, nullable=True)
    locationPref2 = db.Column(db.String(80), unique=False, nullable=True)
    jobPref1 = db.Column(db.String(80), unique=False, nullable=True)
    jobPref2 = db.Column(db.String(80), unique=False, nullable=True)
    authenticated = db.Column(db.Boolean, default=False, nullable=True)

class Posting(db.Model):
    tablename = 'posting'
    id = db.Column(db.CHAR(64), primary_key=True)
    location = db.Column(db.String(80), unique=False, nullable=True)
    county = db.Column(db.String(80), unique=False, nullable=True)
    jobTitle = db.Column(db.String(80), unique=True, nullable=True)
    availabilityDate = db.Column(db.DateTime)
    jobBio = db.Column(db.String(200), unique=False, nullable=True)
    localInfo = db.Column(db.String(200), unique=False, nullable=True)
    imageLink = db.Column(db.String(200), unique=False, nullable=True)
    reviewLink = db.Column(db.String(200), unique=False, nullable=True)
    rank = db.Column(db.String(80), unique=False, nullable=True)
    priority = db.Column(db.Boolean, unique=False, nullable=True)

class Matches(db.Model):
    tablename = 'matches'
    id = db.Column(db.CHAR(64), primary_key=True)
    jobTitle = db.Column(db.String(80), unique=True, nullable=False)
    location = db.Column(db.String(80), unique=False, nullable=False)
    county = db.Column(db.String(80), unique=False, nullable=False)
    jobRank = db.Column(db.String(80), unique=False, nullable=False)
    availabilityDate = db.Column(db.DateTime)
    username = db.Column(db.String(80), unique=True, nullable=False)
    serviceNumber = db.Column(db.String(80), unique = True, nullable = False)
    trade = db.Column(db.String(80), unique=False, nullable=False)
    userRank = db.Column(db.String(80), unique=False, nullable=False)
    fadEnd = db.Column(db.DateTime)

####### Authentication Models ######

login_manager = LoginManager()

def is_active(self):
        """True, as all users are active."""
        return True

def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve

    """
    return User.query.get(user_id)

####### Utility Functions #######

class Utility():
    #

    def initDb(noOfPosts, jobTitle, location, county, rank, priority = "N"):
        i = 0
        x = noOfPosts
        jobUID = 1
        while i <= x:
            db.session.add(Posting(id=uuid.uuid4(), jobTitle=jobTitle + " " + str(jobUID), location=location, county = county, rank = rank, priority = 0 ))
            i += 1
            jobUID += 1
        
    db.session.commit()

    def initDbUser(noOfUsers,firstName,lastName,serviceNumber,password):
        i = 0
        x = noOfUsers
        while i <= x:
            db.session.add(User(id=uuid.uuid4(), firstName=firstName, serviceNumber = serviceNumber, password=password))
            i += 1
                    
    db.session.commit()


#### Database Initialisation & Testing #####


#db.create_all()

#db.session.add(model.Posting(id=uuid.uuid4(), jobTitle="Dogsbody Generic Manpower SAC 345", location="RAF Leeming"))
#db.session.commit()