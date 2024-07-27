""" File containing all routes for the project """
from app import app, db, login_manager
from app.forms import RegisterForm, LoginForm, NewItemForm, ModifyItemForm
from app.models.user import User
from app.models.inventory import Inventory
from flask import render_template, redirect, url_for, session
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('index.html',
                           logged_in=current_user.is_authenticated)


@app.route('/crm')
@login_required
def crm():
    user_info = {
        'id': current_user.user_id
    }
    return render_template('admin.html', user_info=user_info)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.is_submitted():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()

        if not user:
            print("user doesn't exist")
            return redirect(url_for("login"))
        
        elif not check_password_hash(user.password, password):
            print("wrong password")
            return redirect(url_for("login"))
        
        else:
            login_user(user)
            return redirect(url_for("crm"))

    return render_template('login.html', form=form)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.is_submitted():
        email = form.email.data
        if not form.duplicate_email(email):
            name = form.name.data
            hashed_password = generate_password_hash(form.password.data,
                                                    method="pbkdf2:sha256",
                                                    salt_length=8)
            new_user = User(name=name, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('crm'))

    return render_template('register.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/inventory', methods=["GET", "POST"])
def inventory():
    form = NewItemForm()

    if form.is_submitted():
        branch_id = form.branch_id.data
        asset_id = form.asset_id.data
        quantity_in_stock = form.quantity_in_stock.data
        unit_of_measure = form.unit_of_measure.data
        average_price = form.average_price.data
        shelf_life = form.shelf_life.data
        shelf_life_unit = form.shelf_life_unit.data

        existing_item = Inventory.query.filter_by(branch_id=branch_id, asset_id=asset_id).first()
        if existing_item:
            print("item already exists.")
        else:
            new_item = Inventory(branch_id=branch_id, asset_id=asset_id,
                                quantity_in_stock=quantity_in_stock, unit_of_measure=unit_of_measure,
                                average_price=average_price, shelf_life=shelf_life,
                                shelf_life_unit=shelf_life_unit)
            db.session.add(new_item)
            db.session.commit()
            print("item added successfully!")

    return render_template('inventory.html', form=form)

@app.route('/editinv', methods=["GET", "POST"])
def editinv():
    form = ModifyItemForm()
    can_modify = False

    if form.is_submitted():
        from os import getenv
        import MySQLdb
        db = MySQLdb.connect(host=getenv('DB_HOST'), port=int(getenv('DB_PORT')),
                         user=getenv('DB_USER'),
                         passwd=getenv('DB_PASSWORD'),
                         db=getenv('DATABASE'))
        cur = db.cursor()
        selected_branch_id = form.total_branch_ids.data
        cur.execute(f"SELECT inv.asset_id, assets.name \
                    FROM inventory inv \
                    INNER JOIN assets \
                    ON inv.asset_id = assets.asset_id \
                    WHERE inv.branch_id = {selected_branch_id}")
        total_branch_ids_from_asset_id = cur.fetchall()

        can_modify = True

        form.total_asset_ids.choices = [ids for ids in total_branch_ids_from_asset_id]


    return render_template("edit_inventory.html", form=form, can_modify=can_modify)