""" Contains form for login and register """
from app.models.user import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField
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
        if existing_email:
            return True
        return False
        
    def validate_name(self, name):
        """ Returns True if name is already used """
        existing_name = User.query.filter_by(name=name).first()
        if existing_name:
            return True
        return False
    

class LoginForm(FlaskForm):
    """ Represents login form """
    email = StringField(validators=[InputRequired(), Length(min=4, max=128)],
                        render_kw={"placeholder": "Email"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=128)],
                             render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")


class InventoryForm(FlaskForm):
    """ Represents Form to register and item in the inventory """
    branch_id = IntegerField(validators=[InputRequired(), Length(min=1)], render_kw={"placeholder": "Branch ID"})
    asset_id = IntegerField(validators=[InputRequired(), Length(min=1)], render_kw={"placeholder": "Asset id"})
    quantity_in_stock = IntegerField(validators=[InputRequired(), Length(min=1)], render_kw={"placeholder": "Stock quantity"})
    unit_of_measure = SelectField("Unit of Measure", choices=["g", "kg", "ml", "L"])
    average_price = IntegerField(validators=[InputRequired(), Length(min=1)], render_kw={"placeholder": "Average Price"})
    shelf_life = IntegerField(validators=[InputRequired(), Length(min=1)], render_kw={"placeholder": "Shelf Life"})
    shelf_life_unit = IntegerField(validators=[InputRequired(), Length(min=1)], render_kw={"placeholder": "Shelf Life Unit (Days, Months...)"})
    submit = SubmitField("Add to inventory")