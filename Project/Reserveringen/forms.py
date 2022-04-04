from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                                  RadioField, SelectField,
                                  TextAreaField, SubmitField, IntegerField)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rddg5'

class Reserveren(FlaskForm):
    huisje = SelectField(u'Welk huisje wilt u boeken?', choices=[(1, 'Trekkershut'), (2, 'Bungelow'), (3, 'Villa')], validators=[DataRequired()])
    week = IntegerField(u'Welke week wilt u boeken', validators=[DataRequired()])
    submit = SubmitField('Verzend')

class Week_Wijzigen(FlaskForm):
    huisje = SelectField(u'In welk huisje heeft u momenteel een reservering?', choices=[(1, 'Trekkershut'), (2, 'Bungelow'), (3, 'Villa')], validators=[DataRequired()])
    week = IntegerField(u'Welke week heeft u momenteel gereserveerd?', validators=[DataRequired()])
    nieuwe_week = IntegerField(u'Naar welke week wilt u wijzigen?', validators=[DataRequired()])
    submit = SubmitField('Verzend')

class Huisje_wijzigen(FlaskForm):
    huisje = SelectField(u'In welk huisje heeft u momenteel een reservering?', choices=[(1, 'Trekkershut'), (2, 'Bungelow'), (3, 'Villa')], validators=[DataRequired()])
    week = IntegerField(u'Welke week heeft u momenteel gereserveerd?', validators=[DataRequired()])
    nieuw_huisje = SelectField(u'Naar welk huisje wilt u wijzigen?', choices=[(1, 'Trekkershut'), (2, 'Bungelow'), (3, 'Villa')], validators=[DataRequired()])
    submit = SubmitField('Verzend')