from flask import Flask, render_template, redirect, url_for
app = Flask(__name__, template_folder="bungalowpark/templates/", static_folder="bungalowpark/static/")
from Reserveringen.forms import Reserveren
from Huisjes.forms import Beschikbaarheid
from beheer_reserveringen import db, Huis, Soort, Gast, Boeking
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select

@app.route("/")
def index():
# TODO: Uitzoeken hoe variabelen in een pagina te krijgen zonder ze in de url te doen
# en zonder ze local te maken zoals hier
#    if gebruiker is None or gebruiker == "":
    gebruiker = "onbekende gebruiker"
        
    return render_template("index.html", gebruiker=gebruiker)

@app.route("/reserveringen")
def reserveringen():
    return render_template("reserveringen.html")

@app.route('/reserveren', methods=['GET', 'POST'])
def add_cur():
    form = Reserveren()

    if form.validate_on_submit():
        week = form.week.data
        huisje = form.huisje.data
        userID = current_user.id

        # Voeg een nieuwe cursist toe aan de database
        nieuwe_boeking = Boeking(userID, huisje, week)
        db.session.add(nieuwe_boeking)
        db.session.commit()

        return redirect(url_for('reserveringen'))

    return render_template('reserveren.html',form=form)

@app.route('/huisjes', methods=['GET', 'POST'])
def huisjes():
    form = Beschikbaarheid()

    if form.validate_on_submit():
        week = form.week.data

        # Voeg een nieuwe cursist toe aan de database
        beschikbaar = select(huisjes.naam).where(boekingen.week != week)
        print(beschikbaar)

        return redirect(url_for('reserveringen'))

    return render_template("huisjes.html")