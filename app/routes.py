from app import app, db, login_manager
from app.forms import RegisterForm, LoginForm, InventoryForm
from app.models.user import User
from app.models.inventory import Inventory
from app.models.branch import Branch  # Asegúrate de tener este modelo
from app.models.assets import Assets  # Asegúrate de tener este modelo
from flask import render_template, redirect, url_for, flash, session, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('index.html', logged_in=current_user.is_authenticated)

@app.route('/crm')
@login_required
def crm():
    user_info = {
        'id': current_user.user_id
    }
    assets_in_inventory = db.session.query(Assets.asset_id, Assets.picture, Assets.name, Assets.description, Inventory.quantity_in_stock, Inventory.unit_of_measure, Branch.name, Branch.branch_id)\
                          .join(Inventory, Inventory.asset_id == Assets.asset_id).join(Branch, Inventory.branch_id == Branch.branch_id).all()
    
    inventory_data = [
        {
            'asset_id': asset_id,
            'asset_picture': picture,
            'asset_name': name,
            'asset_description': description,
            'quantity_in_stock': quantity_in_stock,
            'unit_of_measure': unit_of_measure,
            'branch_name': branch_name,
            'branch_id': branch_id
        }
        for asset_id, picture, name, description, quantity_in_stock, unit_of_measure, branch_name, branch_id in assets_in_inventory
    ]
    # sorts by asset id to organize without having multiple items scattered throughout the listing
    inventory_data = sorted(inventory_data, key=lambda x: x['asset_id'])

    # pagination
    page = request.args.get('page', 1, type=int)
    per_page = 10
    start = (page - 1) * per_page
    end = start + per_page
    total_pages = (len(assets_in_inventory) + per_page - 1) // per_page
    assets_per_page = inventory_data[start:end]

    assets_unit_of_measure = InventoryForm.unit_of_measure.kwargs.get('choices')

    all_suppliers = db.session.query(Branch.branch_id, Branch.name).all()

    return render_template('crm.html', user_info=user_info, inventory_data=assets_per_page, assets_unit_of_measure=assets_unit_of_measure,
                            all_suppliers=all_suppliers, total_pages=total_pages, page=page)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('crm'))
        else:
            flash('Invalid email or password', 'danger')
    
    return render_template('login.html', form=form)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        email = form.email.data
        if not form.duplicate_email(email):
            name = form.name.data
            hashed_password = generate_password_hash(form.password.data, method="pbkdf2:sha256", salt_length=8)
            new_user = User(name=name, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('crm'))
        else:
            flash('Email already registered', 'danger')
    
    return render_template('register.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route('/inventory')
@login_required
def inventory():
    user_info = {
        'id': current_user.user_id
    }
    return render_template('crm.html', user_info=user_info)

@app.route('/addinventory', methods=["GET", "POST"])
def addinventory():
    branches = Branch.query.all()
    assets = Assets.query.all()

    branch_choices = [(branch.branch_id, branch.name) for branch in branches][:1]
    form = InventoryForm()
    form.branch_id.choices = branch_choices

    #asset_choices = [(asset.asset_id, asset.name) for asset in assets]
    #form.asset_id.choices = asset_choices

    if form.is_submitted():
        branch_id = form.branch_id.data

        asset_id = form.asset_id.data

        quantity_in_stock = form.quantity_in_stock.data
        unit_of_measure = form.unit_of_measure.data
        average_price = form.average_price.data
        shelf_life = form.shelf_life.data
        shelf_life_unit = form.shelf_life_unit.data
        user_id = form.user_id.data

        # Check if asset exists by ID to add it to Assets table, if not, add quantity_in_stock and update average_price
        asset_text = request.form.get("asset_text")
        existing_asset = Assets.query.filter_by(name=asset_text).first()

        if not existing_asset:
            new_asset = Assets(name=asset_text, description="New asset description", picture="default_picture_url")
            db.session.add(new_asset)
            db.session.flush()
            asset_id = new_asset.asset_id

            new_item = Inventory(branch_id=branch_id,
                             asset_id=asset_id,
                             quantity_in_stock=quantity_in_stock,
                             unit_of_measure=unit_of_measure,
                             average_price=average_price,
                             shelf_life=shelf_life,
                             shelf_life_unit=shelf_life_unit,
                             user_id=int(user_id))
            db.session.add(new_item)
        else:
            existing_item = Inventory.query.filter_by(branch_id=branch_id, asset_id=existing_asset.asset_id).first()
            existing_item.quantity_in_stock += quantity_in_stock
            existing_item.average_price = average_price
            asset_id = existing_asset.asset_id

        db.session.commit()
        flash("Item added successfully!", "success")

    form.user_id.data = current_user.user_id
    return render_template('inventory.html', form=form)


@app.route('/costs')
@login_required
def costs():
    user_info = {
        'id': current_user.user_id
    }
    return render_template('crm.html', user_info=user_info)


@app.errorhandler(401)
def unauthorized(e):
    """ Error handler if user is not logged in """
    return 'You are not logged in to visit this page. '\
            r'<a href="/">Go to home page</a> <a href="/register">Register</a> <a href="/login">Login</a>', 401