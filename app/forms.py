from app.models.user import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

class RegisterForm(FlaskForm):
    """ Represents registration form """
    name = StringField(validators=[InputRequired(), Length(min=4, max=64)],
                       render_kw={"placeholder": "Username"})
    email = StringField(validators=[InputRequired(), Length(min=4, max=128)],
                        render_kw={"placeholder": "Email"})
    password = PasswordField(validators=[InputRequired(), Length(min=2, max=128)],
                             render_kw={"placeholder": "Password"})
    submit = SubmitField("Register")

    def duplicate_email(self, email):
        """ Returns True if email is already used """
        existing_email = User.query.filter_by(email=email).first()
        return existing_email is not None
        
    def validate_name(self, name):
        """ Returns True if name is already used """
        existing_name = User.query.filter_by(name=name).first()
        return existing_name is not None
    

class LoginForm(FlaskForm):
    """ Represents login form """
    email = StringField(validators=[InputRequired(), Length(min=4, max=128)],
                        render_kw={"placeholder": "Email"})
    password = PasswordField(validators=[InputRequired(), Length(min=2, max=128)],
                             render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")
