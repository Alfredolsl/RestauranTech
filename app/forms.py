""" Contains form for login and register """
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
    password = PasswordField(validators=[InputRequired(), Length(min=2, max=128)],
                             render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")


class NewItemForm(FlaskForm):
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
    #print([(row[0], f"{row[1]} ID:{row}") for row in branch_rows])
    branch_id =  SelectField(choices=[row for row in branch_rows], validators=[InputRequired()], render_kw={"placeholder": "Select Branch"})
    
    cur.execute("SELECT asset_id, name FROM assets")
    asset_rows = cur.fetchall()
    asset_id = SelectField(choices=[row for row in asset_rows], validators=[InputRequired()], render_kw={"placeholder": "Select Branch"})

    cur.close()
    db.close()
    
    quantity_in_stock = IntegerField(validators=[InputRequired()], render_kw={"placeholder": "Stock Quantity"})
    unit_of_measure = SelectField(choices=['g', 'kg', 'ml', 'L', 'pieces'])
    average_price = FloatField(validators=[InputRequired()], render_kw={"placeholder": "0.00"})
    shelf_life = IntegerField(validators=[InputRequired()], render_kw={"placeholder": "Shelf Life"})
    shelf_life_unit = SelectField(choices=['days', 'months', 'years'])
    submit = SubmitField("Add Item to Inventory")


class ModifyItemForm(FlaskForm):
    """ Represents form to modify existing item in inventory """
    import MySQLdb
    from os import getenv
    db = MySQLdb.connect(host=getenv('DB_HOST'), port=int(getenv('DB_PORT')),
                         user=getenv('DB_USER'),
                         passwd=getenv('DB_PASSWORD'),
                         db=getenv('DATABASE'))
    cur = db.cursor()
    cur.execute("SELECT branch_id, name FROM branch")
    branch_rows_in_inventory = cur.fetchall()

    total_branch_ids = SelectField(choices=[row for row in branch_rows_in_inventory])
    total_asset_ids = SelectField(choices=["Select a branch first"])

    quantity_in_stock = IntegerField(validators=[InputRequired()], render_kw={"placeholder": "Stock Quantity"})
    unit_of_measure = SelectField(choices=['g', 'kg', 'ml', 'L', 'pieces'])
    average_price = FloatField(validators=[InputRequired()], render_kw={"placeholder": "0.00"})
    shelf_life = IntegerField(validators=[InputRequired()], render_kw={"placeholder": "Shelf Life"})
    shelf_life_unit = SelectField(choices=['days', 'months', 'years'])
    submit = SubmitField("Modify Item")