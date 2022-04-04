import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#Zoek de locatie van dit bestand
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

class Soort(db.Model):
    __tablename__ = 'soorten'

    # Primary Key column, uniek voor iedere cursist
    id = db.Column(db.Integer,primary_key=True)
    # Hoeveelheid personen
    personen = db.Column(db.Integer)
    # Prijs van de bungelow per nacht
    prijs = db.Column(db.Integer)

    huisjes = db.relationship('Huis',backref='soort',lazy='dynamic')

    # Hier wordt aangegeven wat iedere instantie meekrijgt aan het begin
    # Merk op dat de ID later automatisch voor ons wordt aangemaakt, dus we voegen deze hier niet toe!
    def __init__(self,personen,prijs):
        self.personen = personen
        self.prijs = prijs

    def __repr__(self):
        # Deze tekst wordt getoond als een cursist wordt aangeroepen
        return f"Een huisje voor {self.personen} personen kost {self.prijs} euro per nacht."

# Overerven van de klasse db.Model
class Huis(db.Model):
    __tablename__ = 'huisjes'

    # Primary Key column, uniek voor iedere cursist
    id = db.Column(db.Integer,primary_key=True)
    # Naam van het huisje
    naam = db.Column(db.Text)
    # ID van het soort huisje
    soort_id = db.Column(db.Integer, db.ForeignKey('soorten.id'))

    boeking = db.relationship('Boeking',backref='huis',lazy='dynamic')


    # Hier wordt aangegeven wat iedere instantie meekrijgt aan het begin
    # Merk op dat de ID later automatisch voor ons wordt aangemaakt, dus we voegen deze hier niet toe!
    def __init__(self,naam,soort_id):
        self.naam = naam
        self.soort_id = soort_id

    def __repr__(self):
        # Deze tekst wordt getoond als een cursist wordt aangeroepen
        return f"Huisje {self.naam} is het type {self.soort_id} "

class Gast(db.Model):
    __tablename__ = 'gasten'

    # Primary Key column, uniek voor iedere cursist
    id = db.Column(db.Integer,primary_key=True)
    # Gebruikersnaam van de gast
    gebruikersnaam = db.Column(db.Integer)
    # Wachtwoord van de gebruiker
    wachtwoord = db.Column(db.Integer)

    boeking = db.relationship('Boeking',backref='gast',lazy='dynamic')

    # Hier wordt aangegeven wat iedere instantie meekrijgt aan het begin
    # Merk op dat de ID later automatisch voor ons wordt aangemaakt, dus we voegen deze hier niet toe!
    def __init__(self,gebruikersnaam,wachtwoord):
        self.gebruikersnaam = gebruikersnaam
        self.wachtwoord = wachtwoord

    def __repr__(self):
        # Deze tekst wordt getoond als een cursist wordt aangeroepen
        return f"Voor gast {self.gebruikersnaam} hoort wachtwoord {self.wachtwoord}"

class Boeking(db.Model):
    __tablename__ = 'boekingen'

    # Primary Key column, uniek voor iedere boeking
    id = db.Column(db.Integer,primary_key=True)
    # Id van gast
    gast_id = db.Column(db.Integer, db.ForeignKey('gasten.id'))
    # ID van bungelow
    bungelow_id = db.Column(db.Integer, db.ForeignKey('huisjes.id'))
    #Week van bezoek
    week = db.Column(db.Integer)


    # Hier wordt aangegeven wat iedere instantie meekrijgt aan het begin
    # Merk op dat de ID later automatisch voor ons wordt aangemaakt, dus we voegen deze hier niet toe!
    def __init__(self,gast_id,bungelow_id,week):
        self.gast_id = gast_id
        self.bungelow_id = bungelow_id
        self.week = week

    def __repr__(self):
        # Deze tekst wordt getoond als een cursist wordt aangeroepen
        return f"Voor de gast met id {self.gast_id} is bungelow met id {self.bungelow_id} geboekt in week {self.week}"