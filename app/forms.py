from app.models.user import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FloatField, SelectField
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
<<<<<<< HEAD
=======

class InventoryForm(FlaskForm):
    """ Represents form to add item to inventory """
    import MySQLdb
    from os import getenv
    db = MySQLdb.connect(host=getenv('DB_HOST'), port=int(getenv('DB_PORT')),
                         user=getenv('DB_USER'),
                         passwd=getenv('DB_PASSWORD'),
                         db=getenv('DATABASE'))
    cur = db.cursor()

    # Capture data from databases to return a list of choices
    # for user to select the name of an asset/branch, then gets translated to the id.
    cur.execute("SELECT branch_id, name FROM branch")
    branch_rows = cur.fetchall()
    branch_id =  SelectField(choices=[row for row in branch_rows], validators=[InputRequired()], render_kw={"placeholder": "Select Branch"})
    
    cur.execute("SELECT asset_id, name FROM assets")
    asset_rows = cur.fetchall()
    asset_id = SelectField(choices=[row for row in asset_rows], validators=[InputRequired()], render_kw={"placeholder": "Select Branch"})

    cur.close()
    db.close()
    
    quantity_in_stock = IntegerField(validators=[InputRequired()], render_kw={"placeholder": "Stock Quantity"})
    unit_of_measure = SelectField(choices=['g', 'kg', 'ml', 'L'])
    average_price = FloatField(validators=[InputRequired()], render_kw={"placeholder": "0.00"})
    shelf_life = IntegerField(validators=[InputRequired()], render_kw={"placeholder": "Shelf Life"})
    shelf_life_unit = SelectField(choices=['days', 'months', 'years'])
    submit = SubmitField("Add Item to Inventory")
>>>>>>> 43d4df0c7f0b01434bf5b7969995d9acf68efa86
