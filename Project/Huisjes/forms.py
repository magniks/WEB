from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                                  RadioField, SelectField,
                                  TextAreaField, SubmitField, IntegerField)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'radd4'

class Beschikbaarheid(FlaskForm):
    week = IntegerField(u'Van welke week wilt u de beschikbaarheid van dit huisje zien?', validators=[DataRequired()])
    submit = SubmitField('Verzend')
