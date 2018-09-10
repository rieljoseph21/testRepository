from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class SignUpForm(FlaskForm):
    fullname = StringField('FULL NAME',
                           validators=[DataRequired(), Length(min=2, max=30)]
                           )
    email = StringField('EMAIL', validators=[DataRequired(), Email()])
    password = PasswordField('PASSWORD', validators=[
                             DataRequired(), Length(min=5, max=20)])
    confirm_password = PasswordField('CONFIRM PASSWORD', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class SignInForm(FlaskForm):
    email = StringField('EMAIL', validators=[DataRequired(), Email()])
    password = PasswordField('PASSWORD', validators=[
                             DataRequired(), Length(min=5, max=20)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
