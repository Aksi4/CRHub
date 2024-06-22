from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, InputRequired, Email, ValidationError, Regexp, EqualTo
from flask_wtf.file import FileField, FileAllowed
from .models import Post
from flask_login import current_user

from wtforms import FloatField

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    contacts = TextAreaField('Contacts', validators=[DataRequired()])
    picture = FileField('Picture', validators=[FileAllowed(['jpg', 'png'])])
    type = SelectField('Region', choices=[('Zakarpattia', 'Zakarpattia'), ('Ivano-Frankivsk', 'Ivano-Frankivsk'), ('Chernivtsi', 'Chernivtsi'), ('Lviv', 'Lviv'), ('Other', 'Other')],
                       default='Other', validators=[DataRequired()])
    enabled = BooleanField('Enabled', default=True)
    latitude = FloatField('Latitude')
    longitude = FloatField('Longitude')
    submit = SubmitField('Submit')

class ReviewsForm(FlaskForm):
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')




