from Postin import db
import uuid
import json

#### App Models #####

class CardStack():

    def generateStack(self):

        # Get Data From Database and submit to new card object

        DbSet = Posting.query.filter_by(rank= "CPL" ).order_by(Posting.jobTitle)
        print(DbSet)

        # Test getting one card from card object
        card0 = Card(DbSet[0].jobTitle, DbSet[0].location, DbSet[0].imageLink, DbSet[0].jobBio)
        card1 = Card(DbSet[1].jobTitle, DbSet[1].location, DbSet[1].imageLink, DbSet[1].jobBio)
        card2 = Card(DbSet[2].jobTitle, DbSet[2].location, DbSet[2].imageLink, DbSet[2].jobBio)
        card3 = Card(DbSet[3].jobTitle, DbSet[3].location, DbSet[3].imageLink, DbSet[3].jobBio)
        card4 = Card(DbSet[4].jobTitle, DbSet[4].location, DbSet[4].imageLink, DbSet[4].jobBio)
        card5 = Card(DbSet[5].jobTitle, DbSet[5].location, DbSet[5].imageLink, DbSet[5].jobBio)
        card6 = Card(DbSet[6].jobTitle, DbSet[6].location, DbSet[6].imageLink, DbSet[6].jobBio)

        cardList = [card0.card, card1.card, card2.card, card3.card, card4.card, card5.card, card6.card]
        print("Cardlist Dump" + " " + str(cardList))

        return json.dumps(cardList)

    def __init__(self):
        self.id = uuid.uuid4()
        self.maxStackHeight = 10
        self.cardList = self.generateStack()

class Card():
    def __init__(self, title, subTitle, imageURL, jobBio):
        self.id = str(uuid.uuid4())
        self.title = title
        self.subTitle = subTitle
        self.imageURL = imageURL
        self.jobBio = jobBio
        self.card = self.generateCard(title, subTitle, imageURL, jobBio)
        

    def generateCard(self, title, subTitle, imageURL, jobBio):
        # Create dictionary first.
        card = {"id": self.id, "title": self.title, "subTitle": self.subTitle, "imageURL": self.imageURL, "jobBio": self.jobBio}
        cardJson = json.dumps(card)
        return card

#### SQL Alchemy Models ####

class User(db.Model):
    tablename = 'user'
    id = db.Column(db.CHAR(64), primary_key=True)
    firstName = db.Column(db.String(80), unique=False, nullable=False)
    lastName = db.Column(db.String(80), unique=False, nullable=False)
    serviceNumber = db.Column(db.String(80), unique = True, nullable = False)
    password = db.Column(db.String(80), unique=False, nullable=True)
    trade = db.Column(db.String(80), unique=False, nullable=True)
    rank = db.Column(db.String(80), unique=False, nullable=True)
    fadEnd = db.Column(db.DateTime)
    locationPref1 = db.Column(db.String(80), unique=False, nullable=True)
    locationPref2 = db.Column(db.String(80), unique=False, nullable=True)
    jobPref1 = db.Column(db.String(80), unique=False, nullable=True)
    jobPref2 = db.Column(db.String(80), unique=False, nullable=True)

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



####### Utility Functions ########

class Utility():

    def initDb(noOfPosts, jobTitle, location, county, rank, priority = "N"):
        i = 0
        x = noOfPosts
        jobUID = 1
        while i <= x:
            db.session.add(Posting(id=uuid.uuid4(), jobTitle=jobTitle + " " + str(jobUID), location=location, county = county, rank = rank, priority = 0 ))
            i += 1
            jobUID += 1
        
    db.session.commit()

    def initDbUser(noOfUsers, firstName, lastName, serviceNumber, password):
        i = 0
        x = noOfUsers
        
        while i <= x:
            db.session.add(User(id=uuid.uuid4(), firstName = firstName, lastName = lastName, serviceNumber = serviceNumber, password = password))
            i += 1
        
    db.session.commit()


#### Database Initialisation & Testing #####


#db.create_all()

#db.session.add(model.Posting(id=uuid.uuid4(), jobTitle="Dogsbody Generic Manpower SAC 345", location="RAF Leeming"))
#db.session.commit()