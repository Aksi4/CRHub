from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, InputRequired, Email, ValidationError, Regexp, EqualTo


class ReviewForm(FlaskForm):
    
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')




